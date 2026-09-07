# UI guidelines

## U1 Two complementary layers

Management: quiet, efficient, readable controls for staffing, priorities, stock and orders. Human-facing: paper/resume/personnel file with portrait, annotations and occasional stamps for significant decisions. They share typography, spacing, focus states and navigation. Do not copy the generated image's placeholder text, currencies, logo or dates as final interface requirements.

## U2 Signature resume

Candidate-supplied facts/claims in a main page; separate manager notes and verification sources; clear cost/action area. Show estimates as ranges or qualitative descriptions, unknown as information state rather than zero. Do not expose a hidden field in a tooltip, sorting value or debugging widget in player builds. Changes accumulate into personnel history. Discovery is not an excuse to hide salary/contract terms the player must accept.

## U3 Layout

Use reusable card, stat row, trait tag, price, tooltip and dialog components. Declare top HUD, world interaction region, side inspector, modal and notification zones. Container/anchor-driven layout; world clicks must not pass through UI. Modals are dismissible and keyboard focus clear. Confirm irreversible employee actions but do not animate every click slowly.

## U4 Test and evidence

Test 1280x720 and 1920x1080, long names/text, missing portraits, zero funds, no selection and candidate with sparse knowledge. Use explicit empty/loading/disabled/error states. Readability cannot depend on color alone. Required typography must use valid licenses; this repo does not bundle fonts by default.

UI/Art reviewer reports overlaps, clipped text, hidden actions and hierarchy issues before calling a screen acceptable. A screenshot proves rendering, not every interaction: pair with functional checks. Benchmark approval is not final UI approval.
