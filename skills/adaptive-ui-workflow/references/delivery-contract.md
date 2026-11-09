# Delivery Contract

大型 UI 任务交付应让用户知道具体结果、范围与证据，按以下字段组织成简明说明；无需机械复制英文标题或写大量文件。

| 字段 | 内容 |
|---|---|
| Current Stack | 实际语言、Framework/UI 类型、样式/Theme；未确认字段和证据 |
| UI Goal | 核心用户任务与本次范围/模式 |
| Chosen Direction | 视觉和交互方向及适合产品的原因 |
| Main Problems Found | 分级问题、截图/代码证据与影响 |
| Design Decisions | 信息结构、主要流程、Token/组件/状态与历史兼容选择 |
| Files Changed | 实际文件链接与作用；只读任务说明应用代码无变化 |
| Verification Performed | 真实运行/截图/交互、尺寸/数据状态、功能与构建结果分别列；静态推断标明 |
| Remaining Issues | 未执行的验证、未解决问题、原因、后续具体动作 |
| What Was Intentionally Not Changed | 保留的业务行为、技术栈、用户流程及范围边界；只陈述对本次交付有意义的项 |

Audit 交付问题及建议；Design 交付具体可实施方案；Implementation 交付已改代码与验证；Review 交付发现与证据；Migration Assessment 交付评估及 Prototype/计划的实际完成范围。小任务用短说明，不强制全套文档。

只在需要长期记录且属于授权产物时，沿用项目 docs/design/architecture 等已有位置保存 Audit、Design Brief、Design System 或 Implementation Plan。不同辅助 Skill 共用一份方案，通用技能留在用户级安装目录；项目 AGENTS.md 只写品牌、尺寸、兼容性或禁止修改区域等特有规则。

明确说明辅助技能不可用或数据未匹配的降级、GUI 无法观察等局限。没有截图/观察证据时禁止声称视觉验收成功；不能只回复“已经优化完成”。
