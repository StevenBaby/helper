import os
import shutil
import copy
import csv
import math
import json
import numpy as np

from const import *
import maps
import events
import const as c
from logger import logger


class Game(object):

    @property
    def floor(self):
        return self.tower[self.level]

    @property
    def mask(self):
        return self.masks[self.level]

    @property
    def coinrate(self):
        if 53 in self.things:
            return 2
        return 1

    def next_price(self):
        # logger.debug("price %s times %d", self.price, self.times)
        return self.price + self.times * 20

    def nearby(self, where, value=None, wall=False):
        nears = []
        for var in [(-1, 0), (1, 0), (0, -1), (0, 1),]:
            var = self.addoffset(where, var)
            if self.floor[var] == 1 and not wall:
                continue
            if value is None:
                nears.append(var)
                continue
            if self.floor[var] == value:
                nears.append(var)
        return nears

    def reset(self):
        self.tower = np.copy(maps.M)
        self.masks = np.zeros((51, 13, 13))
        self.level = 1
        self.max_level = 1
        self.min_level = 1
        self.where = np.array((11, 6))
        self.things = {}
        self.special = {}

        self.life = 1000
        self.attack = 100
        self.defense = 100
        self.coin = 0
        self.price = 20
        self.times = 0
        self.state = 0
        self.mode = MODE_ADD
        self.actions = []
        self.events = copy.deepcopy(events.EVENTS)

    def __init__(self) -> None:
        self.reset()

    def record(self, action, where=(0, 0)):
        self.actions.append((
            self.level,
            self.state,
            action,
            where[0],
            where[1]
        ))

    def domainful(self, where):
        if 44 in self.things:  # 神圣盾
            return 0

        if set(where) & {0, 12}:
            return 0

        total = 0
        nears = []
        for near in self.nearby(where, wall=True):
            nears.append(near)
            if self.floor[near] not in (219, 220, 229):
                continue
            m = MONSTERS[self.floor[near]]
            total += m.domain

        pairs = set([
            (self.floor[nears[0]], self.floor[nears[1]]),
            (self.floor[nears[2]], self.floor[nears[3]]),
        ])
        if pairs & {(246, 246), }:  # 魔法警卫夹攻
            value = self.life // 2
            total += value

        return total

    def harmful(self, where, monster):
        if monster not in MONSTERS:
            return -1

        m = MONSTERS[monster]

        attack = self.attack
        if monster in (208, 213, 214) and 321 in self.things:  # 十字架
            attack *= 2

        if monster in (257, ) and 62 in self.things:  # 屠龙匕
            attack *= 2

        if monster in (245,) and 323 in self.things:  # 阵法被破解
            m = Monster(
                m.life // 10,
                m.attack // 10,
                m.defense // 10,
                m.coin,
                m.domain // 10)

        specials = {}
        special = 0

        if self.level in self.special:
            specials = self.special[self.level]

        where = tuple(where)
        if where in specials:
            special = specials[where]
            # logger.debug(
            #     'special %s %s %s %s',
            #     self.level, where, special, specials)

        if m.defense >= attack:
            # logger.debug("monster defense >= attack")
            return -1

        mlife = m.life
        total = 0

        harm = attack - m.defense
        hurt = m.attack - self.defense
        if special == 1 and hurt > 0:  # 先攻
            total += hurt

        while True:
            mlife -= harm
            if mlife <= 0:
                break

            if hurt > 0:
                total += hurt

        return total

    def domain(self, where):
        if self.level <= 40:
            return True
        total = self.domainful(where)
        if total <= 0:
            return True
        if self.life <= total:
            return False

        self.life -= total
        return True

    def clear(self, where):
        if not self.domain(where):
            return
        self.floor[tuple(where)] = 0
        self.where = where

    def collect(self, where, thing):
        # logger.debug('collect %s', thing)
        self.clear(where)

        match thing:
            case 27:  # 红宝石
                if self.level <= 10:
                    self.attack += 1
                elif self.level <= 20:
                    self.attack += 2
                elif self.level <= 40:
                    self.attack += 4
                elif self.level <= 50:
                    self.attack += 5
            case 28:  # 蓝宝石
                if self.level <= 10:
                    self.defense += 1
                elif self.level <= 20:
                    self.defense += 2
                elif self.level <= 40:
                    self.defense += 4
                elif self.level <= 50:
                    self.defense += 5
            case 31:  # 红药水
                if self.level <= 10:
                    self.life += 50
                elif self.level <= 20:
                    self.life += 100
                elif self.level <= 40:
                    self.life += 200
                elif self.level <= 50:
                    self.life += 250
            case 32:  # 蓝药水
                if self.level <= 10:
                    self.life += 200
                elif self.level <= 20:
                    self.life += 400
                elif self.level <= 40:
                    self.life += 800
                elif self.level <= 50:
                    self.life += 1000

            case 35:  # 铁剑
                self.attack += 10
            case 36:  # 铁盾
                self.defense += 10
            case 37:  # 银剑
                self.attack += 20
            case 38:  # 银盾
                self.defense += 20
            case 39:  # 骑士剑
                self.attack += 40
            case 40:  # 骑士盾
                self.defense += 40
            case 41:  # 圣剑
                self.attack += 50
            case 42:  # 圣盾
                self.defense += 50
            case 43:  # 神圣剑
                self.attack += 100
            case 44:  # 神圣盾
                self.defense += 100
                self.things[44] = 1
            case 50:  # 瞬移
                self.things[50] = 3
            case _:
                self.things.setdefault(thing, 0)
                self.things[thing] += 1

    def battle(self, where, monster):
        # logger.debug("%s, %s", where, monster)
        hurt = self.harmful(where, monster)
        if hurt < 0:
            return False

        life = self.life - hurt * self.mode
        if life <= 0:
            return False

        m = MONSTERS[monster]
        self.life = life
        self.coin += m.coin * self.coinrate
        self.floor[tuple(where)] = 0

        where = tuple(where)
        if where in self.special:
            del self.special[where]
        return True

    def addoffset(self, where, offset):
        return (
            int(where[0] + offset[0]),
            int(where[1] + offset[1])
        )

    def stairs(self, where, stair):
        # logger.debug(f'open %s, %s', where, gate)
        match stair:
            case 87:  # 上楼
                level = self.level + 1
                if level == 44:
                    level += 1
                after = 88
            case 88:  # 下楼
                level = self.level - 1
                if level == 44:
                    level -= 1
                after = 87

        self.level = level
        self.max_level = max(self.max_level, self.level)
        self.min_level = min(self.min_level, self.level)
        args = np.argwhere(self.floor == after)
        if len(args) == 0:
            return
        nearby = self.nearby(args[0], 0)
        self.where = nearby[0]

    def open(self, where, gate):
        key = GATEKEYS[gate]
        if key not in self.things:
            return
        if self.things[key] == 0:
            logger.debug("no key %s", key)
            return

        self.things[key] -= 1
        self.clear(where)

    def move(self, where):
        logger.debug('move to %s', where)
        spot = int(self.floor[where])

        match spot:
            case 1:
                # logger.debug("wall %s", where)
                return
            case 0:
                if self.domain(where):
                    self.where = where
            case spot if spot in range(20, 80):
                self.collect(where, spot)
            case spot if spot in (81, 82, 83):
                self.open(where, spot)
            case spot if spot in (87, 88):
                self.stairs(where, spot)
            case spot if spot in range(200, 260):
                self.battle(where, spot)
            case spot if spot in (121, 3, 2):
                self.clear(where)
            case 122:  # 商人
                self.state = STATE_MERCHANT
            case 124:  # 回收商人
                self.state = STATE_MERCHANT
            case 131:  # 祭坛
                self.state = STATE_ALTAR

    def route(self, to: np.ndarray):
        to = tuple(to)
        queue = [tuple(self.where)]
        visited = set()

        while queue:
            pos = queue.pop(0)
            if pos == to:
                # logger.info("find route from %s to %s", tuple(self.where), to)
                return True
            if pos in visited:
                continue
            visited.add(pos)
            for near in self.nearby(pos):
                if near == to:
                    queue.append(near)
                    break

                if near in visited:
                    continue

                if self.floor[near] not in {0, 87, 88}:
                    continue
                if self.domainful(near) > 0:
                    continue

                queue.append(near)

        return False

    def save_state(self, filename='state.csv'):
        logger.info("save state %s", filename)
        tmp = f'{filename}.tmp'
        try:
            with open(tmp, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.actions)
            shutil.move(tmp, filename)
        except Exception as e:
            os.remove(tmp)
            raise e

    def load_state(self, filename='state.csv'):
        if not os.path.exists(filename):
            return

        logger.info("load state %s", filename)

        try:
            self.reset()
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for level, state, action, x, y in reader:
                    self.execute(action, (int(x), int(y)))
        except Exception as e:
            logger.error('load state error %s', e)
            return

    def match_event(self, match, where):
        if isinstance(match, list):
            for var in match:
                if not self.match_event(var, where):
                    return False
            return True
        if isinstance(match, events.MatchWhere):
            if match == where:
                return True
        elif isinstance(match, events.MatchValue):
            for where, value in match.items():
                if isinstance(value, int) and self.floor[where] != value:
                    return False
                elif isinstance(value, np.ndarray):
                    i, j = where
                    w, h = value.shape
                    area = self.floor[i:i + w, j: j + h]
                    if not np.all(area == value):
                        return False
            return True
        return False

    def action_change(self, change):
        match change:
            case list():
                for var in change:
                    self.action_change(var)
            case events.AssignFloor():
                for key, value in change.items():
                    if isinstance(value, int):
                        self.floor[key] = value
                    elif isinstance(value, np.ndarray):
                        i, j = key
                        w, h = value.shape
                        self.floor[i:i + w, j: j + h] = value

            case events.AssignAttr():
                assert (hasattr(self, change.name))
                setattr(self, change.name, change.value)
                logger.debug("set attr %s %s", change.name, change.value)
            case events.ChangeAttr():
                assert (hasattr(self, change.name))
                setattr(self, change.name,
                        change.value + getattr(self, change.name))
            case events.AssignThings():
                self.things.update(change)
            case events.AssignSpecial():
                self.special.update(change)

    def action_event(self, where):
        where = tuple(where)
        if self.level not in self.events:
            return

        items = self.events[self.level]

        for e in items[:]:
            if not self.match_event(e.match, where):
                continue
            self.action_change(e.change)

            e.times -= 1
            if e.times == 0:
                items.remove(e)

    def action_tool(self, tool):
        tools = {
            'q': 50,  # 瞬移
            'w': 47,  # 破墙镐
            'e': 57,  # 地震卷轴
            'r': 49,  # 炸弹
            't': 51,  # 上楼器
            'y': 26,  # 魔法钥匙
            'u': 52,  # 下楼器
            'i': 54,  # 冰冻徽章
            'o': 320,  # 圣水
        }

        if tool not in tools:
            return
        thing = tools[tool]
        if thing not in self.things:
            return
        assert (self.things[thing] > 0)

        match tool:
            case 'q':  # 瞬移
                where = np.array([-6, -6]) + self.where
                where = np.array([6, 6]) - where
                logger.debug('fly to %s', where)
                if self.floor[tuple(where)] == 0:
                    self.where = where
                    self.things[thing] -= 1

            case 'w':  # 破墙镐
                for offset in np.array([[1, 0], [-1, 0], [0, 1], [0, -1]]):
                    where = self.where + offset
                    if set(where) & {0, 12}:
                        continue
                    if self.floor[tuple(where)] != 1:
                        continue
                    self.floor[tuple(where)] = 0
                    self.things[thing] = 0

            case 'e':  # 地震卷轴
                logger.info("use scroll")
                for i in range(1, 12):
                    for j in range(1, 12):
                        if self.floor[i, j] != 1:
                            continue
                        self.floor[i, j] = 0
                        self.things[thing] = 0

            case 'r':  # 炸弹
                logger.info("use bomb")
                for near in self.nearby(self.where):
                    idx = self.floor[near]
                    if idx not in MONSTERS:
                        continue

                    self.floor[near] = 0
                    self.things[thing] = 0
                    self.coin += MONSTERS[idx].coin * self.coinrate

            case 't':  # 上楼器
                if self.level >= 49:
                    return
                level = self.level + 1
                if self.tower[level][tuple(self.where)] == 0:
                    self.level = level
                    self.things[thing] = 0
            case 'u':  # 下楼器
                level = self.level - 1
                if self.tower[level][tuple(self.where)] == 0:
                    self.level = level
                    self.things[thing] = 0
            case 'y':  # 魔法钥匙
                args = np.argwhere(self.floor == 81)
                if len(args) == 0:
                    return
                logger.debug("open all yellow doors")
                Y = np.transpose(args)[0]
                X = np.transpose(args)[1]
                self.floor[Y, X] = 0
                self.things[thing] = 0
            case 'i':  # 冰冻徽章
                logger.info("use ice")
                for near in self.nearby(self.where):
                    idx = self.floor[near]
                    if idx != 5:
                        continue
                    self.floor[near] = 0
            case 'o':  # 圣水
                logger.info("use water")
                self.life += math.floor((self.attack + self.defense) * 7.4)
                self.things[thing] = 0

        if self.things[thing] == 0:
            del self.things[thing]

    def action_merchant(self, action):
        if action != '1':
            return

        merchant = MERCHANTS[self.level]
        if self.coin < merchant.coin:
            logger.info("no enough coin")
            return

        self.coin -= merchant.coin

        self.things.setdefault(21, 0)
        self.things.setdefault(22, 0)
        self.things.setdefault(23, 0)

        self.things[21] += merchant.yellow
        self.things[22] += merchant.blue
        self.things[23] += merchant.red

        if merchant.scroll:
            self.things[57] = merchant.scroll
        if merchant.property:
            self.attack += math.ceil(self.attack * merchant.property / 100)
            self.defense += math.floor(self.defense * merchant.property / 100)

        self.life += merchant.life

        if self.level in [2, 6, 7, 12, 15, 31, 38, 39, 45, 47]:
            args = np.argwhere(self.floor == 122)[0]
            self.clear(args)

    def action_altar(self, action):
        if action not in '123':
            return

        price = self.next_price()
        if self.coin < price:
            logger.info("no enough coin")
            return

        match action:
            case '1':
                self.life += ALTARS[self.level].life
            case '2':
                self.attack += ALTARS[self.level].attack
            case '3':
                self.defense += ALTARS[self.level].defense

        self.coin -= price
        self.price = price
        self.times += 1

    def action_normal(self, action, where):
        match action:
            case 'up':
                where = self.addoffset(self.where, (-1, 0))
            case 'down':
                where = self.addoffset(self.where, (1, 0))
            case 'left':
                where = self.addoffset(self.where, (0, -1))
            case 'right':
                where = self.addoffset(self.where, (0, 1))
            case action if action in 'qwertyuio':
                self.record(action)
                self.action_tool(action)
                return
            case 'move':
                where = tuple(where)
                if not self.route(where):
                    return
            case 'f' | 'pageup':
                args = np.argwhere(self.floor == 87)
                if len(args) == 0:
                    return
                where = tuple(args[0])
                if not any([
                    46 in self.things and self.level < self.max_level,
                    self.route(where),
                ]):
                    return
            case 'd' | 'pagedown':
                args = np.argwhere(self.floor == 88)
                if len(args) == 0:
                    return
                where = tuple(args[0])
                if not any([
                    46 in self.things and self.level > self.min_level,
                    self.route(where)
                ]):
                    return
            case _:
                return

        self.record(action, where)
        self.move(where)
        self.action_event(where)

    def message(self):
        match self.state:
            case c.STATE_NORMAL:
                content = (
                    f'L:{self.life}\n'
                    f'A:{self.attack}\n'
                    f'D:{self.defense}\n'
                    f'C:{self.coin}\n'
                    f'F:{self.level}\n'
                    f'{json.dumps(dict(sorted(self.things.items())), indent=4)}\n'
                )
            case c.STATE_ALTAR:
                if self.level not in ALTARS:
                    return ''
                content = (
                    f"你有 {self.coin} 个 金币，\n"
                    f"如果供奉 {self.next_price()} 金币，便可以：\n"
                    f"1: 生命 + {ALTARS[self.level].life}\n"
                    f"2: 攻击 + {ALTARS[self.level].attack}\n"
                    f"3: 防御 + {ALTARS[self.level].defense}\n"
                    "4: 离开"
                )
            case c.STATE_MERCHANT:
                merchant = MERCHANTS[self.level]
                content = f"你有 {self.coin} 个 金币，\n"
                if merchant.coin > 0:
                    content += f'我需要 {merchant.coin} 金币，给你：\n'
                elif merchant.coin < 0:
                    content += f'我给你 {abs(merchant.coin)} 金币，回收：\n'
                else:
                    content += f'我可你给你：\n'

                if merchant.yellow:
                    content += f'黄钥匙 {abs(merchant.yellow)} 把\n'
                if merchant.blue:
                    content += f'蓝钥匙 {abs(merchant.blue)} 把\n'
                if merchant.red:
                    content += f'红钥匙 {abs(merchant.red)} 把\n'
                if merchant.life:
                    content += f'生命值 {merchant.life}\n'
                if merchant.scroll:
                    content += f'地震卷轴 {merchant.scroll} 个\n'
                if merchant.property:
                    content += f'提升攻击和防御 {merchant.property} %\n'

                content += (
                    f"1: 成交\n"
                    f"2: 再见"
                )

        return content

    def execute(self, action, where=(0, 0)):
        match self.state:
            case c.STATE_NORMAL:
                self.action_normal(action, where)
            case c.STATE_ALTAR:
                self.record(action)
                self.action_altar(action)
                self.state = STATE_NORMAL
            case c.STATE_MERCHANT:
                self.record(action)
                self.action_merchant(action)
                self.state = STATE_NORMAL
        self.search()

    def check(self, where, value):
        if value in {21, 22, 23}:  # 钥匙
            return MASK.MASK_VALID1
        if value in {27, 28}:  # 宝石
            return MASK.MASK_VALID1
        if value in range(35, 45):  # 剑盾
            return MASK.MASK_VALID1
        if value in {87, 88}:  # 楼梯
            return MASK.MASK_VALID1
        if value in {81, 82, 83}:
            if GATEKEYS[value] not in self.things:
                return MASK.MASK_INVALID
            if self.things[GATEKEYS[value]] <= 0:
                return MASK.MASK_INVALID
            return MASK.MASK_VALID3
        if value in MONSTERS:
            harm = self.harmful(where, value)
            if harm < self.life:
                return MASK.MASK_VALID3

            return MASK.MASK_INVALID
        if value in {31, 32}:  # 药水
            return MASK.MASK_VALID3
        if value in {121, }:
            return MASK.MASK_EMPTY
        return MASK.MASK_UNKNOWN

    def search(self):
        queue = [tuple(self.where)]
        visited = set()

        while queue:
            pos = queue.pop(0)
            if pos in visited:
                continue
            visited.add(pos)
            self.mask[pos] = MASK.MASK_VISITED.value

            for near in self.nearby(pos):
                if near in visited:
                    continue

                value = self.floor[near]
                if value in {0, 2, 3}:
                    queue.append(near)
                    continue
                if value in {1, 85, 86}:
                    continue

                self.mask[near] = self.check(near, value).value


if __name__ == '__main__':
    import main
    window = main.Mota()
    window.show()
