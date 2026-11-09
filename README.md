# YuChenSkill

个人常用的 9 个 Agent Skills，整理为可通过 GitHub 同步的完整目录。目标环境为 Codex 和 OpenCode，包含入口、参考文档、脚本、设计数据及已有许可证。

本仓库是个人安装目录的发布副本。首次整理日期为 2026-11-09。技能来源与适配见 THIRD_PARTY_NOTICES.md，静态审查和验证边界见 SECURITY.md。

## 技能目录

| 技能 | 使用场景 | 依赖与边界 |
|---|---|---|
| mew-spec | 需求澄清、规格、计划、任务与验收 | 默认逐阶段批准，用户可明确连续授权 |
| adaptive-ui-workflow | UI 分析、设计、实现、审查总控 | 按实际框架路由辅助 UI 技能 |
| frontend-design-codex | Web、Electron、Tauri 前端设计 | 视觉验证需要浏览器或项目截图工具 |
| frontend-ui-standards | 设计变量、组件、布局一致性 | 按目标平台应用规则 |
| ui-ux-pro-max | 设计风格、色彩、字体、图表与技术栈检索 | Python 3，完整 scripts 和 data 目录 |
| guided-learning-tutor | 教学、理解修复、练习与提示 | 核心流程无工具依赖 |
| context7-mcp | 查询库和框架的当前文档 | 目标客户端另配 Context7 MCP |
| writing-skills | 用基线与压力场景改进技能 | 独立会话有助于有效评测，Graphviz 渲染可选 |
| anthropic-skill-creator | 技能编写、评测和描述优化 | 部分自动评测脚本仍需 Claude Code |

## 安装与使用

完整步骤见 [INSTALL.md](INSTALL.md)。Codex 和 OpenCode 可共用 `~/.agents/skills/`，每个技能保留完整子目录。仅克隆仓库到任意目录，通常不会让客户端自动发现其中的 skills。

在仓库根目录运行以下 Python 命令可先核对目录与语法。

```sh
python scripts/verify_bundle.py
```

向 agent 提出正常任务即可按描述触发技能，也可明确写“请使用 mew-spec”或“请使用 guided-learning-tutor”。涉及 MCP、截图和独立 agent 会话时，以客户端实际暴露的工具为准。

## 维护

更新前先保存另一台电脑上的本地改动，拉取仓库后重新复制选定目录。仅首次安装可使用 INSTALL.md 的无覆盖复制示例。修改后运行验证器，检查 SECURITY.md 和 CHANGELOG.md 中的记录，再正常提交并推送。仓库内 manifest.json 记录此次发布文件的 SHA-256，修改技能后需同步更新清单。.gitattributes 保留文件字节，避免 Windows 自动换行转换使清单失配。

兼容性详情见 [COMPATIBILITY.md](COMPATIBILITY.md)，审查结果见 [SECURITY.md](SECURITY.md)。首次范围与验收记录位于 docs/maintenance/。
