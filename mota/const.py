from collections import namedtuple
import enum

import numpy as np


Monster = namedtuple(
    "Monster", [
        'life', 'attack', 'defense', 'coin', 'domain'])

MONSTERS = {
    201: Monster(35, 18, 1, 1, 0),  # 绿色史莱姆
    202: Monster(45, 20, 2, 2, 0),  # 红色史莱姆
    203: Monster(130, 60, 3, 8, 0),  # 大史莱姆
    204: Monster(360, 310, 20, 40, 0),  # 史莱姆王
    205: Monster(35, 38, 3, 3, 0),  # 小蝙蝠
    206: Monster(60, 100, 8, 12, 0),  # 大蝙蝠
    207: Monster(200, 390, 90, 50, 0),  # 吸血蝙蝠
    208: Monster(444, 199, 66, 144, 0),  # 吸血鬼
    209: Monster(50, 42, 6, 6, 0),  # 骷髅人
    210: Monster(55, 52, 12, 8, 0),  # 骷髅士兵
    211: Monster(100, 65, 15, 30, 0),  # 骷髅队长
    212: Monster(220, 180, 30, 35, 0),  # 鬼战士
    213: Monster(260, 85, 5, 18, 0),  # 兽人
    214: Monster(320, 120, 15, 30, 0),  # 兽人武士
    215: Monster(20, 100, 68, 28, 0),  # 石头人
    216: Monster(320, 140, 20, 30, 0),  # 幽灵
    217: Monster(60, 32, 8, 5, 0),  # 初级法师
    218: Monster(100, 95, 30, 22, 0),  # 高级法师
    219: Monster(220, 370, 110, 80, 100),  # 初级巫师
    220: Monster(200, 380, 130, 90, 200),  # 高级巫师
    221: Monster(50, 48, 22, 12, 0),  # 初级卫兵
    222: Monster(100, 180, 110, 50, 0),  # 中级卫兵
    223: Monster(180, 460, 360, 200, 0),  # 高级卫兵
    224: Monster(100, 680, 50, 55, 0),  # 双手剑士
    225: Monster(210, 200, 65, 45, 0),  # 战士
    226: Monster(120, 150, 50, 100, 0),  # 骑士队长
    227: Monster(160, 230, 105, 65, 0),  # 骑士
    228: Monster(180, 430, 210, 120, 0),  # 黑暗骑士
    229: Monster(200, 380, 130, 90, 200),  # 高级巫师
    245: Monster(8000, 5000, 1000, 500, 0),  # 魔王
    246: Monster(230, 450, 100, 100, 0),  # 魔法卫士
    247: Monster(4500, 560, 310, 1000, 0),  # 大法师
    249: Monster(5000, 1580, 190, 500, 0),  # 魔王
    257: Monster(1500, 600, 250, 800, 0),  # 魔龙
    258: Monster(1200, 180, 20, 100, 0),  # 大乌贼
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
    4: Monster(100, 2, 4, 0, 0),
    12: Monster(100, 4, 8, 0, 0),
    32: Monster(300, 8, 16, 0, 0),
    46: Monster(300, 10, 20, 0, 0),
}

Merchant = namedtuple(
    "Merchant", [
        'coin',
        'yellow',
        'blue',
        'red',
        'life',
        'scroll',
        'property',
    ])

MERCHANTS = {
    2: Merchant(0, 0, 0, 0, 0, 0, 3),
    6: Merchant(50, 0, 1, 0, 0, 0, 0),
    7: Merchant(50, 5, 0, 0, 0, 0, 0, ),
    12: Merchant(800, 0, 0, 1, 0, 0, 0, ),
    15: Merchant(200, 0, 1, 0, 0, 0, 0, ),
    28: Merchant(-100, -1, 0, 0, 0, 0, 0, ),
    31: Merchant(1000, 4, 1, 0, 0, 0, 0, ),
    38: Merchant(200, 3, 0, 0, 0, 0, 0, ),
    39: Merchant(2000, 0, 3, 0, 0, 0, 0, ),
    45: Merchant(1000, 0, 0, 0, 2000, 0, 0, ),
    47: Merchant(4000, 0, 0, 0, 0, 1, 0, ),
}


class MASK(enum.Enum):
    MASK_EMPTY = enum.auto()
    MASK_UNKNOWN = enum.auto()
    MASK_VISITED = enum.auto()
    MASK_INVALID = enum.auto()
    MASK_VALID1 = enum.auto()
    MASK_VALID2 = enum.auto()
    MASK_VALID3 = enum.auto()


TOOLS = {
    'q': 50,  # 瞬移
    'w': 47,  # 破墙镐
    'e': 57,  # 地震卷轴
    'r': 49,  # 炸弹
    't': 51,  # 上楼器
    'y': 26,  # 魔法钥匙
    'u': 52,  # 下楼器
    'i': 54,  # 冰冻徽章
    'o': 56,  # 圣水
}

TOOLKEYS = {v: k for k, v in TOOLS.items()}
