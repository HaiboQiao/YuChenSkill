# guided-learning-tutor｜个人学习导师

## What

一个供 Codex 与 OpenCode 使用的纯指令 Skill：先讲清当前主线，再逐渐展开必要知识。它优化 AI 的学习对话，不需要 Python、Node、API、Obsidian 或笔记系统。

## Why

回答有很多知识不等于学习者能理解。这个 Skill 把篇幅留给当前原理、前置关系和一个具体例子；相关知识可以主动补充，但不会把核心淹没。详细意味着解释更透，不意味着一次百科式展开。

## Modes

- Quick：小概念、小区别。
- Standard：普通原理与算法知识点，默认模式。
- Deep：明确详细讲、学透；先地图，再展开一个尚未掌握的模块。
- Practice：一题一轮，按需逐层提示。
- Learn by Doing：一次目的明确的实操步骤，观察结果后继续。
- Review：定位已有基础中的具体缺口，不重讲整套课程。

Teach（先教）与 Guide（补缺口）由已有基础决定；不会默认每轮苏格拉底问答或考试。

## Installation

唯一共享安装内容：

- Windows：`%USERPROFILE%\.agents\skills\guided-learning-tutor\`
- Linux/macOS：`~/.agents/skills/guided-learning-tutor/`

[Codex 官方技能文档](https://learn.chatgpt.com/docs/build-skills) 与 [OpenCode 官方技能文档](https://opencode.ai/docs/skills/) 都列出了用户级 `.agents/skills`。不要再给两个客户端各复制一份。遇到旧客户端不发现时先核对版本、技能权限与官方搜索位置，再考虑指向这一 canonical 内容的目录链接，避免维护多份正文。

放入后开新会话；Codex 支持检测技能变更，若列表未更新可重新加载或重启客户端。OpenCode 由 `skill` 工具按需加载。核心仅使用通用 name / description frontmatter；agents/openai.yaml 仅增强 Codex UI。

本机具体路径、真实发现结果及评测证据在开发项目的 README.md 与 evaluation/report.md 中；此包不声称所有版本都已实际验证。更新时编辑同一 canonical 内容，重新验证对应场景，不覆盖其他技能。

## Usage

直接说：

- “给我讲一下前缀和。”
- “这个我要学透。”
- “只讲主线。”
- “这里没懂，换种方式。”
- “举个例子。”
- “考考我。”

Codex 也可以显式使用：`$guided-learning-tutor 给我讲一下前缀和。`

在 OpenCode 中可以说：“使用 guided-learning-tutor 教我前缀和。”自然语言仍由客户端选择并加载 Skill，不保证每条消息都会自动触发。新会话没有旧的学习上下文时，补一句当前学到哪里即可。

## Design

Mainline First（主线优先）、Progressive Disclosure（渐进展开）、Terminology Gate（先解释再命名）、Relevance Anchor（说明知识为何出现）、Comprehension Repair（困惑时降低信息量并换表示）。S/M/L 是软预算，不是强行缩短或凑字。

```text
guided-learning-tutor/
├── SKILL.md
├── README.md
├── references/
│   ├── teaching-principles.md
│   ├── response-patterns.md
│   ├── learning-modes.md
│   ├── examples.md
│   └── evaluation.md
└── agents/
    └── openai.yaml
```

## Credits

独立按用户需求编写，参考思想而未复制第三方 Skill 正文：

- [Lucian1u/learning-coach](https://github.com/Lucian1u/learning-coach)：适应已有基础，缺前置先教，按需提示与练习；核查为 MIT。
- [quzhi-ai/deep-learning](https://github.com/quzhi-ai/deep-learning)：分步深入、复述与理解验证；核查为 MIT，这里仅在深入学习时自愿使用。
- [gkuchar/educational-agent-skills](https://github.com/gkuchar/educational-agent-skills)：逐轮 Hint、Debrief、回忆与迁移；2026-10-04 下载的 main 归档未找到 LICENSE，因此未复制其文本或代码。
- [scibly-dev/skills](https://github.com/scibly-dev/skills)：教学削减、学习目标及微学习；核查为 MIT，这里不强制普通学习先填需求表或测验。

调研快照与许可证只作项目内留档，不作为运行依赖。遵循 [Agent Skills 通用规范](https://agentskills.io/specification)。
