# -*- coding: utf-8 -*-
"""评分闸门 · 关1 机械数字对照（接口骨架）。

样片与对标模板跑同一套测量工具，逐维比（镜头时长 / 卡点命中 / 字幕坐标 / 配色 / BPM…），
过线判据 = 落在模板集自身实测区间内 → 防 p-hacking。
关2（真人「像不像 / 有没有魂」盲审）走在线表格闸门，不在本脚本。
"""


def score(sample_measure: dict, template_band: dict) -> dict:
    """逐维对照，返回每维是否在模板实测区间内 + 总判定。"""
    raise NotImplementedError("完整实现见 https://autovideo.fengyunagent.xyz")
