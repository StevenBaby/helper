
from collections import UserDict
import typing

import numpy as np
from numpy import array as a


class AssignAttr(typing.NamedTuple):
    name: str
    value: typing.Any


class ChangeAttr(typing.NamedTuple):
    name: str
    value: typing.Any


class AssignFloor(UserDict):
    ...


class AssignThings(dict):
    ...


class AssignSpecial(dict):
    ...


class MatchWhere(typing.NamedTuple):
    y: int
    x: int


class MatchValue(UserDict):
    ...


class Event(object):

    def __init__(self, match, change, times: int = 1) -> None:
        self.match = match
        self.change = change
        self.times = times


EVENTS: dict[int, list[Event]] = {
    2: [
        Event(
            MatchWhere(7, 3),
            AssignFloor({
                (7, 3): 0,
                (7, 2): 0,
            })
        ),
        Event(
            MatchWhere(4, 11),
            ChangeAttr('coin', 1000)
        ),
        Event(
            MatchWhere(11, 11),
            [
                AssignFloor({(11, 11): 0, }),
                AssignAttr("level", 35),
                AssignFloor({(10, 4): 0, }),
                AssignAttr("level", 2),
            ]
        ),
        Event(
            MatchValue({
                (2, 6): 0,
                (2, 8): 0,
            }),
            AssignFloor({
                (5, 5): 0,
                (5, 9): 0,
                (8, 5): 0,
                (8, 9): 0,
                (11, 5): 0,
                (11, 9): 0,
            }),
        ),
    ],
    3: [
        Event(
            MatchWhere(10, 5),
            [
                AssignFloor({
                    (7, 4): a([
                        1, 0, 1,
                        0, 0, 0,
                        0, 0, 0,
                        1, 0, 1,
                    ]).reshape(4, 3),
                }),
                AssignAttr('level', 2),
                AssignAttr('where', (8, 3)),
                AssignAttr('life', 400),
                AssignAttr('attack', 10),
                AssignAttr('defense', 10),
            ]
        ),
        Event(
            MatchWhere(4, 11),
            AssignThings({
                45: 1,
            })
        ),
    ],
    8: [
        Event(
            MatchValue({
                (5, 11): 0,
                (5, 9): 0,
            }),
            AssignFloor({
                (4, 10): 0,
            }),
        ),
    ],
    10: [
        Event(
            MatchWhere(5, 6),
            [
                AssignAttr('where', (5, 6)),
                AssignFloor({
                    (1, 6): 211,
                    (3, 1): a([
                        0, 0, 0, 0, 0, 0,
                    ]).reshape(2, 3),
                    (3, 9): a([
                        0, 0, 0, 0, 0, 0,
                    ]).reshape(2, 3),
                    (4, 5): a([
                        209, 210, 209,
                        209, 0, 209,
                        209, 210, 209,
                    ]).reshape(3, 3),
                    (3, 6): 85,
                    (7, 6): 85,
                }),
            ]
        ),
        Event(
            MatchValue({
                (1, 6): 211,
                (4, 5): a([
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                ]).reshape(3, 3),
            }),
            AssignFloor({(3, 6): 0, }),
        ),
        Event(
            MatchValue({
                (1, 6): 0,
                (4, 5): a([
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                ]).reshape(3, 3),
            }),
            AssignFloor({
                (3, 6): 0,
                (7, 6): 0,
                (4, 4): 0,
                (4, 8): 0,
                (3, 1): a([
                    27, 27, 27,
                    32, 32, 32,
                ]).reshape(2, 3),
                (3, 9): a([
                    28, 28, 28,
                    21, 21, 21,
                ]).reshape(2, 3),
                (11, 6): 87,
            }),
        ),
    ],
    11: [
        Event(
            MatchValue({
                (5, 1): 0,
                (5, 3): 0,
            }),
            AssignFloor({
                (4, 2): 0,
            }),
        ),
    ],
    14: [
        Event(
            MatchValue({
                (1, 1): 0,
                (1, 3): 0,
                (2, 2): 0,
            }),
            AssignFloor({
                (3, 1): 23,
            }),
        ),
    ],
    15: [
        Event(
            MatchWhere(1, 9),
            AssignFloor({
                (1, 9): 0,
                (1, 8): 0,
            })
        ),
        Event(
            MatchWhere(7, 6),
            AssignFloor({
                (3, 6): 0,
                (5, 5): a([
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                ]).reshape(3, 3),
            })
        ),
    ],
    16: [
        Event(
            MatchWhere(11, 11),
            [
                AssignFloor({(11, 11): 0, }),
                AssignThings({56: 1}),
            ]
        ),
    ],
    17: [
        Event(
            MatchValue({
                (8, 1): 0,
                (8, 3): 0,
            }),
            AssignFloor({
                (7, 2): 0,
            }),
        ),
        Event(
            MatchValue({
                (5, 1): 0,
                (5, 3): 0,
            }),
            AssignFloor({
                (4, 2): 0,
            }),
        ),
        Event(
            MatchValue({
                (8, 9): 0,
                (8, 11): 0,
            }),
            AssignFloor({
                (7, 10): 0,
            }),
        ),
        Event(
            MatchValue({
                (5, 9): 0,
                (5, 11): 0,
            }),
            AssignFloor({
                (4, 10): 0,
            }),
        ),
    ],
    19: [
        Event(
            MatchWhere(3, 6),
            [
                AssignFloor({(3, 6): 0, }),
                AssignThings({55: 1}),
            ]
        ),
    ],
    20: [
        Event(
            MatchWhere(8, 6),
            [
                AssignFloor({(8, 6): 0, }),
                AssignFloor({
                    (5, 5): a([
                        0, 0, 0,
                        0, 208, 0,
                        0, 0, 0,
                    ]).reshape(3, 3),
                }),
            ]
        ),
        Event(
            MatchWhere(6, 6),
            AssignFloor({
                (3, 6): 0,
                (4, 5): a([21, 21, 21]).reshape(1, 3),
                (5, 4): a([27, 27, 27]).reshape(3, 1),
                (5, 8): a([28, 28, 28]).reshape(3, 1),
                (8, 5): a([32, 32, 32]).reshape(1, 3),
            }),
        ),
    ],
    24: [
        Event(
            [
                MatchWhere(1, 6),
                MatchValue({
                    (1, 5): a([1, 0, 1]).reshape(1, 3),
                })
            ],
            [
                AssignAttr('level', 50),
                AssignAttr('where', (7, 6)),
            ]
        ),
    ],
    25: [
        Event(
            MatchValue({
                (6, 6): 0,
            }),
            [
                AssignFloor({
                    (8, 4): a([23, 23, 0, 23, 23]).reshape(1, 5),
                }),
            ]
        ),
    ],
    26: [
        Event(
            MatchWhere(6, 6),
            [
                AssignAttr('level', 24),
                AssignFloor({
                    (1, 5): a([1, 0, 1]).reshape(1, 3),
                    (2, 6): a([0, 0, 0]).reshape(3, 1),
                }),
                AssignAttr('level', 26),
            ]
        ),
    ],
    29: [
        Event(
            MatchWhere(2, 6),
            [
                AssignFloor({
                    (2, 6): 0,
                    (3, 6): 0,
                }),
                AssignAttr('level', 2),
                AssignFloor({
                    (11, 11): 123,
                }),
                AssignAttr('level', 29),
            ]
        ),
    ],
    30: [
        Event(
            MatchValue({
                (5, 3): a([0, 0, 0, 0, 0, 0, 0]).reshape(1, 7),
            }),
            AssignFloor({
                (4, 6): 0,
            }),
        ),
    ],
    32: [
        Event(
            MatchValue({
                (10, 1): 0,
                (10, 3): 0,
            }),
            AssignFloor({
                (9, 2): 0,
            }),
        ),
        Event(
            MatchWhere(10, 6),
            AssignSpecial({
                32: {
                    (9, 6): 1,
                }
            })
        ),
    ],
    33: [
        Event(
            MatchWhere(10, 9),
            AssignFloor({
                (10, 8): 1,
            }),
        ),
        Event(
            MatchWhere(5, 10),
            [
                AssignAttr('where', (5, 10)),
                AssignFloor({
                    (4, 10): 85,
                    (5, 10): 0,
                    (8, 10): 85,
                }),
            ]
        ),
        Event(
            MatchValue({
                (5, 9): a([
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                ]).reshape(3, 3),
            }),
            AssignFloor({
                (4, 10): 0,
                (8, 10): 0,
            }),
        ),
    ],
    34: [
        Event(
            MatchValue({
                (4, 5): 0,
                (8, 5): 0,
                (4, 7): 0,
                (8, 7): 0,
                (4, 9): 0,
                (8, 9): 0,
                (4, 11): 0,
                (8, 11): 0,
            }),
            AssignFloor({
                (5, 1): a([
                    21, 0, 21,
                    0, 23, 0,
                    21, 0, 21,
                ]).reshape(3, 3),
            }),
        ),
    ],
    35: [
        Event(
            MatchValue({
                (7, 6): 0,
            }),
            AssignFloor({
                (2, 6): 0,
                (5, 5): a([
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                ]).reshape(3, 3),
            }),
        ),
    ],
    38: [
        Event(
            MatchValue({
                (10, 1): 0,
                (10, 3): 0,
            }),
            AssignFloor({
                (9, 2): 0,
            }),
        ),
        Event(
            MatchWhere(6, 2),
            AssignFloor({
                (5, 2): 1,
            }),
        ),
    ],
    39: [
        Event(
            MatchValue({
                (2, 2): a([
                    81, 0, 0, 0, 81,
                    0, 0, 0, 0, 0,
                    81, 0, 81, 0, 0,
                    0, 0, 0, 0, 0,
                    81, 0, 81, 0, 81,
                ]).reshape(5, 5),
            }),
            AssignFloor({
                (4, 4): 50,
            }),
        ),
    ],
    40: [
        Event(
            [
                MatchWhere(7, 6),
                MatchValue({
                    (8, 6): 0,
                })
            ],
            AssignFloor({
                (8, 6): 85,
            }),
        ),
        Event(
            [
                MatchWhere(7, 6),
                MatchValue({
                    (1, 6): 226,
                    (2, 2): a([224, 224, 224]).reshape(1, 3),
                    (2, 8): a([227, 227, 227]).reshape(1, 3),
                    (4, 3): a([212, 212, 212]).reshape(1, 3),
                    (4, 7): a([225, 225, 225]).reshape(1, 3),
                })
            ],
            AssignSpecial({
                40: {
                    (1, 6): 1,
                    (2, 2): 1,
                    (2, 3): 1,
                    (2, 4): 1,
                    (2, 8): 1,
                    (2, 9): 1,
                    (2, 10): 1,
                    (4, 3): 1,
                    (4, 4): 1,
                    (4, 5): 1,
                    (4, 7): 1,
                    (4, 8): 1,
                    (4, 9): 1,
                }
            })
        ),
        Event(
            MatchValue({
                (1, 6): 0,
                (2, 2): a([0, 0, 0]).reshape(1, 3),
                (2, 8): a([0, 0, 0]).reshape(1, 3),
                (4, 3): a([0, 0, 0]).reshape(1, 3),
                (4, 7): a([0, 0, 0]).reshape(1, 3),
            }),
            AssignFloor({
                (1, 6): 87,
                (2, 2): a([21, 21, 21]).reshape(1, 3),
                (2, 8): a([27, 27, 27]).reshape(1, 3),
                (4, 3): a([32, 32, 32]).reshape(1, 3),
                (4, 7): a([28, 28, 28]).reshape(1, 3),
            }),
        ),
        Event(
            MatchValue({
                (1, 6): 87,
                (8, 6): 85,
            }),
            AssignFloor({
                (8, 6): 0,
            }),
        ),
    ],
    41: [
        Event(
            MatchWhere(2, 10),
            AssignFloor({
                (2, 10): 220,
            }),
        ),
        Event(
            MatchValue({
                (2, 2): 0,
                (2, 10): 0,
            }),
            AssignFloor({
                (5, 5): a([
                    1, 52, 1,
                    1, 1, 1,
                    0, 0, 0,
                ]).reshape(3, 3)
            }),
        ),
    ],
    44: [
        Event(
            MatchValue({
                (9, 5): 0,
                (9, 7): 0,
            }),
            AssignFloor({
                (8, 6): 0,
            }),
        ),
    ],
    45: [
        Event(
            MatchValue({
                (9, 8): 0,
                (11, 8): 0,
            }),
            AssignFloor({
                (10, 7): 0,
            }),
        ),
        Event(
            MatchValue({
                (9, 5): 0,
                (11, 5): 0,
            }),
            AssignFloor({
                (10, 4): 0,
            }),
        ),
    ],
    47: [
        Event(
            [
                MatchWhere(var, 1),
                MatchValue({
                    (var - 1, 1): 229,
                })
            ],
            AssignFloor({
                (var - 2, 1): 229,
                (var - 1, 1): 0,
            }),
        ) for var in range(10, 3, -1)
    ] + [
        Event(
            [
                MatchWhere(var, 1),
                MatchValue({
                    (var + 1, 1): 229,
                })
            ],
            AssignFloor({
                (var + 2, 1): 229,
                (var + 1, 1): 0,
            }),
        ) for var in range(8, 10)
    ] + [
        Event(
            [
                MatchWhere(3, 8),
                MatchValue({
                    (2, 8): 229,
                })
            ],
            AssignFloor({
                (1, 8): 229,
                (2, 8): 0,
            }),
        )
    ],
    49: [
        Event(
            MatchValue({
                (10, 5): 0,
                (10, 7): 0,
            }),
            AssignFloor({
                (9, 6): 0,
            }),
        ),
        Event(
            MatchValue({
                (8, 5): 0,
                (8, 7): 0,
            }),
            AssignFloor({
                (7, 6): 0,
            }),
        ),
        Event(
            MatchWhere(6, 6),
            [
                AssignFloor({
                    (7, 6): 85,
                    (0, 0): 324,
                    (2, 5): a([
                        [246, 246, 246,],
                        [246, 245, 246,],
                        [246, 246, 246,]
                    ]),
                }),
            ]
        ),
        Event(
            MatchValue({
                (2, 5): a([
                    [246, 0, 246,],
                    [0, 245, 0,],
                    [246, 0, 246,]
                ]),
            }),
            AssignThings({
                323: 1,
            })
        ),
        Event(
            MatchValue({
                (3, 6): 0,
                (0, 0): 324,
            }),
            AssignFloor({
                (2, 5): a([[23, 0, 62],]),
                (4, 2): a([[27, 27, 27, 0, 0, 0, 28, 28, 28],]),
                (5, 5): a([[32, 32, 32],]),
                (7, 6): 0,
            })
        ),
    ],
    50: [
        Event(
            MatchWhere(6, 6),
            [
                AssignFloor({
                    (5, 6): 249,
                }),
            ]
        ),
    ]
}
