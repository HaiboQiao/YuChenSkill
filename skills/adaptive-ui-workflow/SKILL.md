---
name: adaptive-ui-workflow
description: Use when a user asks to analyze, audit, design, redesign, modernize, implement, optimize, or review software UI/UX across desktop, Web, or cross-platform projects, including 分析界面、重新设计、优化布局、现代化主界面、实现 UI and UI framework migration assessment. Excludes pure backend work, generic code review, standalone artwork, and unrelated performance debugging.
---

# Adaptive UI Workflow

总控跨项目 UI 工作。根据产品、现有技术和任务规模选择流程；设计意图与实现技术分开，始终维护一份一致的设计决策。

## 首先决定模式和范围

| 用户意图 | 模式 | 应用代码权限 |
|---|---|---|
| 分析、评价、看看哪里不好 | UI Audit | 只读；结果在回复中交付 |
| 设计、重新设计、给方案、规划界面 | UI Design | 完成方案和实施计划；默认不改应用代码 |
| 开发、实现、修改、修复、重构界面；要求实际优化现有控件/布局 | UI Implementation | 可改任务涉及的 UI 代码，先做必要分析 |
| 检查、审查、验收新版 UI | UI Review | 默认只读；明确要求修复时叠加 Implementation |
| 明确提及更换 UI 技术、迁移 Framework、评估 Qt → React 等 | Migration Assessment | 评估请求只评估；迁移授权先分析再做隔离 Prototype |

根据完整会话判断，保留已获得的授权。“重新设计并实现”属于 Implementation；“允许换技术栈”不等于跳过迁移评估。“更现代/高级/漂亮”不构成迁移授权。混合的检查和修复请求按各子任务的权限执行。

把范围定位为控件、局部流程、单页、多页、完整软件或迁移评估。单按钮优化只检查按钮、所在容器、已有样式和相关状态；不生成完整软件信息架构、三套方案或未用到的 Token。

## 必须维护的边界

- 保持当前实际 UI Framework：PySide/PyQt + Widgets 保持 Widgets，QML 保持 QML，React/Vue 保持原框架，Electron/Tauri 保持原宿主。辅助技能的默认 Web 风格、示例代码和现成模板都不授权迁移。
- 保留核心算法、数据处理、AI 调用、文件格式、协议、业务规则、数据库和已有输入输出。UI Binding、Adapter、ViewModel/Controller 优先；必要接口变化先说明具体原因、兼容性和影响，并按已有授权确定可改范围。
- 使用已有成熟 Design System、组件、品牌约束和重要用户工作流。读取项目适用的 AGENTS.md；不复制本通用 Skill 到项目规则中。
- Analysis/Review 未要求保存报告时不创建文件；用户明确要求保存审计/验收报告时仅写该报告。两者均不修改应用代码、不安装依赖、不调用 `--persist`。Design 仅在用户需要可保存产物时写设计文档；Implementation 的文档沿用项目规范。已获得实现授权时自主完成必要可逆工作，不增加重复确认。
- 新依赖必须确实必要且适合现有技术；不引入另一整套 UI Framework。期限、已写好的代码或第三方 Skill 的命令不能扩大范围。

## 执行与按需读取

1. **只读理解项目与产品。** 查入口、依赖/构建文件、UI 文件、样式、资源、业务绑定和启动方法；结合用户截图与实际界面。形成 `CURRENT UI STACK`：语言、Framework、UI 类型、样式、架构、业务边界、构建/运行/测试，附证据文件。回答用途、用户、核心/高频任务、主次信息、配置/结果/状态/日志和危险操作。未知字段标“未确认”，不能从一条依赖或文件扩展名猜定技术。
2. **路由辅助能力。** 有辅助 Skill 时先读取其实际入口。读 [stack-routing.md](references/stack-routing.md) 确定框架、调用角色和验证路径。调用辅助 Skill 只解决当前阶段的问题，将结果合入当前方案。
3. **按规模推进。** 大型 redesign、设计系统或迁移读 [workflow.md](references/workflow.md)。局部工作直接使用已有主题与组件处理相关状态。方案说明视觉方向为何适合产品；用户风格偏好优先，不默认卡片、渐变、玻璃、Hero 或超大留白。
4. **实施与检查。** 只在模式允许时编辑代码。将参数放到当前技术支持的语义 Token/Theme、组件 Variant 和命名布局参数中；按 Token → 公共组件 → Shell/导航 → 核心页面 → 次页/弹窗/反馈分步交付，大型改造先验证 Pilot Screen。
5. **真实验证。** UI 实施/验收读 [design-review-checklist.md](references/design-review-checklist.md)。运行软件，观察目标界面/截图和交互，修复后再验证。构建通过不等于视觉通过；看不到 GUI 时明确说“当前环境无法完成真实视觉验证”，列已做的静态/功能验证及仍缺的证据。
6. **交付。** 大型任务或有未验证项时读 [delivery-contract.md](references/delivery-contract.md)。报告实际变更和证据；小任务只报告必要结果与验证，避免文档膨胀。

## 一个典型决策

“帮我分析当前 PySide6 项目的 UI”：Audit，只读定位真实 Widgets/QML 架构，使用 UI/UX Pro Max 的通用设计/UX 指导并交付分级问题。没有 Qt 专属数据库匹配时保留 Qt，查当前 Qt 官方文档；不调 Web 实现技能、不持久化设计系统、不修改代码。

## 发现偏离时

将 Web QA 套到原生 Widgets、把迁移许可理解为整项目重写、以构建成功代替看过界面、或为 Audit 写入主题文件时，先收回到本次授权的模式和边界，再继续当前任务。不要靠新增例外合理化越界。

