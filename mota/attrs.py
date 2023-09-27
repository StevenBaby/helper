from collections import namedtuple

import numpy as np


Monster = namedtuple("Monster", ['life', 'attack', 'defense', 'coin'])

MONSTERS = {
    201: Monster(35, 18, 1, 1),  # 绿色史莱姆
    202: Monster(45, 20, 2, 2),  # 红色史莱姆
    203: Monster(130, 60, 3, 8),  # 大史莱姆
    205: Monster(35, 38, 3, 3),  # 小蝙蝠
    206: Monster(60, 100, 8, 12),  # 大蝙蝠
    208: Monster(444, 199, 66, 144),  # 吸血鬼
    209: Monster(50, 42, 6, 6),  # 骷髅人
    210: Monster(55, 52, 12, 8),  # 骷髅士兵
    211: Monster(100, 65, 15, 30),  # 骷髅队长
    212: Monster(220, 180, 30, 35),  # 鬼战士
    213: Monster(260, 85, 5, 18),  # 兽人
    214: Monster(320, 120, 15, 30),  # 兽人武士
    215: Monster(20, 100, 68, 28),  # 石头人
    216: Monster(320, 140, 20, 30),  # 幽灵
    217: Monster(60, 32, 8, 5),  # 初级法师
    218: Monster(100, 95, 30, 22),  # 高级法师
    221: Monster(50, 48, 22, 12),  # 初级卫兵
    225: Monster(210, 200, 65, 45),  # 战士
    226: Monster(120, 170, 50, 100),  # 骑士队长
    258: Monster(1200, 180, 20, 100),  # 大乌贼
}

EMPTY = 0
WALL = 1

STATE_NORMAL = 0
STATE_ALTAR = 131
STATE_MERCHANT = 122

MODE_ADD = -1
MODE_SUB = 1

GATEKEYS = {
    81: 21,  # 黄
    82: 22,  # 蓝
    83: 23,  # 红
}

ALTARS = {
    4: Monster(100, 2, 4, 0),
    12: Monster(100, 4, 8, 0),
}

Merchant = namedtuple("Merchant", ['coin', 'yellow', 'blue', 'red', 'life'])

MERCHANTS = {
    7: Merchant(50, 5, 0, 0, 0),
    12: Merchant(800, 0, 0, 1, 0),
    15: Merchant(200, 0, 1, 0, 0),
}

GUARDS = {
    8: [
        (
            (4, 10), 0,
            np.array(
                [
                    [5, 9],
                    [5, 11],
                ]
            )
        )
    ],
    10: [
        (
            (3, 6), 0,
            np.array([
                [4, 5],
                [4, 6],
                [4, 7],
                [5, 5],
                [5, 7],
                [6, 5],
                [6, 6],
                [6, 7],
            ])
        )
    ],
    11: [
        (
            (4, 2), 0,
            np.array([
                [5, 1],
                [5, 3],
            ]),
        )
    ],
    14: [
        (
            (3, 1), 23,
            np.array([
                [1, 1],
                [1, 3],
                [2, 2],
            ]),
        )
    ],
    17: [
        (
            (7, 2), 0,
            np.array([
                [8, 1],
                [8, 3],
            ])
        ),
        (
            (4, 2), 0,
            np.array([
                [5, 1],
                [5, 3],
            ])
        ),
        (
            (7, 10), 0,
            np.array([
                [8, 9],
                [8, 11],
            ])
        ),
        (
            (4, 10), 0,
            np.array([
                [5, 9],
                [5, 11],
            ])
        ),
    ],
    30: [
        (
            (4, 6), 0,
            np.array([
                [5, 3],
                [5, 4],
                [5, 5],
                [5, 7],
                [5, 8],
                [5, 9],
            ]),
        )
    ],
    33: [
        (
            (4, 10), 0,
            np.array([
                [5, 9],
                [5, 11],
                [7, 9],
                [7, 11],
            ]),
        ),
        (
            (8, 10), 0,
            np.array([
                [5, 9],
                [5, 11],
                [7, 9],
                [7, 11],
            ]),
        )
    ],
}
