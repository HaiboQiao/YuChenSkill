# Stack Routing

仅在需要选实现技术/辅助 Skill/验证途径时读取。先基于源代码与启动配置确定实际运行的 UI；混合项目逐个界面路由。宿主、语言和 UI Framework 是不同字段。

## Framework 路由

| 当前 UI | 保持的实现方式 | 辅助能力 | 真实验证重点 |
|---|---|---|---|
| Python PyQt/PySide 或 C++ Qt Widgets | 现有 Layout、Size Policy、QSS/QPalette、Custom Widgets、信号/槽 | Pro Max 通用 UX；standards 的 Token/复用原则 | 实际窗口、resize、DPI/缩放、焦点、键盘、状态和信号行为 |
| Qt Quick / QML | 现有 QML 组件、Theme、Layout/Anchors、Binding | Pro Max 通用 UX；standards 原则 | 真正的 QML 窗口、绑定/状态、窗口缩放与高频更新 |
| React / Vue / HTML-CSS / 其他 Web | 已有组件、路由、CSS/主题和构建链 | Pro Max + frontend-design-codex；Token/一致性时 standards | 浏览器实际渲染、目标视口、键盘、响应式、溢出、console |
| Electron / Tauri + Web frontend | Web 前端保持当前框架；桌面 Shell 保持现有架构 | Web 路由能力，只作用于前端 | 浏览器 QA + 实际桌面宿主；权限、文件选择、窗口/IPC 行为 |
| Flutter / 原生移动 / 其他桌面 | 现有框架 Theme、组件和平台布局机制 | Pro Max 有匹配时查该 stack；standards 原则 | 实际设备/模拟器/桌面，目标平台字体缩放、触控或键盘 |
| 未确定或未支持的框架 | 先读入口、manifest 和项目文档确认 | 通用 UX；没有匹配时明确降级 | 确认启动和观测能力，不默认 React/HTML |

## 辅助 Skill 的责任

- **ui-ux-pro-max**：设计方向、配色、排版、交互、导航、无障碍和 UX Audit。小问题用单一 `--domain` 查询，大型方向才 `--design-system`。数据结果是参考，不是项目架构或写代码授权；保留用户已有 Design System。生成器可能给出 Landing Page、Web 字体或动画片段，必须按产品和平台筛选。
- **frontend-design-codex**：仅 browser-rendered UI 的实现和真实浏览器 QA。Qt Widgets、QML、原生 Flutter 不调用它来实现；Flutter Web 或真实内嵌 Web 区域可按对应子界面调用。先继承已选的设计方案，不再生成竞争方案。
- **frontend-ui-standards**：Implementation/Review 中的语义 Token、组件复用、组件/页面参数、一致性和 UI 代码检查。Qt 中把 CSS/React 示例原则翻译为已有 Theme/QSS/QPalette 或 QML 单例，不引入 Web 依赖。Audit 只在确实涉及样式代码一致性时按需读取。

从当前会话技能目录获取入口的实际绝对路径。没有被列出时，只在当前用户技能根查找所需名称的 SKILL.md；无需扫描其他业务项目或敏感目录。辅助技能缺失时报告缺项并按本 Skill 的通用流程继续，不自动安装软件。不能说调用了未读取的 Skill 或查询了没有结果的数据。

Pro Max 的搜索入口在其自身 `scripts/search.py`：从技能目录解析绝对路径，使用已有 Python 3，查询仅含通用产品/平台词。未运行时不伪造搜索结果。Qt 不在已部署数据库的 `--stack` 列表：查 `ux/style/color/typography` 等通用域，再查当前 Qt 文档；不得用 `html-tailwind` 代替 Qt。无匹配最多按其查询规范重试，随后标明一般指导的降级来源。

对于 API 语法、框架配置和版本差异，使用现有 Context7：先 resolve-library-id，再按单一概念 query-docs，选择实际版本；无法得到匹配文档则用官方来源并说明。对通用设计判断或业务逻辑分析，不必查询所有框架。辅助数据不是当前 API 文档。

## 验证能力选择

优先使用已提供的浏览器、GUI、截图或项目现有测试能力，先确认工具确实可用。Web 选实际视口；桌面按支持的最小/默认窗口和目标 DPI 测试，不强制增加移动页面。Electron/Tauri 的浏览器截图不能代替宿主验证。原生 UI 若能运行 GUI 并观察必须尽可能验证；离屏渲染截图只证明对应渲染结果，不证明原生输入/文件对话框都已验证。

工具缺失时不安装未知截图运行时；完成不依赖它的工作，交付缺失证据，并可请用户后续提供截图继续迭代。
