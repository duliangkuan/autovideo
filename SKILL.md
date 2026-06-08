# AutoVideo — 编排器说明

> 本文件说明 AutoVideo 编排器的**工作流与分层**。完整的步骤实现、配方参数、文案模型与工具链接入是产品本体，见 [autovideo.fengyunagent.xyz](https://autovideo.fengyunagent.xyz)。

## 触发

当需要「逆向某类爆款 → 搭一条产这类视频的自动化流水线」时启动。输入：同类对标视频（3–5 条）+ 一句话说明。

## 工作方式

「人 + AI 协同」，非全自动、无人值守。逆向拆解一个新赛道、搭出能跑的流水线，快的话 3 天以内可以完成。

## 编排流程

```
Step 0  建审阅载体（在线多维表格，一表两用：传对标视频 + 闸门审阅）
Step 1  获取对标视频            → scripts/fetch.py
Step 2  测量（数字 + 干净文案）  → scripts/measure.py
Step 3  推演剪辑配方 harness     → 产出 recipe + 素材对照清单 + 样片
Step 4  关1 数字对照            → scripts/score.py
Step 5  关2 真人盲审（飞书闸门）
Step 6  造厂：照配方生成 <赛道>-pipeline 项目
```

## 关键纪律

- 测量层只「提取」，不「分析」；分析在推演层。
- 内容维度（选题 + 文案）是最高权重。
- 数据先行：模式归纳先跨多条样本验证。
- 供料可行性闸门卡在推演阶段。
- 两道关都过才算配方对（机器数字 + 真人味道）。
- 不打扰原则：搜索 / 下载 / 写脚本自动做；只有「要用户的钱/账号的 key」和「法律 / ToS 风险动作」才攒一张清单一次性问。

---

> 完整系统 / 课程 / 定制 → [autovideo.fengyunagent.xyz](https://autovideo.fengyunagent.xyz)
