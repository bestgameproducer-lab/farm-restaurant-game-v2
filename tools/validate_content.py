#!/usr/bin/env python3
"""Validate EMP-001 source fixtures. No engine, network, or extra packages required."""
from __future__ import annotations
import argparse
import json
import math
import sys
from pathlib import Path


def validate(catalog: dict, definitions: dict, knowledge: dict) -> list[str]:
    errors: list[str] = []
    def need(ok: bool, message: str) -> None:
        if not ok:
            errors.append(message)
    def number(value: object, low: float, high: float = math.inf) -> bool:
        return type(value) in (int, float) and math.isfinite(value) and low <= value <= high
    for name, doc in [('catalog', catalog), ('definitions', definitions), ('knowledge', knowledge)]:
        if not isinstance(doc, dict):
            return [f'{name}: root must be an object']
        need(type(doc.get('schema_version')) is int and doc['schema_version'] == 1, f'{name}: unsupported schema_version')
    sets: dict[str, set[str]] = {}
    for key in ('professions', 'titles', 'skills', 'traits', 'knowledge_states'):
        values = catalog.get(key)
        if not isinstance(values, list) or not all(isinstance(v, str) and v for v in values):
            errors.append(f'catalog.{key}: expected nonempty string IDs')
            sets[key] = set()
        else:
            need(len(values) == len(set(values)), f'catalog.{key}: duplicate IDs')
            sets[key] = set(values)
    rows = definitions.get('employees')
    if not isinstance(rows, list):
        return errors + ['definitions.employees: expected array']
    employees: dict[str, dict] = {}
    allowed = {'id', 'name', 'age_years', 'profession_id', 'title_id', 'hire_cost', 'wage_per_service', 'skills', 'traits', 'private_goal'}
    for index, employee in enumerate(rows):
        loc = f'employees[{index}]'
        if not isinstance(employee, dict):
            errors.append(f'{loc}: expected object')
            continue
        need(set(employee) == allowed, f'{loc}: missing or unsupported fields')
        eid = employee.get('id')
        if not isinstance(eid, str) or not eid:
            errors.append(f'{loc}: invalid id')
            continue
        need(eid not in employees, f'{loc}: duplicate employee id {eid}')
        employees[eid] = employee
        need(isinstance(employee.get('name'), str) and bool(employee['name'].strip()), f'{eid}: missing name')
        need(type(employee.get('age_years')) is int and 18 <= employee['age_years'] <= 120, f'{eid}: fixture employee must be an adult aged 18-120')
        for field, enum in [('profession_id', 'professions'), ('title_id', 'titles')]:
            need(isinstance(employee.get(field), str) and employee[field] in sets[enum], f'{eid}: unknown {field}')
        for field in ('hire_cost', 'wage_per_service'):
            need(number(employee.get(field), 0), f'{eid}: {field} must be finite nonnegative number')
        skills = employee.get('skills')
        if not isinstance(skills, dict):
            errors.append(f'{eid}: skills must be an object')
        else:
            need(set(skills) == sets['skills'], f'{eid}: missing/unknown skill IDs')
            for skill, value in skills.items():
                need(number(value, 0, 100), f'{eid}.{skill}: skill must be finite in 0-100, not a boolean')
        traits = employee.get('traits')
        if not isinstance(traits, list) or not all(isinstance(t, str) for t in traits):
            errors.append(f'{eid}: invalid traits')
        else:
            need(len(traits) == len(set(traits)), f'{eid}: duplicate trait')
            need(set(traits) <= sets['traits'], f'{eid}: unknown trait')
        need(isinstance(employee.get('private_goal'), str) and bool(employee['private_goal']), f'{eid}: missing private_goal')
    profiles = knowledge.get('profiles')
    if not isinstance(profiles, list):
        return errors + ['knowledge.profiles: expected array']
    seen: set[str] = set()
    fields = {'title_id', 'profession_id', 'private_goal'} | {f'skills.{s}' for s in sets['skills']} | {f'traits.{t}' for t in sets['traits']}
    for index, profile in enumerate(profiles):
        if not isinstance(profile, dict):
            errors.append(f'profiles[{index}]: expected object')
            continue
        eid = profile.get('employee_id')
        if not isinstance(eid, str):
            errors.append(f'profiles[{index}]: invalid employee_id')
            continue
        need(eid in employees, f'profile {eid}: unknown employee')
        need(eid not in seen, f'profile {eid}: duplicate profile')
        seen.add(eid)
        need(set(profile) <= {'employee_id', 'observations', 'claims'}, f'profile {eid}: unapproved truth/private fields')
        observations = profile.get('observations')
        if not isinstance(observations, list):
            errors.append(f'{eid}: observations must be an array')
            observations = []
        seen_fields: set[str] = set()
        for observation in observations:
            if not isinstance(observation, dict):
                errors.append(f'{eid}: invalid observation')
                continue
            field, state = observation.get('field'), observation.get('state')
            valid_field = isinstance(field, str) and field in fields
            need(valid_field, f'{eid}: unknown observation field')
            need(isinstance(state, str) and state in sets['knowledge_states'], f'{eid}: invalid knowledge state')
            if isinstance(field, str):
                need(field not in seen_fields, f'{eid}: duplicate current observation {field}')
                seen_fields.add(field)
            need(bool(observation.get('source')) and isinstance(observation.get('source'), str), f'{eid}: observation source required')
            need(type(observation.get('at_tick')) is int and observation['at_tick'] >= 0, f'{eid}: invalid observation tick')
            need(set(observation) <= {'field', 'state', 'source', 'at_tick', 'value', 'range'}, f'{eid}: unapproved observation payload')
            if state == 'estimated':
                bounds = observation.get('range')
                ok = isinstance(bounds, list) and len(bounds) == 2 and all(number(v, 0, 100) for v in bounds)
                need(ok and bounds[0] <= bounds[1], f'{eid}: invalid estimate range')
                need(isinstance(field, str) and field.startswith('skills.'), f'{eid}: numeric estimate only for demo skills')
                need('value' not in observation, f'{eid}: estimate leaks exact value')
                # Estimates may be wrong; do not require actual skill inside the interval.
            elif state == 'verified':
                need('value' in observation and 'range' not in observation, f'{eid}: verified observation needs exact value only')
                if valid_field and eid in employees:
                    truth = employees[eid]
                    if field.startswith('skills.'):
                        actual = truth.get('skills', {}).get(field.split('.', 1)[1])
                    elif field.startswith('traits.'):
                        actual = field.split('.', 1)[1] in truth.get('traits', [])
                    else:
                        actual = truth.get(field)
                    value = observation.get('value')
                    need(type(value) is type(actual) and value == actual, f'{eid}.{field}: verified value disagrees with fixture truth')
            else:
                need('value' not in observation and 'range' not in observation, f'{eid}: hidden/suspected information must not carry truth')
        claims = profile.get('claims')
        if not isinstance(claims, list):
            errors.append(f'{eid}: claims must be array')
            claims = []
        for claim in claims:
            if not isinstance(claim, dict):
                errors.append(f'{eid}: invalid claim')
                continue
            need(isinstance(claim.get('field'), str) and claim['field'] in fields, f'{eid}: claim field unknown')
            need('claimed_value' in claim and claim.get('verification') == 'unverified', f'{eid}: demo claims need unverified claimed_value')
            need(isinstance(claim.get('source'), str) and bool(claim['source']), f'{eid}: claim source required')
            need(set(claim) <= {'field', 'claimed_value', 'verification', 'source'}, f'{eid}: claim contains truth fields')
    need(seen == set(employees), 'Every demo employee needs exactly one knowledge profile')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        folder = args.root / 'content' / 'employees'
        docs = [json.loads((folder / name).read_text(encoding='utf-8')) for name in ('catalog.json', 'definitions.json', 'knowledge.json')]
        errors = validate(*docs)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        errors = [f'Cannot validate content: {exc}']
    if errors:
        for error in errors:
            print(f'FAIL: {error}', file=sys.stderr)
        return 1
    print(f'PASS: {len(docs[1]["employees"])} employee definitions and knowledge profiles; runtime/UI not tested.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
