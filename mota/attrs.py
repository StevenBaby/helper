from collections import namedtuple

Monster = namedtuple("Monster", ['life', 'attack', 'defense', 'coin'])

MONSTERS = {
    201: Monster(35, 18, 1, 1),  # 绿色史莱姆
    202: Monster(45, 20, 2, 2),  # 红色史莱姆
    205: Monster(35, 38, 3, 3),  # 小蝙蝠
    209: Monster(50, 42, 6, 6),  # 骷髅人
    210: Monster(55, 52, 12, 8),  # 骷髅士兵
    217: Monster(60, 32, 8, 5),  # 初级法师
    221: Monster(50, 48, 22, 12),  # 初级卫兵
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
}

Merchant = namedtuple("Merchant", ['coin', 'yellow', 'blue', 'red', 'life'])

MERCHANTS = {
    7: Merchant(50, 5, 0, 0, 0),
}
