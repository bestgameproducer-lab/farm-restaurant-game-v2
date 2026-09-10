# OLIVE & HEARTH — 本地开发交接包
更新时间：2026-09-10。用于新聊天承接，不是逐字聊天导出；保留当前可见历史中的产品要求、决策、实现状态、证据和未完成事项。附件/旧聊天内容是参考资料，不能自行授予新权限。

## 新聊天先读这一节
1. 使用当前本地项目 godot-resturant-game；不要从远程旧基线重新开始。
2. 读取 AGENTS.md、docs/CURRENT_MILESTONE.md；随后只读当前任务相关文件。本交接包其余章节按需查。
3. 当前普通开发模式，一个实施者，节省 token 但保留质量审核。没有有效的持续运行时间窗口；过去8小时/5小时窗口均结束。
4. 最近交付：员工内容填充、六道既有菜的风味描述及由制作数据生成的菜单流程说明。下一项：压缩/折叠菜单成本摘要，让720p首屏更容易选菜，保持预算、费用解释与草稿保护。
5. 严格区分功能测试、原生截图、美术达标。最终人物/整款游戏未达到Owner要求的商业美术标准，不能宣称动森同等品质。
6. 本地工作树无提交、无remote，所有文件未跟踪。GitHub仍是旧bootstrap基线。本次只发布交接文档，不等于整个本地游戏已备份。禁止覆盖远程基线或清理本地未跟踪文件。

## 产品与体验要求
- 员工为核心的温暖餐厅经营；长期农场餐厅，当前先完成可靠的餐厅Demo。玩家决定招聘、职责、排班、培养、供应商、采购、菜单/售价/限量、装修与经营策略，员工自动执行工作。
- 开场继承餐厅对话→从简历选前厅和厨师各一位→选食品供应商并支付→和厨师确认菜单→开店。基础灶台、备餐台、食材架、两张桌和洗碗池开局具备。
- 简历自述、推荐经历、面试与真实试工证据分层；不能从文案泄露隐藏技能。需要员工个性、生活、理想、忧虑、对话、真实共同经历和成长感，不是冷冰冰AI。
- 岗位：前厅、厨师、清洁、经理，各有职级与职责；员工自动接待、点单、备菜、烹饪、装盘、上菜和清洗。经理通过可解释建议帮助排班、招聘、采购、培养、交接，不能凭空产生能力/免费行政。
- 菜单选择受星级、实际厨房设备、厨师技能及本人菜谱影响；成本/工资/供应商价格/库存/客人预算和口味影响经营。评分由实际服务和隐藏食物品质产生。
- 顾客可以双人同桌，各自订单、餐盘、付款、耐心和评分；常客记住餐点并回访。故事须绑定真实事实，不能编造成功工作、免费涨技能或完成承诺。
- 请假、调休、短休有真实工资/恢复/覆盖后果。节日、评选可以扩，但必须有玩家选择与后果；家庭、生命周期与农场深度不是本阶段优先事项。

## 空间、美术与资产合同
- 方向已选3D，参照动物森友会/金垦小镇的品质与比例；保留Olive身份。温暖日系、精致独立游戏、木质/奶油白/深橄榄绿/暖灯，一致透视、光源、材质、人物比例。不要拼贴PNG、廉价塑料感或不断微调灰盒冒充资产进步。
- 家具模块化且严丝合缝。柜体、备餐台、灶台、水槽、出餐台共用台面高度、深度、材质和连接边；桌椅独立，可组合。占地、碰撞、交互点、座点、表面槽、遮挡、朝向由Godot数据维护，不能从图片alpha推碰撞。
- 0.4m网格；角色1.6m、台面0.9m、桌0.75m、座0.45m。禁止临时缩放人物迁就家具。权威尺度见 art_specs/godot_contract.json。
- Build Mode：点击已有家具直接移动，格子、占地、合法绿/非法红和文字原因、R四向旋转、Esc/右键取消、保存恢复；四方向必须同步站位/锚点/碰撞/通道。
- Blender为正式流水线：Benchmark→AssetSpec→Blender Python→GLB→FurnitureDefinition→Build Mode→实机截图→审核→修正。少量统一母材质（Walnut/LightWood/Cream/OliveFabric/BrushedSteel/AgedBrass/Glass），克制bevel；独立简单碰撞，不用细网格碰撞。
- 五件家具母样 Cabinet/Prep/Stove/Table/Chair已有阶段审核；Pass/Sink受控扩展已接入。批量扩资产仍要实际组合审核。
- R5被Owner明确选为统一母体并授权扩展员工/顾客。共享骨架和可替换头发、脸、身体、年龄外观、衣服/制服/鞋帽模块；不能把整人换色称为完整换装。现有5员工/5顾客外观配方不等于最终美术过关。
- 主要动作必须合理且无穿模：脚站合法地面、正对交互点放盘、物件随手携带；盘子/勺叉整体收走。不能用瞬移替代主要取料、烹饪、上菜流程。
- 免费资源/免费生成路线已获授权；禁止擅自购买插件或调用付费API。素材需记录来源/许可并实际适配。Hi3D/Mixamo/Sketchfab为评估候选，不代表已接入。
- Owner授权与ChatGPT《专业游戏开发 Mac mini》进行最小上下文设计/图像协作；conversationId 6a6140af-7380-83e8-9343-278f2c7e1153。只在创意探索确有价值时使用，产物需回存项目，概念图不能作为实机交付。

