
import os
import re
import pickle
import json
import copy
import math
import shutil
import itertools

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
from const import *
import const as c
import events
import game

dirname = os.path.dirname(os.path.abspath(__file__))


class Mota(object):

    def read_resource(self, filename: str) -> Image:
        filename = os.path.join(dirname, 'materials', filename)
        if filename not in self.resources:
            img = Image.open(filename).convert("RGBA")
            self.resources[filename] = img
        return self.resources[filename]

    def read_icon(self, filename: str, i: int):
        img = self.read_resource(filename)
        icon = img.crop((0, i * 32, 32, (i + 1) * 32))
        return icon

    def load_icons(self):
        icons = {}

        # 地墙
        icons[0] = self.read_icon("terrains.png", 0)
        icons[1] = self.read_icon("terrains.png", 3)
        icons[2] = self.read_icon("terrains.png", 4)
        icons[3] = self.read_icon("terrains.png", 5)
        icons[4] = self.read_icon("animates.png", 0)
        icons[5] = self.read_icon("animates.png", 1)
        icons[7] = self.read_icon("terrains.png", 31)
        icons[8] = self.read_icon("terrains.png", 32)
        icons[320] = self.read_icon("terrains.png", 12)
        icons[321] = self.read_icon("terrains.png", 12)
        icons[330] = self.read_icon("terrains.png", 45)
        icons[322] = self.read_icon("terrains.png", 0)
        icons[324] = self.read_icon("terrains.png", 3)

        # 宝石
        icons[27] = self.read_icon("items.png", 16)
        icons[28] = self.read_icon("items.png", 17)

        # 钥匙
        icons[21] = self.read_icon("items.png", 0)
        icons[22] = self.read_icon("items.png", 1)
        icons[23] = self.read_icon("items.png", 2)
        icons[26] = self.read_icon("items.png", 6)

        # 药水
        icons[31] = self.read_icon("items.png", 20)
        icons[32] = self.read_icon("items.png", 21)

        icons[35] = self.read_icon("items.png", 50)  # 铁剑
        icons[36] = self.read_icon("items.png", 55)  # 铁盾
        icons[37] = self.read_icon("items.png", 51)  # 银剑
        icons[38] = self.read_icon("items.png", 56)  # 银盾
        icons[39] = self.read_icon("items.png", 52)  # 骑士剑
        icons[40] = self.read_icon("items.png", 57)  # 骑士盾

        icons[41] = self.read_icon("items.png", 53)
        icons[42] = self.read_icon("items.png", 58)
        icons[43] = self.read_icon("items.png", 54)
        icons[44] = self.read_icon("items.png", 59)
        icons[45] = self.read_icon("items.png", 9)  # 怪物手册

        # 工具
        icons[46] = self.read_icon("items.png", 12)  # 飞行器
        icons[47] = self.read_icon("items.png", 45)  # 锤子
        icons[49] = self.read_icon("items.png", 43)  # 炸弹
        icons[50] = self.read_icon("items.png", 13)  # 瞬移
        icons[51] = self.read_icon("items.png", 15)  # 升华之翼

        # 道具
        icons[52] = self.read_icon("items.png", 14)  # 下楼器
        icons[53] = self.read_icon("items.png", 11)  # 幸运金币
        icons[54] = self.read_icon("items.png", 41)  # 冰冻徽章
        icons[55] = self.read_icon("items.png", 40)  # 十字架
        icons[56] = self.read_icon("items.png", 29)  # 圣水
        icons[57] = self.read_icon("items.png", 8)  # 地震卷轴
        icons[62] = self.read_icon("items.png", 42)  # 屠龙匕

        icons[73] = self.read_icon("items.png", 10)  # 记事本

        # 门
        icons[81] = self.read_icon("terrains.png", 25)
        icons[82] = self.read_icon("terrains.png", 26)
        icons[83] = self.read_icon("terrains.png", 27)
        icons[85] = self.read_icon("animates.png", 8)
        icons[86] = self.read_icon("animates.png", 9)

        # 楼梯
        icons[87] = self.read_icon("terrains.png", 24)
        icons[88] = self.read_icon("terrains.png", 23)

        # NPC
        icons[121] = self.read_icon("npcs.png", 0)
        icons[122] = self.read_icon("npcs.png", 1)
        icons[123] = self.read_icon("npcs.png", 2)
        icons[124] = self.read_icon("npcs.png", 3)
        icons[125] = self.read_icon("npcs.png", 4)
        icons[126] = self.read_icon("enemys.png", 45)
        icons[127] = self.read_icon("terrains.png", 0)
        icons[128] = self.read_icon("enemys.png", 10)
        icons[129] = self.read_icon("enemys.png", 57)
        icons[131] = self.read_icon("npcs.png", 10)  # 商店
        icons[132] = self.read_icon("npcs.png", 11)  # 公主

        # 大乌贼和魔龙的身体
        for i in range(16):
            icons[181 + i] = self.read_icon("npcs.png", 12 + i)

        # 怪物
        for i in range(60):
            icons[201 + i] = self.read_icon("enemys.png", i)

        icons[1000] = self.read_icon("hero.png", 0)  # 人
        icons[1001] = self.read_icon("icons.png", 0)  # 楼梯
        icons[1002] = self.read_icon("icons.png", 3)  # ♥
        icons[1003] = self.read_icon("icons.png", 4)  # 攻击
        icons[1004] = self.read_icon("icons.png", 5)  # 防御
        icons[1005] = self.read_icon("icons.png", 7)  # 金币

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
        mpl.rcParams['font.family'] = list(family)
        fonts = matplotlib.font_manager.findSystemFonts(fontext='ttf')

        for fontfile in fonts:
            try:
                font = matplotlib.ft2font.FT2Font(fontfile)
                logger.debug("find font name %s", font.family_name)
                logger.debug("find path %s", fontfile)
            except Exception as e:
                continue

    def create_image(self):
        img = Image.new("RGBA", (32 * 18, 32 * 13))
        return img

    def create_background(self):
        img = self.create_image()
        icon = self.icons[0]
        for i, j in itertools.product(range(13), range(18)):
            img.paste(icon, (j * 32, i * 32))
        return img

    def plotharm(self, where, idx, canvas):
        if idx not in MONSTERS:
            return

        harmful = self.game.harmful(where, idx)
        # logger.debug(harmful)
        text = Image.new("RGBA", (32, 32))
        draw = ImageDraw.Draw(text)
        draw.text((2, 22), str(harmful), fill='#000000cc',)
        draw.text((1, 21), str(harmful), fill='#db2828ff',)
        self.paste_icon(canvas, text, where)

    def plotdomain(self, where, idx, canvas):
        total = self.game.domainful(where)
        if total <= 0:
            return

        text = Image.new("RGBA", (32, 32))
        draw = ImageDraw.Draw(text)
        draw.text((2, 12), str(total), fill='#000000cc',)
        draw.text((1, 11), str(total), fill='#fbbd08ff',)
        self.paste_icon(canvas, text, where)

    def plotmask(self, where, idx, canvas):
        mask = self.game.mask[where]
        if not mask:
            return

        outlines = {
            MASK.MASK_UNKNOWN.value: '#a333c8',
            MASK.MASK_INVALID.value: '#db2828',
            MASK.MASK_VISITED.value: '#82a0b9',
            MASK.MASK_VALID1.value: '#21ba45',
            MASK.MASK_VALID2.value: '#a7bd0d',
            MASK.MASK_VALID3.value: '#2185d0',
        }
        outline = outlines.get(mask, '#82a0b9')

        icon = Image.new("RGBA", (32, 32))
        draw = ImageDraw.Draw(icon)
        draw.rectangle((0, 0, 31, 31), outline=outline, width=1)
        self.paste_icon(canvas, icon, where)

    def paste_icon(self, canvas, icon, where):
        i, j = where
        canvas.paste(icon, (j * 32, i * 32))

    def plottext(self, canvas, text, where, height=1):
        icon = Image.new("RGBA", (32 * 5, 32 * height))
        draw = ImageDraw.Draw(icon)
        font = ImageFont.truetype('simhei.ttf', 12)
        # draw.rectangle((2, 10, 30, 20), fill='#00000077')
        draw.text((4, 11), str(text), fill='#2185d0', font=font,
                  stroke_width=2,
                  stroke_fill="#ffffffcc")
        self.paste_icon(canvas, icon, (where))

    def plotmessage(self, canvas, message):
        self.plottext(canvas, message, (0, 13), height=13)

    def plotinfo(self, canvas, text):
        if self.game.state != game.STATE_NORMAL:
            self.plottext(canvas, self.game.message(), (0, 13), height=13)
            return

        self.paste_icon(canvas, self.icons[1001], (0, 13))
        self.plottext(text, self.game.level, (0, 13))

        self.paste_icon(canvas, self.icons[1002], (1, 13))
        self.plottext(text, self.game.life, (1, 13))

        self.paste_icon(canvas, self.icons[1003], (2, 13))
        self.plottext(text, self.game.attack, (2, 13))

        self.paste_icon(canvas, self.icons[1004], (3, 13))
        self.plottext(text, self.game.defense, (3, 13))

        self.paste_icon(canvas, self.icons[1005], (4, 13))
        self.plottext(text, self.game.coin, (4, 13))

        idx = 0
        for var in (21, 22, 23):
            self.paste_icon(canvas, self.icons[var], (idx, 14))
            self.plottext(text, self.game.things.get(var, 0), (idx, 14))
            idx += 1

        idx = 0
        for var in self.game.things:
            if var in (21, 22, 23):
                continue
            if var not in self.icons:
                continue
            self.paste_icon(canvas, self.icons[var], (idx, 15))
            info = ''
            if var in TOOLKEYS:
                info = TOOLKEYS[var]

            count = self.game.things.get(var, 0)
            if count > 1:
                info += f' {count}'

            if info:
                self.plottext(text, info, (idx, 15))
            idx += 1

    def update(self, game: game.Game = None, message=None):
        if game is None:
            game = self.game

        canvas = self.create_image()
        domain = self.create_image()
        mask = self.create_image()

        for i, j in itertools.product(range(13), range(13)):
            idx = game.floor[i, j]
            if idx not in self.icons:
                logger.warning("no icon %s", idx)
                continue
            icon = self.icons[idx]
            self.paste_icon(canvas, icon, (i, j))
            self.plotharm((i, j), idx, domain)
            self.plotdomain((i, j), idx, domain)
            self.plotmask((i, j), idx, mask)

        if message is not None:
            self.plotmessage(canvas, message)
        else:
            self.plotinfo(canvas, domain)

        hero = self.create_image()
        self.paste_icon(hero, self.icons[1000], game.where)

        out = Image.alpha_composite(self.background, canvas)
        out = Image.alpha_composite(out, hero)
        out = Image.alpha_composite(out, domain)
        out = Image.alpha_composite(out, mask)
        self.img.set_data(out)
        self.fig.canvas.draw()
    #     return combined

    def __init__(self) -> None:
        logger.info("mota creating...")
        self.resources = {}
        self.icons = self.load_icons()
        self.game = game.Game()
        self.stack = []
        self.setup_matplotlib()

        self.fig = plt.figure(figsize=(18, 13))
        self.fig.tight_layout()
        self.fig.subplots_adjust(
            top=1,
            bottom=0,
            left=0,
            right=1,
        )

        self.ax = self.fig.add_subplot()

        self.ax.axis("off")

        self.background = self.create_background()

        self.img = self.ax.imshow(self.background)

        self.fig.canvas.mpl_connect('key_press_event', self.key_press_event)
        self.fig.canvas.mpl_connect('button_press_event', self.click_event)
        self.fig.canvas.manager.set_window_title('Mota')

        self.update(self.game)

    def show(self):
        plt.show()

    def execute(self, action, where=(0, 0)):
        state = self.game.state
        self.stack.append(copy.deepcopy(self.game))
        logger.debug(self.stack)
        self.game.execute(action, where)
        if state != self.game.state:
            logger.info(self.game.message())
        self.update()

    def click_event(self, event: matplotlib.backend_bases.MouseEvent):
        # logger.debug(event)
        try:
            data = np.array([event.ydata, event.xdata]) // 32
        except Exception:
            return
        data = data.astype(np.int32)
        logger.debug("click location %s", data)
        self.execute('move', data)

    def validate(self, key):
        if key in {
            'ctrl+s',
            'ctrl+l',
            'ctrl+n',
            'ctrl+z',
            'up',
            'down',
            'left',
            'right',
            'pageup',
            'pagedown',
        }:
            return True
        if key in 'qwertyuiofdvs1234':
            return True
        return False

    def key_press_event(self, event: matplotlib.backend_bases.KeyEvent):
        # logger.debug(event.key)
        if not self.validate(event.key):
            return

        match event.key:
            case 'ctrl+s':
                self.game.save_state()
                self.update(message="状态已保存")
                return
            case 'ctrl+l':
                self.game.load_state()
                self.update(message="状态已加载")
                return
            case 'ctrl+n':
                self.game.reset()
                self.update(message="状态已重置")
            case 'ctrl+z':
                if self.stack:
                    logger.debug("ctrl + z")
                    self.game = self.stack.pop()
                    self.update()
            case 'v':
                logger.info(self.game.message())
            case 's':
                game = copy.deepcopy(self.game)
                if self.game.search(execute=True):
                    self.stack.append(game)
            case _:
                self.execute(event.key)

        self.update()


if __name__ == '__main__':
    mota = Mota()
    mota.show()
