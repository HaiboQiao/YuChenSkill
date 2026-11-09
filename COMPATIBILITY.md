# Codex 与 OpenCode 兼容性

## 文件格式

9 个技能均采用目录内 SKILL.md，名称使用与目录一致的唯一小写连字符 ID。scripts、references、assets、data 必须随技能目录整体复制。OpenCode 支持全局 `~/.agents/skills/`，也支持自身的技能目录。不同版本的发现与元数据规则有差异，统一名称可兼顾较严格的版本。[OpenCode Skills](https://opencode.ai/docs/skills)、[OpenCode 1 Agent Skills](https://docs.opencode.ai/docs/skills/)

## 工具与行为

| 分类 | 技能 | 已检查情况 |
|---|---|---|
| 文本工作流 | mew-spec、guided-learning-tutor、frontend-ui-standards | 无专属运行时要求，实际表现受模型与上下文影响 |
| UI 协同 | adaptive-ui-workflow、frontend-design-codex | 可协调其他技能，GUI 与浏览器证据需要客户端实际工具 |
| 本地检索 | ui-ux-pro-max | Python 标准库为主，数据完整性与检索已本地验证 |
| 外部文档 | context7-mcp | 需要另接 Context7，本次会话无可调用 MCP，未测试真实查询 |
| 技能测试方法 | writing-skills | 已移除缺失的 Superpowers 必需文件引用，保留现有详细测试说明 |
| 技能创建评测 | anthropic-skill-creator | 入口 ID 已统一，自动评测后端继续使用 Claude Code |

独立会话工具的名称和统计字段随客户端变化。缺少隔离评测能力时采用披露限制的人工用例，不报告未执行的定量结果。技能文件不会随复制自动安装 MCP、登录账号、图像工具或浏览器。

## 验证层级

此次完成本地静态检查、Python 语法检查、名称与清单校验、设计数据校验、检索冒烟检查，以及预览器注入修复与端口占用回归检查。另一台电脑的 OpenCode 自动发现、模型触发、MCP 查询和 Claude Code 评测尚待实际环境验证。