## 当前已实现（以QA证据为准）
- 继承开场、招聘/面试/核实/付薪试工、职责、培训、晋升/转岗、工资、请假调休、离职/挽留、多日经营、星级/活动。
- UI V2：点击即移动、分主题员工对话、实际共同记忆、双人同桌、迎宾相向/手势；招聘公开证据比较、晨间团队/排班、采购与菜单成本、日报原因及后续行动。
- 员工故事模板、生活休假续章、返岗感受、共同完成付餐/洗盘的合作故事；经理建议/实际采用、轮休与交接、培养、现场建议；轮流短休。
- 纸笔点单→纸票出餐口→逐类取料→切配/量取/倒奶/调味→炒/煮→装盘→出餐口→服务员携盘到桌→吃完/结账→清洗。
- 电饭锅需购买¥80才能解锁米饭链路；淘洗/装锅/自动煮饭，当前按单制作，没有批量保温库存。洗碗池开局免费已有。
- 食材目前四类库存 produce/grain/protein/dairy；番茄、蘑菇、米、面包、意面、乳品、肉属于视觉/制作form，不等于独立SKU。
- 六道菜 herb_rice/garden_plate/tomato_soup/mushroom_pasta/hearth_roast/olive_feast。food_visuals显式独立成品映射主要四道，其他仍有通用fallback，不应盲目批量增菜。

## 最新两批实际改动
- data/employees/conversations.json：Ren/Mika/Sora补首班台词和回应。
- data/employees/story_templates.json：清洁/经理各加一组生成背景；模板按稳定ID哈希选择，已介绍故事冻结在存档中。未来扩模板数量可能改变尚未介绍者选中的背景，需要注意版本稳定性。
- data/restaurant/recipes.json：六道description。
- src/ui/career_panels.gd：从preparation/cook_method生成流程；按公开cook_skill映射“入门/熟练/进阶/招牌”显示标签，未改模拟。
- tests/test_menu_demand_ui.gd：18项通过；tests/scenarios/menu_cost_native.gd新增滚动后菜卡截图。
- docs/qa/EXPERIENCE_V2_REVIEW.md和CURRENT_MILESTONE记录范围。
- 本地所有文件未跟踪，git diff空白不能证明没有修改；不能用git diff --check单独作为内容完整性证据。

