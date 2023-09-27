
import os
import pickle
import json
from collections import namedtuple

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backend_bases
import matplotlib as mpl
import matplotlib.font_manager
import matplotlib.ft2font

from logger import logger
import maps
from attrs import *
import attrs


os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Mota(object):

    def read_resource(self, filename: str):
        if filename not in self.resources:
            img = plt.imread(filename)
            if img.shape[2] == 3:
                img = np.dstack((img, np.ones_like(img[:, :, 0])))
            self.resources[filename] = img

        return self.resources[filename]

    def read_ground(self):
        img = self.read_resource("materials/terrains.png")
        return img[0: 32, :32]

    def read_icon(self, filename: str, i: int):
        img = self.read_resource(filename)
        icon = img[i * 32: (i + 1) * 32, :32]
        alpha = np.expand_dims(icon[:, :, 3], 2)

        icon[:, :, :] = alpha * icon[:, :, :] + \
            (1 - alpha) * self.read_ground()

        return icon

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
        icons[330] = self.read_icon("materials/terrains.png", 45)

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

        # 铁剑
        icons[35] = self.read_icon("materials/items.png", 50)
        icons[36] = self.read_icon("materials/items.png", 55)
        icons[37] = self.read_icon("materials/items.png", 51)
        icons[38] = self.read_icon("materials/items.png", 56)
        icons[39] = self.read_icon("materials/items.png", 52)

        icons[41] = self.read_icon("materials/items.png", 53)
        icons[42] = self.read_icon("materials/items.png", 58)
        icons[43] = self.read_icon("materials/items.png", 54)
        icons[44] = self.read_icon("materials/items.png", 59)

        # 工具
        icons[46] = self.read_icon("materials/items.png", 12)
        icons[47] = self.read_icon("materials/items.png", 45)  # 锤子
        icons[49] = self.read_icon("materials/items.png", 43)  # 炸弹
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

    def plotmap(self):
        # logger.debug("plot map where %s", self.where)
        map = self.tower[self.level]

        canvas = np.zeros((32 * 13, 32 * 13, 4))
        for i in range(13):
            for j in range(13):
                if map[i, j] not in self.icons:
                    continue
                canvas[
                    i * 32: (i + 1) * 32,
                    j * 32: (j + 1) * 32
                ] = self.icons[map[i, j]]

        i, j = self.where

        canvas[
            i * 32: (i + 1) * 32,
            j * 32: (j + 1) * 32
        ] = self.icons[1000]

        self.img.set_data(canvas)
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

    def __init__(self) -> None:
        logger.info("mota creating...")
        self.resources = {}
        self.icons = self.load_icons()

        self.tower = np.copy(maps.M)
        self.level = 1
        self.max_level = 50
        self.min_level = 0
        self.where = np.array((11, 6))
        self.things = {}

        self.life = 1000
        self.attack = 100
        self.defense = 100
        self.coin = 0
        self.price = 20
        self.times = 0
        self.state = 0
        self.mode = MODE_ADD

        self.setup_matplotlib()

        self.fig = plt.figure(figsize=(7, 5))
        self.fig.tight_layout()
        self.fig.subplots_adjust(
            top=1, bottom=0, left=0,  right=1, hspace=0, wspace=0)

        gs = self.fig.add_gridspec(1, 7)

        self.ax = self.fig.add_subplot(gs[0:5])
        self.ax2 = self.fig.add_subplot(gs[5:])

        self.ax.axis("off")
        self.ax2.axis("off")

        self.img = self.ax.imshow(np.zeros((32 * 13, 32 * 13, 4)))

        self.fig.canvas.mpl_connect('key_press_event', self.key_press_event)
        # self.fig.canvas.mpl_connect('button_press_event', self.click_event)

        self.ax2.imshow(np.zeros((5, 2, 4)) + 0.3)
        self.label = self.ax2.text(0, 2.5, "")

        # self.load_state()
        self.plotmap()
        plt.show()

    @property
    def floor(self):
        return self.tower[self.level]

    def click_event(self, event):
        logger.debug(event)

    def update_state(self, state=None):
        if state is not None:
            (
                self.tower,
                self.level,
                self.min_level,
                self.max_level,
                self.where,
                self.things,
                self.life,
                self.attack,
                self.defense,
                self.coin,
                self.state,
                self.price,
                self.times,
                self.mode,
            ) = state
        else:
            return (
                self.tower,
                self.level,
                self.min_level,
                self.max_level,
                self.where,
                self.things,
                self.life,
                self.attack,
                self.defense,
                self.coin,
                self.state,
                self.price,
                self.times,
                self.mode,
            )

    def save_state(self):
        filename = 'state.pkl'
        logger.info("save state %s", filename)
        with open(filename, 'wb') as file:
            file.write(pickle.dumps(self.update_state()))

    def load_state(self):
        filename = 'state.pkl'
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

    def state_normal(self, event: matplotlib.backend_bases.KeyEvent):
        # logger.debug(event)
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
            case 'ctrl+s':
                self.save_state()
            case 'ctrl+l':
                self.load_state()
            case _:
                logger.info("key pressed %s", event.key)

        if where is None:
            return

        where += self.where
        spot = int(self.floor[tuple(where)])

        match spot:
            case attrs.WALL:
                logger.debug("wall...")
                return
            case attrs.EMPTY:
                self.where = where
            case spot if spot in range(20, 80):
                self.collect(where, spot)
            case spot if spot in range(81, 90):
                self.open(where, spot)
            case spot if spot in range(200, 260):
                self.battle(where, spot)
            case _:
                self.special(where, spot)

    def state_altar(self, event: matplotlib.backend_bases.KeyEvent):
        if event.key not in '123':
            self.state = STATE_NORMAL
            return
        if self.coin < self.next_price():
            logger.info("no enough coin")
            return

        match event.key:
            case '1':
                self.life += ALTARS[self.level].life
            case '2':
                self.attack += ALTARS[self.level].attack
            case '3':
                self.defense += ALTARS[self.level].defense
            case _:
                logger.info("key pressed %s", event.key)
                return

        self.state = STATE_NORMAL
        self.coin -= self.next_price()
        self.times += 1

    def state_merchant(self, event):
        if event.key != '1':
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

        if self.level in [7, ]:
            args = np.argwhere(self.floor == 122)[0]
            self.clear(args)

    def super_state(self, event: matplotlib.backend_bases.KeyEvent):
        match event.key.lower():
            case 'f' | 'pageup':
                if self.level >= self.max_level:
                    return True

                self.level += 1
                args = np.argwhere(self.floor == 88)
                if len(args) == 0:
                    args = np.argwhere(self.floor == 87)
                if len(args) == 0:
                    return True

                self.where = args[0]
                return True
            case 'd' | 'pagedown':
                if self.level <= self.min_level:
                    return True

                self.level -= 1
                args = np.argwhere(self.floor == 87)
                if len(args) == 0:
                    args = np.argwhere(self.floor == 88)
                if len(args) == 0:
                    return True
                self.where = args[0]
                return True
        return False

    def key_press_event(self, event: matplotlib.backend_bases.KeyEvent):
        if self.super_state(event):
            self.plotmap()
            return

        match self.state:
            case attrs.STATE_NORMAL:  # 正常
                self.state_normal(event)
            case attrs.STATE_ALTAR:  # 祭坛
                self.state_altar(event)
            case attrs.STATE_MERCHANT:
                self.state_merchant(event)

        self.plotmap()

    def clear(self, where):
        self.floor[tuple(where)] = 0
        self.where = where

    def special(self, where, spot):
        logger.info("%s %s", where, spot)
        match spot:
            case 3:  # 暗墙
                self.clear(where)
            case 126:  # 第三层特殊处理
                self.life = 400
                self.attack = 10
                self.defense = 10
                self.tower[2] = maps.S126[2]
                self.tower[3] = maps.S126[3]
                self.level = 2
                self.where = np.array([9, 1])
            case 121:  # 老头
                self.clear(where)
                self.things[121] = 1
            case 122:  # 商人
                self.state = STATE_MERCHANT
            case 131:  # 祭坛
                self.state = STATE_ALTAR
                # self.state_altar(None)

    def guard(self, where, monster):
        if monster not in (221, ):
            return

        args = np.argwhere(self.floor == monster)
        if len(args) > 0:
            return
        match (self.level, monster):
            case (8, 221):
                self.floor[4, 10] = 0

    def battle(self, where, monster):
        logger.debug("%s, %s", where, monster)
        if monster not in MONSTERS:
            return
        m = MONSTERS[monster]

        if m.defense >= self.attack:
            logger.debug("monster defense >= attack")
            return

        mlife = m.life
        wlife = self.life

        while True:
            harm = self.attack - m.defense
            mlife -= harm
            if mlife <= 0:
                break

            harm = m.attack - self.defense
            if harm > 0:
                wlife -= harm * self.mode
            if wlife <= 0:
                break

        if wlife <= 0:
            return

        self.life = wlife
        self.coin += m.coin
        self.clear(where)
        self.guard(where, monster)

    def open(self, where, gate):
        logger.debug(f'%s, %s\n', where, gate)
        match gate:
            case 87:  # 上楼
                self.level += 1
                self.max_level = max(self.max_level, self.level)
                self.where = np.argwhere(self.floor == 88)[0]
                return
            case 88:  # 下楼
                self.level -= 1
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
        logger.debug('collect %s', thing)
        self.clear(where)

        match thing:
            case 27:  # 红宝石
                self.attack += 1
            case 28:  # 蓝宝石
                self.defense += 1
            case 31:  # 红药水
                self.life += 50
            case 32:  # 蓝药水
                self.life += 200
            case 35:  # 铁剑
                self.attack += 10
            case 36:  # 铁盾
                self.defense += 10
            case _:
                self.things.setdefault(thing, 0)
                self.things[thing] += 1


if __name__ == '__main__':
    mota = Mota()
