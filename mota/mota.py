
import os
import re
import pickle
import json
import copy
from collections import namedtuple

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backend_bases
import matplotlib as mpl
import matplotlib.font_manager
import matplotlib.ft2font
from PIL import ImageDraw, Image, ImageFont

from logger import logger
import maps
from attrs import *
import attrs
import events

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Mota(object):

    def read_resource(self, filename: str) -> Image:
        if filename not in self.resources:
            img = Image.open(filename).convert("RGBA")
            self.resources[filename] = img
        return self.resources[filename]

    def read_ground(self):
        img = self.read_resource("materials/terrains.png")
        return img.crop((0, 0, 32, 32))

    def read_icon(self, filename: str, i: int):
        img = self.read_resource(filename)
        img = img.crop((0, i * 32, 32, (i + 1) * 32))
        return Image.alpha_composite(self.read_ground(), img)

    def load_icons(self):
        icons = {}

        # 地墙
        icons[0] = self.read_icon("materials/terrains.png", 0)
        icons[1] = self.read_icon("materials/terrains.png", 3)
        icons[2] = self.read_icon("materials/terrains.png", 4)
        icons[3] = self.read_icon("materials/terrains.png", 5)
        icons[4] = self.read_icon("materials/animates.png", 0)
        icons[5] = self.read_icon("materials/animates.png", 1)
        icons[7] = self.read_icon("materials/terrains.png", 31)
        icons[8] = self.read_icon("materials/terrains.png", 32)
        icons[320] = self.read_icon("materials/terrains.png", 12)
        icons[321] = self.read_icon("materials/terrains.png", 12)
        icons[330] = self.read_icon("materials/terrains.png", 45)
        icons[322] = self.read_icon("materials/terrains.png", 0)
        icons[323] = self.read_icon("materials/enemys.png", 7)
        icons[324] = self.read_icon("materials/terrains.png", 0)
        icons[325] = self.read_icon("materials/npcs.png", 2)

        # 宝石
        icons[27] = self.read_icon("materials/items.png", 16)
        icons[28] = self.read_icon("materials/items.png", 17)

        # 钥匙
        icons[21] = self.read_icon("materials/items.png", 0)
        icons[22] = self.read_icon("materials/items.png", 1)
        icons[23] = self.read_icon("materials/items.png", 2)
        icons[26] = self.read_icon("materials/items.png", 6)

        # 药水
        icons[31] = self.read_icon("materials/items.png", 20)
        icons[32] = self.read_icon("materials/items.png", 21)

        icons[35] = self.read_icon("materials/items.png", 50)  # 铁剑
        icons[36] = self.read_icon("materials/items.png", 55)  # 铁盾
        icons[37] = self.read_icon("materials/items.png", 51)  # 银剑
        icons[38] = self.read_icon("materials/items.png", 56)  # 银盾
        icons[39] = self.read_icon("materials/items.png", 52)  # 骑士剑
        icons[40] = self.read_icon("materials/items.png", 57)  # 骑士盾

        icons[41] = self.read_icon("materials/items.png", 53)
        icons[42] = self.read_icon("materials/items.png", 58)
        icons[43] = self.read_icon("materials/items.png", 54)
        icons[44] = self.read_icon("materials/items.png", 59)

        # 工具
        icons[46] = self.read_icon("materials/items.png", 12)
        icons[47] = self.read_icon("materials/items.png", 45)  # 锤子
        icons[49] = self.read_icon("materials/items.png", 43)  # 炸弹
        icons[50] = self.read_icon("materials/items.png", 13)  # 瞬移
        icons[51] = self.read_icon("materials/items.png", 15)  # 升华之翼

        # 道具
        icons[53] = self.read_icon("materials/items.png", 12)
        icons[54] = self.read_icon("materials/items.png", 41)  # 冰冻徽章

        icons[73] = self.read_icon("materials/items.png", 10)  # 记事本

        # 门
        icons[81] = self.read_icon("materials/terrains.png", 25)
        icons[82] = self.read_icon("materials/terrains.png", 26)
        icons[83] = self.read_icon("materials/terrains.png", 27)
        icons[85] = self.read_icon("materials/animates.png", 8)
        icons[86] = self.read_icon("materials/animates.png", 9)

        # 楼梯
        icons[87] = self.read_icon("materials/terrains.png", 24)
        icons[88] = self.read_icon("materials/terrains.png", 23)

        # NPC
        icons[121] = self.read_icon("materials/npcs.png", 0)
        icons[122] = self.read_icon("materials/npcs.png", 1)
        icons[123] = self.read_icon("materials/npcs.png", 2)
        icons[124] = self.read_icon("materials/npcs.png", 3)
        icons[125] = self.read_icon("materials/npcs.png", 4)
        icons[126] = self.read_icon("materials/enemys.png", 45)
        icons[127] = self.read_icon("materials/terrains.png", 0)
        icons[128] = self.read_icon("materials/enemys.png", 10)
        icons[129] = self.read_icon("materials/enemys.png", 57)
        icons[131] = self.read_icon("materials/npcs.png", 10)  # 商店
        icons[132] = self.read_icon("materials/npcs.png", 11)  # 公主

        # 大乌贼和魔龙的身体
        for i in range(16):
            icons[181 + i] = self.read_icon("materials/npcs.png", 12 + i)

        # 怪物
        for i in range(60):
            icons[201 + i] = self.read_icon("materials/enemys.png", i)

        icons[1000] = self.read_icon("materials/hero.png", 0)

        return icons

    def setup_matplotlib(self):
        mpl.rcParams['toolbar'] = 'None'

        for key in mpl.rcParams:
            if key.startswith("keymap"):
                mpl.rcParams[key] = []

        if os.name == 'nt':
            family = {
                "Simhei"
            }
        else:
            family = {
                "WenQuanYi Zen Hei",
            }

        fonts = matplotlib.font_manager.findSystemFonts(fontext='ttf')

        for fontfile in fonts:
            try:
                font = matplotlib.ft2font.FT2Font(fontfile)
                logger.debug("find font name %s", font.family_name)
                logger.debug("find path %s", fontfile)
            except Exception as e:
                continue

        mpl.rcParams['font.family'] = list(family)

    def plotharm(self, icon, where, idx):
        if idx not in MONSTERS:
            return icon

        harmful = self.harmful(where, idx)
        # logger.debug(harmful)
        text = Image.new("RGBA", (32, 32))
        draw = ImageDraw.Draw(text)
        draw.text((2, 22), str(harmful), fill='#000000cc',)
        draw.text((1, 21), str(harmful), fill='#db2828ff',)

        combined = Image.alpha_composite(icon, text)
        return combined

    def ploticon(self, where: tuple, idx: int, canvas: np.ndarray):
        if idx not in self.icons:
            return
        i, j = where
        icon = self.icons[idx]
        icon = self.plotharm(icon, where, idx)

        canvas.paste(icon, (j * 32, i * 32))

    def plotmap(self):
        canvas = Image.new("RGBA", (32 * 13, 32 * 13))
        for i in range(13):
            for j in range(13):
                if self.floor[(i, j)] not in self.icons:
                    continue
                self.ploticon((i, j), self.floor[(i, j)], canvas)

        self.ploticon(self.where, 1000, canvas)

        self.img.set_data(np.array(canvas))
        self.update_labels()

        self.fig.canvas.draw()

    def update_labels(self):
        match self.state:
            case attrs.STATE_NORMAL:
                content = (
                    f'L:{self.life}\n'
                    f'A:{self.attack}\n'
                    f'D:{self.defense}\n'
                    f'C:{self.coin}\n'
                    f'F:{self.level}\n'
                    f'{json.dumps(self.things, indent=4)}\n'
                )
            case attrs.STATE_ALTAR:
                content = (
                    f"如果供奉 {self.next_price()} 金币，便可以：\n"
                    f"1: 生命 + {ALTARS[self.level].life}\n"
                    f"2: 攻击 + {ALTARS[self.level].attack}\n"
                    f"3: 防御 + {ALTARS[self.level].defense}\n"
                    "4: 离开"
                )
            case attrs.STATE_MERCHANT:
                merchant = MERCHANTS[self.level]
                content = (
                    f"我需要 {merchant.coin} 金币，给你：\n"
                )

                if merchant.yellow:
                    content += f'黄钥匙 {merchant.yellow} 把\n'
                if merchant.blue:
                    content += f'蓝钥匙 {merchant.blue} 把\n'
                if merchant.red:
                    content += f'红钥匙 {merchant.red} 把\n'
                if merchant.life:
                    content += f'生命值 {merchant.yellow}\n'

                content += (
                    f"1: 买之\n"
                    f"2: 不买\n"
                )

        # logger.debug("update label %s", content)
        self.label.set_text(content)

    def next_price(self):
        return self.price + self.times * 20

    def init_state(self, actions=None):
        self.tower = np.copy(maps.M)
        self.level = 1
        self.max_level = 50
        self.min_level = 0
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

        if actions is not None:
            for action in actions:
                self.action(action)
            self.actions = actions

    def __init__(self) -> None:
        logger.info("mota creating...")
        self.resources = {}
        self.icons = self.load_icons()
        self.init_state()

        self.setup_matplotlib()

        self.fig = plt.figure(figsize=(8, 5))
        self.fig.tight_layout()
        self.fig.subplots_adjust(
            top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)

        gs = self.fig.add_gridspec(1, 8)

        self.ax = self.fig.add_subplot(gs[0:5])
        self.ax2 = self.fig.add_subplot(gs[5:])

        self.ax.axis("off")
        self.ax2.axis("off")

        self.img = self.ax.imshow(np.zeros((32 * 13, 32 * 13, 4)))

        self.fig.canvas.mpl_connect('key_press_event', self.key_press_event)
        self.fig.canvas.mpl_connect('button_press_event', self.click_event)

        self.ax2.imshow(np.zeros((5, 3, 4)) + 0.3)
        self.label = self.ax2.text(0, 2.5, "")

        # self.load_state()
        self.plotmap()
        plt.show()

    @property
    def floor(self):
        return self.tower[self.level]

    def route(self, to: np.ndarray):
        to = tuple(to)
        wheres = [tuple(self.where)]
        visited = set()
        offsets = np.array([
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ])

        while wheres:
            pos = wheres.pop(0)
            if pos == to:
                # logger.info("find route from %s to %s", tuple(self.where), to)
                return True
            if pos in visited:
                continue
            visited.add(pos)
            for offset in offsets:
                near = tuple(np.array(pos) + offset)
                if near == to:
                    wheres.append(near)
                    break

                if near in visited:
                    continue

                if self.floor[near] != 0:
                    continue
                wheres.append(near)

        return False

    def click_event(self, event: matplotlib.backend_bases.MouseEvent):
        if event.inaxes != self.ax:
            return
        if self.state != attrs.STATE_NORMAL:
            return
        logger.debug(event)
        data = np.array([event.ydata, event.xdata]) // 32
        data = data.astype(np.int32)
        logger.debug("click location %s %s", data, self.floor[tuple(data)])
        if self.route(data):
            self.actions.append((self.state, data))
            self.action_normal(data)

        self.plotmap()

    def update_state(self, state=None):
        if state is not None:
            (
                actions,
            ) = state
            self.init_state(actions)
        else:
            return (
                self.actions,
            )

    def save_state(self, filename='state.pkl'):
        logger.info("save state %s", filename)
        with open(filename, 'wb') as file:
            file.write(pickle.dumps(self.update_state()))

    def load_state(self, filename='state.pkl'):
        if not os.path.exists(filename):
            return

        logger.info("load state %s", filename)
        with open(filename, 'rb') as file:
            state = pickle.loads(file.read())
        try:
            self.update_state(state)
        except Exception:
            return

        self.plotmap()

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
                if self.floor[where] != value:
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
                    self.floor[key] = value
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
        # logger.debug("%s %s", where, self.floor[where])
        if self.level not in self.events:
            return

        items = self.events[self.level]

        for e in items[:]:
            if not self.match_event(e.match, where):
                continue
            self.action_change(e.change)

            e.times -= 1
            # logger.debug(e.times)
            if e.times == 0:
                items.remove(e)
                # logger.debug(items)

    def action_normal(self, where):
        if isinstance(where, str):
            return self.action_tool(where)

        spot = int(self.floor[tuple(where)])

        match spot:
            case attrs.WALL:
                # logger.debug("wall...")
                return
            case attrs.EMPTY:
                self.where = where
            case spot if spot in range(20, 80):
                self.collect(where, spot)
            case spot if spot in range(81, 90):
                self.open(where, spot)
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
            # case _:
                # self.special(where, spot)
        self.action_event(where)

    def action_tool(self, tool):
        match tool:
            case 'q':  # 瞬移
                if 50 not in self.things:
                    return
                if self.things[50] <= 0:
                    return
                where = np.array([-6, -6]) + self.where
                where = np.array([6, 6]) - where
                logger.debug('fly to %s', where)
                if self.floor[tuple(where)] == 0:
                    self.where = where
                    self.things[50] -= 1
                if self.things[50] == 0:
                    del self.things[50]
            case 'w':  # 破墙镐
                if 47 not in self.things:
                    return
                if self.things[47] <= 0:
                    return
                for offset in np.array([[1, 0], [-1, 0], [0, 1], [0, -1]]):
                    where = self.where + offset
                    if set(where) & {0, 12}:
                        continue
                    if self.floor[tuple(where)] != 1:
                        continue
                    self.floor[tuple(where)] = 0
                    self.things[47] = 0
                if self.things[47] == 0:
                    del self.things[47]

        # logger.debug(tool)

    def key_normal(self, event: matplotlib.backend_bases.KeyEvent):
        # logger.debug(event)
        match = re.match(r'(ctrl|alt)\+(\d)', event.key)
        if match:
            match match.group(1):
                case 'ctrl':
                    self.save_state(filename=f'state.{match.group(2)}.pkl')
                case 'alt':
                    self.load_state(filename=f'state.{match.group(2)}.pkl')
            logger.debug("save state %s", match.group(2))
            return

        where = None
        match event.key:
            case 'up':
                where = np.array([-1, 0])
            case 'down':
                where = np.array([1, 0])
            case 'left':
                where = np.array([0, -1])
            case 'right':
                where = np.array([0, 1])
            case 'f' | 'pageup':
                args = np.argwhere(self.floor == 87)
                if len(args) == 0:
                    return
                where = tuple(args[0])
                if self.route(where):
                    self.actions.append((self.state, where))
                    self.action_normal(where)
                return
            case 'd' | 'pagedown':
                args = np.argwhere(self.floor == 88)
                if len(args) == 0:
                    return
                where = tuple(args[0])
                if self.route(where):
                    self.actions.append((self.state, where))
                    self.action_normal(where)
                return
            case 'q' | 'w':
                self.actions.append((self.state, event.key))
                self.action_normal(event.key)
            case 'ctrl+s':
                self.save_state()
            case 'ctrl+l':
                self.load_state()
            case 'ctrl+n':
                self.init_state()
            case _:
                # logger.info("key pressed %s", event.key)
                ...

        if where is None:
            return

        where += self.where

        self.actions.append((self.state, where))
        self.action_normal(where)

    def key_altar(self, event: matplotlib.backend_bases.KeyEvent):
        self.actions.append((self.state, event.key))
        self.action_altar(event.key)

    def action_altar(self, param):
        if param not in '123':
            self.state = STATE_NORMAL
            return
        if self.coin < self.next_price():
            logger.info("no enough coin")
            return

        match param:
            case '1':
                self.life += ALTARS[self.level].life
            case '2':
                self.attack += ALTARS[self.level].attack
            case '3':
                self.defense += ALTARS[self.level].defense
            case _:
                logger.info("key pressed %s", param)
                return

        self.state = STATE_NORMAL
        self.coin -= self.next_price()
        self.times += 1

    def key_merchant(self, event):
        self.actions.append((self.state, event.key))
        self.action_merchant(event.key)

    def action_merchant(self, param):
        if param != '1':
            self.state = STATE_NORMAL
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

        self.life += merchant.life

        if self.level in [6, 7, 12, 15, 31, 38, 39]:
            args = np.argwhere(self.floor == 122)[0]
            self.clear(args)

        self.state = STATE_NORMAL

    def action(self, act):
        state, param = act
        if self.state != state:
            logger.error("state error %s != %s", self.state, state)

        match state:
            case attrs.STATE_NORMAL:
                self.action_normal(param)
            case attrs.STATE_ALTAR:
                self.action_altar(param)
            case attrs.STATE_MERCHANT:
                self.action_merchant(param)

    def key_press_event(self, event: matplotlib.backend_bases.KeyEvent):
        # logger.debug(event.key)
        match self.state:
            case attrs.STATE_NORMAL:  # 正常
                self.key_normal(event)
            case attrs.STATE_ALTAR:  # 祭坛
                self.key_altar(event)
            case attrs.STATE_MERCHANT:
                self.key_merchant(event)

        self.update_special()
        self.plotmap()

    def clear(self, where):
        self.floor[tuple(where)] = 0
        self.where = where

    def harmful(self, where, monster):
        if monster not in MONSTERS:
            return -1

        m = MONSTERS[monster]

        attack = self.attack
        if monster in (208, 213, 214) and 321 in self.things:  # 十字架
            attack *= 2

        specials = {}
        special = 0

        if self.level in self.special:
            specials = self.special[self.level]

        where = tuple(where)
        if where in specials:
            special = specials[where]
            logger.debug(
                'special %s %s %s %s',
                self.level, where, special, specials)

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

    def battle(self, where, monster):
        # logger.debug("%s, %s", where, monster)
        wlife = self.harmful(where, monster)
        if wlife < 0:
            return False

        life = self.life - wlife * self.mode
        if life <= 0:
            return False

        m = MONSTERS[monster]
        self.life = life
        self.coin += m.coin
        self.clear(where)

        where = tuple(where)
        if where in self.special:
            del self.special[where]
        # self.guard(where, monster)
        return True

    def open(self, where, gate):
        # logger.debug(f'open %s, %s', where, gate)
        match gate:
            case 87:  # 上楼
                self.level += 1

                if self.level == 44:
                    self.level = 45

                self.max_level = max(self.max_level, self.level)
                self.where = np.argwhere(self.floor == 88)[0]
                return
            case 88:  # 下楼
                self.level -= 1
                if self.level == 44:
                    self.level = 43

                self.min_level = min(self.min_level, self.level)
                self.where = np.argwhere(self.floor == 87)[0]
                return

        if gate not in GATEKEYS:
            return

        key = GATEKEYS[gate]
        if key not in self.things:
            return
        if self.things[key] == 0:
            logger.debug("no key %s", key)
            return

        self.things[key] -= 1
        self.clear(where)

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
            case 28:  # 蓝宝石
                if self.level <= 10:
                    self.defense += 1
                elif self.level <= 20:
                    self.defense += 2
                elif self.level <= 40:
                    self.defense += 4
            case 31:  # 红药水
                if self.level <= 10:
                    self.life += 50
                elif self.level <= 20:
                    self.life += 100
                else:
                    self.life += 200
            case 32:  # 蓝药水
                if self.level <= 10:
                    self.life += 200
                elif self.level <= 20:
                    self.life += 400
                else:
                    self.life += 800
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
            case 50:  # 瞬移
                self.things[50] = 3
            case _:
                self.things.setdefault(thing, 0)
                self.things[thing] += 1

    def update_special(self):
        pass


if __name__ == '__main__':
    mota = Mota()