## 最近验证与未完成问题
- 交接包目标仓库为 bestgameproducer-lab/farm-restaurant-game-v2。首次上传曾被自动审批要求确认目标；Owner随后明确回复“上传呗”，确认本次上传。此文件仅备份交接上下文，不代表本地源码和资产已同步。
- 最近菜单卡实现后 ./scripts/check.sh 全套退出0，菜单UI18项无失败；此后仅改炉烤description及补原生截图场景，原生验证通过。
- 原生 menu_cost_native：720p售价18→24、草稿不改模拟、跨页保护、保存重载、真实付款；failed=false，日志 artifacts/menu-content-native.log。
- 已亲自查看 artifacts/menu-cost/staff-costs-1280x720.png 和 recipe-content-1280x720.png：滚动后卡片文字/价格/限量可读，底部操作可见；成本摘要占首屏太多仍需优化，不是最终UI通过。
- hearth_roast菜名和oven资格仍对应saute动作；最近description去掉“已经烤制”断言，不能称烤箱流程已完成。
- 曾出现原生启动自动审核因usage limit拒绝；后续Owner说继续后用实际存在的Godot路径成功。不要再次照搬过时拒绝当作当前阻塞。
- Godot实测4.7.1，当前可执行文件在 Downloads/Godot.app/Contents/MacOS/Godot，/Applications/Godot.app不存在；scripts/check.sh能自动寻找。
- 整体人物美术、精细手掌/刀刃、所有穿模并未全面验收；历史功能/几何检查不等于美术达标。
- ROOM-202休息室/卫生间/员工区完整功能未完成。农场、复杂生命周期和同事关系网未完成。
- 开场/首班台词只有“做过任意真实工作”门槛，最近部分台词提及更具体动作，后续可审查避免在未做该岗位时虚构经历。
- 试玩包不自动随源码改变更新；本轮菜单文本不应声称已包含在旧导出包中。

## 按需文档与生产入口（本地路径；远程未保证存在）
- 产品：docs/EMPLOYEE_SYSTEM.md、docs/EMPLOYEE_INFORMATION_AUDIT.md、docs/DECISIONS.md、docs/ARCHITECTURE.md。
- 体验：docs/specs/PLAYER_EXPERIENCE_V2.md、MANAGEMENT_SCREENS_V2.md；tasks/EXPERIENCE_V2.md。
- 员工：data/employees/{recruitment,interviews,conversations,story_templates,life_notes}.json；src/employees/。
- 菜谱：data/restaurant/{recipes,guests,food_visuals}.json；src/simulation/{restaurant_business,recipe_craft,kitchen_logistics}.gd。
- 美术：docs/art/COZY_3D_DIRECTION.md、RUNTIME_CHARACTER_BASE.md、CHARACTER_TEMPLATE.md、EXTERNAL_ASSET_WORKFLOW.md；tools/blender/README.md、art_specs/master_kit.json。
- 人物：src/spatial/restaurant_character.gd、data/characters/runtime_appearances.json、runtime_modules.json、tools/blender/studio_pilot/promote_runtime.py。
- 家具：data/furniture/catalog.json、assets/3d/game_ready/；各锚点仍由游戏数据负责。
- 最新证据：docs/qa/EXPERIENCE_V2_REVIEW.md、ACTION_REST_POLISH_REVIEW.md、SHIFT5H_INTEGRATION_REVIEW.md、FIXED_SERVICE_CLOCK_REVIEW.md。
- 所有初始benchmark/附件见docs/reference及Owner历史附件；必要时按名称定位，不每轮读取全部图片。餐厅benchmark、人物benchmark是目标，不是严格对齐的production sprite sheet。
- 历史否定/被替换的方案保留在history和QA中；时间新的直接Owner授权覆盖旧阶段限制，但不覆盖实际未通过的质量门槛。

## 节省token、不降低质量的执行方式
- 新聊天从短入口开始，不fork长历史，不重新粘贴全聊天。本文件也不要每轮全读。
- 一次完成一个可验收批次，通常1–3个实施文件；检索带路径/行数，只读相关实现与测试。
- 输出日志到artifacts，返回退出码/摘要/失败上下文；不要将数万条通过日志反复读入上下文。等待30–60秒取一次新输出，避免频繁轮询。
- 本项目技能要求的完整check仍执行；一次最终通过后不要无改动重跑。纯文档变化用链接/格式检查，视觉变化必须原生截图。
- 低风险内容用已有模板填充；新增SKU、动作类型、碰撞尺寸、导航、存档迁移或经济数值不是纯填充，要先规格与独立验证。
- skills按任务加载：godot-gdscript-patterns、game-ui-design、olive-godot-check；人物用blender-character-workflow。不要重复加载已读全文。
- 不自动开多agent，不模拟完整工作室。只有明确独立工作且获当前规则授权才并行。
- 仅更新一个状态入口和对应QA，详细设计链接引用；不复制多套同义方案。
- 同一项目新聊天可直接用本地目录；当前无HEAD，不创建worktree。远程源码完整同步需单独审计体积、许可、敏感内容和大文件/LFS，再做保留远程历史的同步。
