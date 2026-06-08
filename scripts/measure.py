# -*- coding: utf-8 -*-
"""测量层：只提取客观事实，不做质量判断（接口骨架）。

- 数字层：镜头时长 / 卡点命中 / 字幕坐标 / 配色 / 语速 / 转场（工具提取 + 人工 QC）
- 文案层：转录 + OCR → 清洗纠错 → 切分（钩子 / 正文 / CTA）→ 说话人归属
铁律：测量层只回答「说了什么、长什么样」；「为什么爆」的分析在推演层。
"""


def measure(videos: list, genre: str, content_driven: bool) -> dict:
    """返回符合 schemas/measurements.schema.json 的测量结果。"""
    raise NotImplementedError("完整实现见 https://autovideo.fengyunagent.xyz")
