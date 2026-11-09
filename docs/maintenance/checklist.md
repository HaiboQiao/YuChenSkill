# 验收记录

- [x] 9 个技能入口与目录 ID 一致。
- [x] 保留支持资源、已有许可证和来源证据。
- [x] 补齐中文安装、兼容性、安全与来源说明。
- [x] 运行目录、清单、语法与本地功能验证。

验证命令为 verify_bundle.py、validate_data.py、search.py、quick_validate.py 与 node --check。针对预览器的临时回归验证通过，详情见 SECURITY.md。
- [x] 提交、推送并核对远端提交。

首次发布提交为 2059d26e2d790bee27e787cac6c5673839b296c2，已通过 ls-remote 确认 GitHub main 指向该提交。重新从 GitHub 克隆后运行 verify_bundle.py，9 个入口、106 个文件哈希及 Python 语法均通过。随后仅补充本验收记录。
- [ ] 目标 OpenCode 环境真实触发验证，当前环境未执行。
