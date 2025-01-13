import numpy as np
import os
import json_tricks

from pathlib import Path

home_dir = Path(__file__).parent.resolve()

answer = {
    "task1": {
        "det_A_terms": sorted([
            -1,
            -1
        ]),
        "det_A_1_terms": sorted([
            -2,
            0
        ]),
        "det_A_2_terms": sorted([
            0,
            -2
        ]),
        "x": np.array([
            1,
            1
        ]),
        "cofactors": np.array([
            [-1, -1],
            [-1, 1]
        ]),
        "inverse": np.array([
            [0.5, -0.5],
            [-0.5, -0.5]
        ], dtype='float64')
    },
    "task2": {
        "det_A_terms": sorted([
            2,
            3
        ]),
        "det_A_1_terms": sorted([
            2,
            8
        ]),
        "det_A_2_terms": sorted([
            8,
            -3
        ]),
        "x": np.array([
            2,
            1
        ]),
        "cofactors": np.array(
            [
                [2, -3],
                [1, 1]
            ]
        ),
        "inverse": np.array([
            [-0.4, -0.2],
            [0.6, -0.2]
        ])
    },
    "task3": {
        "det_A_terms": sorted([
            -2,
            3,
            2,
            1,
            -6,
            -2
        ]),
        "det_A_1_terms": sorted([
            -4,
            9,
            0,
            3,
            -12,
            0
        ]),
        "det_A_2_terms": sorted([
            0, 6, 3, 0, -9, -4
        ]),
        "x": np.array([
            1, 1, 0
        ]),
        "cofactors": np.array([
            [-1, -1],
            [-1, 1]
        ]),
        "inverse": np.array([
            [0.5, -0.5],
            [-0.5, -0.5]
        ])
    }
}

json_tricks.dump(
    answer, 
    open(home_dir/Path('.answer.json'), "w+"))