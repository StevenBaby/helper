from collections import namedtuple
from collections import UserDict
import typing


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
            AssignFloor({
                (10, 5): 0,
                (9, 4): 0,
                (9, 6): 0,
                (8, 5): 0,
                (7, 5): 0,
            }),
        ),
        Event(
            MatchWhere(10, 5),
            [
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
                121: 1,
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
                    (3, 1): 0,
                    (3, 2): 0,
                    (3, 3): 0,
                    (3, 6): 85,
                    (3, 9): 0,
                    (3, 10): 0,
                    (3, 11): 0,
                    (4, 2): 0,
                    (4, 5): 209,
                    (4, 6): 210,
                    (4, 7): 209,
                    (4, 10): 0,
                    (5, 5): 209,
                    (5, 6): 0,
                    (5, 7): 209,
                    (6, 5): 209,
                    (6, 6): 210,
                    (6, 7): 209,
                    (7, 6): 85,
                }),
            ]
        ),
        Event(
            MatchValue({
                (1, 6): 211,
                (4, 5): 0,
                (4, 6): 0,
                (4, 7): 0,
                (5, 5): 0,
                (5, 6): 0,
                (5, 7): 0,
                (6, 5): 0,
                (6, 6): 0,
                (6, 7): 0,
            }),
            AssignFloor({(3, 6): 0, }),
        ),
        Event(
            MatchValue({
                (1, 6): 0,
                (4, 5): 0,
                (4, 6): 0,
                (4, 7): 0,
                (5, 5): 0,
                (5, 6): 0,
                (5, 7): 0,
                (6, 5): 0,
                (6, 6): 0,
                (6, 7): 0,
            }),
            AssignFloor({
                (3, 6): 0,
                (7, 6): 0,
                (4, 4): 0,
                (4, 8): 0,
                (3, 1): 27,
                (3, 2): 27,
                (3, 3): 27,
                (3, 9): 28,
                (3, 10): 28,
                (3, 11): 28,
                (4, 1): 32,
                (4, 2): 32,
                (4, 3): 32,
                (4, 9): 21,
                (4, 10): 21,
                (4, 11): 21,
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
                (7, 5): 0,
                (7, 6): 0,
                (7, 7): 0,
                (6, 5): 0,
                (6, 6): 0,
                (6, 7): 0,
                (5, 5): 0,
                (5, 6): 0,
                (5, 7): 0,
                (3, 6): 0,
            })
        ),
    ],
    16: [
        Event(
            MatchWhere(11, 11),
            [
                AssignFloor({(11, 11): 0, }),
                AssignThings({320: 1}),
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
                AssignThings({321: 1}),
            ]
        ),
    ],
    20: [
        Event(
            MatchWhere(8, 6),
            [
                AssignFloor({(8, 6): 0, }),
                AssignFloor({
                    (5, 5): 0,
                    (5, 6): 0,
                    (5, 7): 0,
                    (6, 5): 0,
                    (6, 6): 208,
                    (6, 7): 0,
                    (7, 5): 0,
                    (7, 6): 0,
                    (7, 7): 0,
                }),
            ]
        ),
        Event(
            MatchWhere(6, 6),
            AssignFloor({
                (3, 6): 0,
                (4, 5): 21,
                (4, 6): 21,
                (4, 7): 21,
                (5, 4): 27,
                (6, 4): 27,
                (7, 4): 27,
                (5, 8): 28,
                (6, 8): 28,
                (7, 8): 28,
                (8, 5): 32,
                (8, 6): 32,
                (8, 7): 32,
            }),
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
                (5, 3): 0,
                (5, 4): 0,
                (5, 5): 0,
                (5, 7): 0,
                (5, 8): 0,
                (5, 9): 0,
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
    ],
    33: [
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
                (5, 9): 0,
                (5, 11): 0,
                (7, 9): 0,
                (7, 11): 0,
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
                (5, 1): 21,
                (5, 3): 21,
                (7, 1): 21,
                (7, 3): 21,
                (6, 2): 23,
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
                (2, 4): 0,
                (4, 6): 0,
                (2, 2): 81,
                (2, 6): 81,
                (4, 2): 81,
                (4, 4): 81,
                (6, 2): 81,
                (6, 4): 81,
                (6, 6): 81,
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
            MatchValue({
                (1, 6): 0,
                (2, 2): 0,
                (2, 3): 0,
                (2, 4): 0,
                (2, 8): 0,
                (2, 9): 0,
                (2, 10): 0,
                (4, 3): 0,
                (4, 4): 0,
                (4, 5): 0,
                (4, 7): 0,
                (4, 8): 0,
                (4, 9): 0,
            }),
            AssignFloor({
                (1, 6): 87,
                (2, 2): 21,
                (2, 3): 21,
                (2, 4): 21,
                (2, 8): 27,
                (2, 9): 27,
                (2, 10): 27,
                (4, 3): 32,
                (4, 4): 32,
                (4, 5): 32,
                (4, 7): 28,
                (4, 8): 28,
                (4, 9): 28,
            }),
        ),
    ],
}
