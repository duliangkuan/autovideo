# -*- coding: utf-8 -*-
"""配方执行器：recipe + 新选题 → 样片.mp4（接口骨架）。

双重身份：推演期用它出样片做验收（样片 ≈ 模板为收敛判据）；
冻结 + 特化后打包进 <赛道>-pipeline 作为生产引擎。
"""


def execute(recipe: dict, topic: str, out_path: str) -> str:
    """按配方 + 新选题生成样片，返回输出路径。"""
    raise NotImplementedError("完整实现见 https://autovideo.fengyunagent.xyz")
