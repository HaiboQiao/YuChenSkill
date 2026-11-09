# 来源与许可证

本仓库按目录保留已有许可证。根目录采用来源说明，未对全部内容授予新的统一许可证。

| 目录 | 来源证据 | 许可证情况 |
|---|---|---|
| frontend-design-codex | SOURCE.json 记录 dachent/skills 与提交 | 保留 MIT LICENSE |
| frontend-ui-standards | SOURCE.json 记录 MaxHan7/frontend-ui-standards-skill 与提交 | 保留 MIT LICENSE |
| ui-ux-pro-max | SOURCE.json 记录 nextlevelbuilder/ui-ux-pro-max-skill 与提交 | 保留 MIT LICENSE 与数据来源、字体许可元数据 |
| anthropic-skill-creator | 本地安装副本，携带 Anthropic skill-creator 内容与 LICENSE.txt | 保留 Apache-2.0 文本，原始提交未记录 |
| writing-skills | 内容指向 obra/superpowers，原始提交未记录 | 补入上游 MIT LICENSE，版权 Jesse Vincent |
| guided-learning-tutor | 本地 README 记录启发来源和原创整理说明 | 本地未附独立许可证，保留原说明，后续复用需确认授权 |
| adaptive-ui-workflow | 本地个人安装副本 | 本地未附独立许可证，来源与授权待维护者补全 |
| mew-spec | 本地个人安装副本 | 本地未附独立许可证，来源与授权待维护者补全 |
| context7-mcp | 本地个人安装副本 | 本地未附独立许可证，来源与授权待维护者补全 |

“个人安装”描述文件存放位置。原始作者、授权与使用频率分别需要对应记录证明。此次用户已授权将指定副本上传至个人仓库，未据此给来源不明的文件补写开源授权。

writing-skills 许可证于 2026-11-09 从上游公开地址取得，未证明当前本地副本逐字对应某一上游提交。[Superpowers LICENSE](https://github.com/obra/superpowers/blob/master/LICENSE)

## 本次发布适配

- Anthropic 入口改名为 anthropic-skill-creator，补充 Claude Code 依赖与执行边界。
- writing-skills 移除缺失的相邻技能文件硬依赖，内联 RED-GREEN-REFACTOR 基础并保留现有测试参考。
- 两个 UI 技能的工具定位措辞改为当前 agent 可用能力。
- Anthropic 预览器移除自动杀端口进程，转义嵌入 JSON，隔离表格 HTML 预览，限制反馈请求来源和大小。

这些修改仅作用于发布副本，具体文件差异和 SHA-256 记录在 manifest.json。第三方原有版权声明继续适用。

- Anthropic Python 文件读写显式使用 UTF-8，修复 Windows 默认 GBK 下的读取失败。
