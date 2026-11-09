# 安装与同步

## 准备

需要 Git。使用设计检索与验证脚本时需要 Python 3.10 或更高版本。Context7、截图工具和 Claude Code 按需单独配置。先核对本机现有技能，避免同 ID 的不同副本产生覆盖。

```sh
git clone https://github.com/HaiboQiao/YuChenSkill.git
cd YuChenSkill
python scripts/verify_bundle.py
```

## Windows PowerShell 首次安装

在克隆仓库的根目录运行。存在同名目标时逐个跳过，不覆盖已有技能。

```powershell
$skillDestination = Join-Path $HOME '.agents/skills'
New-Item -ItemType Directory -Force -Path $skillDestination | Out-Null
Get-ChildItem -LiteralPath './skills' -Directory | ForEach-Object {
    $target = Join-Path $skillDestination $_.Name
    if (Test-Path -LiteralPath $target) {
        Write-Warning "已存在，跳过 $target"
    } else {
        Copy-Item -LiteralPath $_.FullName -Destination $target -Recurse
    }
}
```

## macOS / Linux 首次安装

在仓库根目录使用 Bash 运行。

```bash
mkdir -p "$HOME/.agents/skills"
for source in skills/*; do
  target="$HOME/.agents/skills/$(basename "$source")"
  if [ -e "$target" ]; then
    printf '已存在，跳过 %s\n' "$target"
  else
    cp -R "$source" "$target"
  fi
done
```

## OpenCode 专用目录

也可将目标改为 `~/.config/opencode/skills/`，或在单个项目中使用 `.opencode/skills/`。为避免同 ID 的技能覆盖，只选择一个安装位置。另一台电脑的 OpenCode 版本尚未实测，首次安装后新建会话，检查技能发现情况。

## 可选依赖

- UI 检索使用 `python skills/ui-ux-pro-max/scripts/search.py "desktop productivity" --design-system`，默认读取本地数据。只有显式指定 `--persist` 才生成设计文件。
- 数据核对使用 `python skills/ui-ux-pro-max/scripts/validate_data.py`。
- Context7 skill 提供调用顺序。按当前 Context7 官方指引在目标客户端配置 MCP，并确认 `resolve-library-id` 与 `query-docs` 可用。MCP 的凭证保留在目标机器。
- Anthropic 评测工具的基本校验使用 PyYAML，可在独立虚拟环境运行 `python -m pip install PyYAML`。`run_eval.py`、`run_loop.py`、`improve_description.py` 仍调用 `claude`，需要 Claude Code 已安装且登录，并可能产生费用。
- `writing-skills/render-graphs.js` 需要 Node.js 和 Graphviz。它只在手动调用时运行。

## 更新

保存已安装副本的本地改动，运行 `git pull --ff-only`，验证仓库后对比并更新选定技能目录。复制安装不会自动同步，删除上游文件时也需要手动核对本地旧文件。更新后新建客户端会话。

## 排错

技能未出现时，检查目录层级是否为 `<技能根目录>/<技能 ID>/SKILL.md`，名称是否唯一，客户端技能权限是否允许，以及所需 MCP 是否连接。`agents/openai.yaml` 是保留的 Codex 元数据，OpenCode 的发现入口是 SKILL.md。

路径依据为 2026-11-09 查阅的官方说明。[OpenCode Skills](https://opencode.ai/docs/skills)
