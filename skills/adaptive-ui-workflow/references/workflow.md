# Workflow

用于大型设计、Design System 和 Migration Assessment；局部控件无需全部执行。

## 只读项目与产品基线

记录实际 CURRENT UI STACK 与证据；查 UI/业务耦合和既有功能入口。截图、代码和产品行为一起解释，旧截图标时间/版本限制。确认用户、核心路径、密度、工作时长、高频操作、持续可见信息及配置/结果/状态/日志区域。只询问会改变设计或安全边界的未知信息，继续独立工作。

审计覆盖信息架构、视觉层级、布局/对齐/间距/密度、排版/色彩/对比、导航、组件、交互/反馈、Loading/Empty/Error、无障碍、一致性、扩展性和窗口/响应式行为。按 Critical（阻止任务、重要能力丢失）、Important（效率/可读性/一致性明显受损）、Polish（视觉细节）分级。每项含证据、用户影响和建议，不把所有问题都列严重。

## 设计方向与轻量 Design System

依据用途、用户、环境、信息密度、品牌与历史习惯选择方向，如 professional utility、dense analyst workspace、engineering workstation、creator workspace；说明适用理由。用户要求简约/深色/工业风/IDE 等时重新推导，不固定审美。避免没有产品理由的全卡片、超大圆角、渐变、玻璃、Hero、巨量留白和强阴影。专业工具优先可读、稳定、清楚、高效。

现有成熟系统优先补充/修复/扩展。仅定义实际用到的语义颜色与 Surface、字体层级、间距、Radius、Border/Shadow、图标、控件高度、组件 Variant 与状态；记录如何映射至当前 Theme/Token 文件。按钮/Input/Select/Tabs/Table/Tree/Panel/Dialog/Tooltip 按需覆盖。定义 Hover、Focus、Selected、Disabled、Loading、Empty、Error、Warning、Success 的相关表现，状态不只依靠颜色。按目标平台选择度量单位、字体及控件尺寸，Web 数值不直接套到桌面。

Design System 是一份决策；辅助 Skill 只补充当前问题，不各自产生独立系统。优先已有品牌与资源。字体、图标许可和离线可用性按具体资源检查，不因字体推荐擅自下载或加依赖。

## 实施顺序与功能保护

列受影响的 UI 文件、绑定和必须保持的行为；保留用户正在修改的内容。大型改造先选代表性 Pilot Screen，覆盖典型数据、长文本和异常状态，再推广 Token → 公共组件 → Shell → 导航 → 核心页面 → 次级页面/弹窗 → 反馈 → Polish。每步具有可运行结果及验证证据，不一次性重写整个应用。

接口问题先用 Adapter/ViewModel/Controller/UI Binding 解耦。若确需改业务接口，说明调用方、兼容路径和结果影响；不在仅授权 UI 的任务里更改算法、协议或数据定义。复用既有启动/构建链，新增依赖说明必要性及较小替代方案，避免无关 Refactor。

记录受影响的旧功能入口、输入输出和典型任务作为回归基线；验证按变化规模选择。动画、透明、Blur、Shadow、表格数据量和高频更新不能明显拖慢 UI。卡顿按 UI 线程阻塞/业务计算/渲染/IO 分析，不用“Python 慢”解释一切。

## Migration Assessment：独立于普通 redesign

仅明确迁移意图进入；只允许评估的请求不产生应用代码变化，也不创建 Prototype 文件。

先交付：Current Architecture、Migration Motivation、Expected Benefits、Migration Cost、Risk、Business Logic Reuse、UI Rewrite Scope、Packaging Impact、Deployment Impact、Maintainability 和 Prototype Plan。评估目标框架及宿主，React 不天然等于 Electron/Tauri。

当会话已明确授权迁移/Prototype 时，在项目约定的隔离位置做最小代表性 Prototype；保留原入口和可工作的 UI。先验证一个核心业务路径、接口复用、桌面能力、打包/分发、性能及视觉效果，再形成分阶段计划和回退边界。Prototype 结果不足先调整方案，不用现成模板或沉没成本为全量重写辩护。

“我允许从 Qt 换成 React”授权迁移方向，但仍需上述分析与隔离 Prototype；不能马上覆盖整个 Qt UI。已有全面实施授权且具体阶段经过验证时可以继续按计划推进。若只有评估或 Prototype 授权，完成该范围并交付可审阅成果，扩大范围前才需要新增授权。每次询问应指向具体未授权变更，不重复索取已有授权。

## 迁移授权的可观察判据

| 会话措辞 | 完成范围 |
|---|---|
| “评估是否该从 Qt 换成 React” | 评估和 Prototype 计划，只读，不写原型 |
| “我允许从 Qt 换成 React”或“先做迁移原型” | 分析、隔离原型和渐进计划；不立即替换完整应用；交付原型证据及下一阶段的具体范围 |
| “使用 React 重写并实现 UI 迁移”或“按已验证方案完成迁移” | 先评估与代表性原型验证，再自主逐步实施已授权范围；每阶段保持可运行/可回退结果，不重复请求已有权限 |

这些依据完整会话而非一句孤立措辞判断；“允许换技术栈”不能覆盖项目外的后端、协议或数据迁移。

期限紧时先保核心任务/功能兼容，再处理明显布局和状态问题，最后 Polish。验证失败只针对观察到的问题迭代；相同环境阻塞重复出现且没有新的可执行恢复办法时，交付已完成部分和未验证项，不扩大 redesign，也不宣称完成该项验证。
