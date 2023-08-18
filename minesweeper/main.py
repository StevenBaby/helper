import sys
import os
import time
import threading
import queue
import random

from PySide6.QtCore import (
    Qt, QRect
)
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
)
from PySide6.QtGui import (
    QGuiApplication,
    QPixmap,
    QImage,
    QMouseEvent,
    QKeyEvent,
    QPainter,
)

import mss
import torch

import cv2
import numpy as np
import tone
import matplotlib.pyplot as plt
import pyautogui

from logger import logger

dirname = os.path.dirname(os.path.abspath(__file__))
device = tone.utils.learning.try_use_device()


class Line(QLabel):

    def __init__(self, parent=None, pos=100, vertical=True):
        super().__init__(parent=parent)
        self.setStyleSheet("background-color: rgba(0, 255, 0, 50)")
        self.show()
        self.vertical = vertical
        self.w = 10
        if vertical:
            self.setGeometry(QRect(pos, 0, self.w, self.screen().geometry().height()))
        else:
            self.setGeometry(QRect(0, pos, self.screen().geometry().width(), self.w))

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        p = event.position()
        gp = self.mapToParent(p)
        logger.debug(gp)
        if self.vertical:
            self.move(gp.x(), 0)
        else:
            self.move(0, gp.y())
        return super().mouseMoveEvent(event)


class Signal(QtCore.QObject):

    enter = QtCore.Signal(None)
    right = QtCore.Signal(object)
    click = QtCore.Signal(object)


class MainWindow(QMainWindow):

    def show_board(self):
        self.label.setPixmap(self.screenshot())
        self.label.setGeometry(self.board_rect())
        self.label.setVisible(True)
        self.label.setText("")

    def show_coordinate(self):
        pixmap = self.screenshot()
        image = pixmap.toImage()
        image = np.array(image.bits()).reshape(image.height(), image.width(), 4)

        w = pixmap.width() / 30
        h = pixmap.height() / 16
        for i in range(16):
            for j in range(30):
                x = int(w * j + 10)
                y = int(h * i + 40)
                cv2.putText(img=image,
                            text=f"{i},{j}",
                            org=(x, y),
                            fontFace=cv2.FONT_HERSHEY_DUPLEX,
                            fontScale=0.6,
                            color=(255, 0, 0, 255),
                            thickness=2)

        height, width, channel = image.shape
        bytesperline = channel * width
        pixmap = QPixmap(
            QImage(
                image.data,
                width, height,
                bytesperline,
                QImage.Format.Format_RGBA8888
            ).rgbSwapped()
        )

        self.label.setPixmap(pixmap)
        self.label.setGeometry(self.board_rect())
        self.label.setVisible(True)
        self.label.setText("")

    def show_situation(self, board):
        pixmap = self.screenshot()
        image = pixmap.toImage()
        image = np.array(image.bits()).reshape(image.height(), image.width(), 4)

        w = pixmap.width() / 30
        h = pixmap.height() / 16

        for i, line in enumerate(board):
            for j, value in enumerate(line):
                x = int(w * j + 20)
                y = int(h * i + 40)
                cv2.putText(img=image,
                            text=str(value),
                            org=(x, y),
                            fontFace=cv2.FONT_HERSHEY_DUPLEX,
                            fontScale=1,
                            color=(255, 0, 0, 255),
                            thickness=2)

        height, width, channel = image.shape
        bytesperline = channel * width
        pixmap = QPixmap(
            QImage(
                image.data,
                width, height,
                bytesperline,
                QImage.Format.Format_RGBA8888
            ).rgbSwapped()
        )

        self.label.setPixmap(pixmap)
        self.label.setGeometry(self.board_rect())
        self.label.setVisible(True)
        self.label.setText("")

    def situation(self, pixmap: QPixmap = None):
        if pixmap is None:
            pixmap = self.screenshot()
        image = pixmap.toImage()
        image = np.array(image.bits()).reshape(image.height(), image.width(), 4)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]

        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        if self.classifier is None:
            self.classifier = self.load_classifier()

        rects = []
        for c in cnts:
            rect = cv2.boundingRect(c)
            x, y, w, h = rect
            if w < 5:
                continue
            if h < 5:
                continue
            rects.append(rect)

        if len(rects) != 480:
            self.error = True
            logger.error("recognize board error")
            return

        result = sorted(rects, key=lambda e: e[1])
        lines = [
            result[i * 30: (i + 1) * 30]
            for i in range(16)
        ]
        result = []
        for line in lines:
            result.append(sorted(line, key=lambda e: e[0]))

        inputs = []
        for j in range(16):
            for i in range(30):
                x, y, w, h = result[j][i]

                dice = image[y:y + h, x:x + w]
                dice = cv2.resize(dice, (64, 64))

                input = cv2.cvtColor(dice, cv2.COLOR_BGR2GRAY)
                input = torch.from_numpy(input).float().to(device) / 255.0
                input = input.unsqueeze(0)
                inputs.append(input)

        input = torch.stack(inputs)
        # logger.debug(input.shape)
        output = self.classifier.predict(input)
        board = output.cpu().numpy().reshape(16, 30)
        # logger.debug(f"\n{board}")
        return board

    def screenshot(self):
        # reference
        # https://doc.qt.io/qtforpython-6/examples/example_widgets_desktop_screenshot.html
        screen = QGuiApplication.screens()[1]
        window = self.windowHandle()
        if window:
            screen = self.screen()
        if not screen:
            return

        # logger.debug(screen)

        rect = self.board_rect()
        if rect.width() == 0:
            return
        if rect.height() == 0:
            return

        if self.screen() == QGuiApplication.screens()[0]:
            pixmap = screen.grabWindow(0, rect.x(), rect.y(), rect.width(), rect.height())
            return pixmap

        with mss.mss() as sct:
            left = sct.monitors[1]['width']
            num = 2

            # logger.debug(sct.monitors)
            monitor = {
                "left": left + rect.x(),
                "top": rect.y(),
                "width": rect.width(),
                "height": rect.height(),
                "mon": num,
            }
            # logger.debug(monitor)

            img = sct.grab(monitor)
            img = np.array(img)
            # cv2.imshow('aaa', img)
            # logger.debug((img, img.shape))

        height, width, channel = img.shape
        bytesperline = channel * width
        pixmap = QPixmap(
            QImage(
                img.data,
                width, height,
                bytesperline,
                QImage.Format.Format_RGBA8888
            ).rgbSwapped()
        )
        return pixmap

    def board_rect(self):
        xs = (self.vlines[0].x(), self.vlines[1].x())
        ys = (self.hlines[0].y(), self.hlines[1].y())
        x0 = min(xs) + self.vlines[0].w
        x1 = max(xs)
        y0 = min(ys) + self.vlines[0].w
        y1 = max(ys)
        rect = QRect(x0, y0, x1 - x0, y1 - y0)
        # logger.debug((xs, ys))
        return rect

    def get_sournd(self, y, x):
        wheres = [
            (y - 1, x - 1),
            (y - 1, x + 1),
            (y, x - 1),
            (y, x + 1),
            (y + 1, x - 1),
            (y + 1, x + 1),
            (y - 1, x),
            (y + 1, x),
        ]
        result = []
        for y, x in wheres:
            if x < 0 or x >= 30:
                continue
            if y < 0 or y >= 16:
                continue
            result.append((y, x))
        return result

    def get_possible(self, y, x, board: np.ndarray):
        wheres = self.get_sournd(y, x)
        result = []
        for where in wheres:
            if board[where] == 9:
                result.append(where)
        return result

    def get_mines(self, y, x, board: np.ndarray):
        wheres = self.get_sournd(y, x)
        result = []
        for where in wheres:
            if board[where] == 10:
                result.append(where)
        return result

    def solve_board(self, board: np.ndarray):
        place = np.zeros_like(board)
        marks = board.copy()
        remain = board.copy()

        possibles = []

        for y, line in enumerate(board):
            for x, value in enumerate(line):
                mines = self.get_mines(y, x, board)
                if len(mines) > board[(y, x)]:
                    logger.error(f"error of mines {(y, x)} {mines}")
                    continue

                possible = self.get_possible(y, x, board)
                place[(y, x)] = len(possible) + len(mines)
                if board[(y, x)] > 8:
                    continue

                possibles.append((set(possible), (y, x)))
                remain[(y, x)] = board[(y, x)] - len(mines)

        for p0, w0 in possibles:
            if board[w0] > 8:
                continue
            for p1, w1 in possibles:
                if board[w1] > 8:
                    continue
                a, b, c, d = (p0, p1, w0, w1) if len(p0) > len(p1) else (p1, p0, w1, w0)
                if not b.issubset(a):
                    continue

                sub = a - b
                if len(sub) == 0:
                    continue

                count = remain[c] - remain[d]
                if count < 0:
                    continue

                if count == 0:
                    for where in sub:
                        marks[where] = 14
                elif len(sub) == count:
                    for where in sub:
                        marks[where] = 10

        return marks

    def move_to_pos(self, y, x):
        with mss.mss() as sct:
            if self.screen() == QGuiApplication.screens()[0]:
                left = 0
            else:
                left = sct.monitors[1]['width']

        rect = self.board_rect()
        x0 = rect.x() + left
        y0 = rect.y()
        w = rect.width() / 30
        h = rect.height() / 16
        # logger.debug((x0, y0, w, h))
        self.cursor().setPos(x0 + (x + 0.5) * w, y0 + (y + 0.5) * h)

    def mark_action(self, board, result):
        logger.debug("mark action")

        for y, line in enumerate(board):
            for x, value in enumerate(line):
                where = (y, x)
                if board[where] == 9 and result[where] == 10:
                    self.events.put((where, 1))
                if board[where] == 9 and result[where] == 14:
                    self.events.put((where, 0))

    def probability(self):
        map = self.screenshot()
        if not map:
            return
        board = self.situation(map)
        if board is None:
            return
        mark = board.copy()

        result = np.zeros_like(board).astype(np.float32)

        for y, line in enumerate(board):
            for x, value in enumerate(line):
                where = (y, x)
                if board[where] > 8:
                    continue

                possible = self.get_possible(y, x, board)
                if not possible:
                    continue
                if len(possible) <= 1:
                    self.make_events()
                    # logger.debug(board)
                    # logger.error((where, board[where], possible))
                    return

                prob = 1.0 / len(possible)

                for pos in possible:
                    if result[pos] < prob:
                        result[pos] = prob
                        mark[pos] = 14

        args0 = np.argwhere(board == 9)
        args1 = np.argwhere(mark == 14)
        temp = result.copy()

        # logger.debug((result.shape, board.shape))

        result[result == 0.0] = 1.0
        divider = (len(args0) - len(args1))
        if divider > 0:
            prob = 1.0 / divider
            for where in args0:
                result[(where[0], where[1])] = prob
            for where in args1:
                result[(where[0], where[1])] = temp[(where[0], where[1])]

        value = np.min(result)
        args = np.argwhere(result == value)
        wheres = [(x[0], x[1]) for x in args]
        self.events.put((random.choice(wheres), 3))
        return result

    def do_click_events(self):
        self.running = True
        while True:
            where, type = self.events.get()
            if self.error:
                self.running = False
                return
            self.move_to_pos(where[0], where[1])
            if type == 0:
                logger.debug(f"double click {where}")
                pyautogui.click()
                pyautogui.doubleClick()
                pyautogui.doubleClick()
                time.sleep(0.1)
            elif type == 1:
                logger.debug(f"right click {where}")
                pyautogui.rightClick()
                time.sleep(0.1)
            else:
                pyautogui.click()
                pyautogui.doubleClick()
                pyautogui.doubleClick()
                # self.cursor().setPos(self.left + 20, 200)
                # pyautogui.rightClick()

                board = self.situation()
                if board is None:
                    self.running = False
                    return
                time.sleep(0.1)

            if self.events.empty():
                # self.cursor().setPos(self.left + 20, 200)
                # pyautogui.rightClick()
                self.make_events()
                time.sleep(0.1)
            if self.events.empty():
                self.probability()
                time.sleep(0.1)
                # self.cursor().setPos(self.left + 20, 200)
                # pyautogui.rightClick()

    def make_events(self):
        map = self.screenshot()
        if not map:
            return
        board = self.situation(map)
        if board is None:
            return

        result = self.solve_board(board)
        self.mark_action(board, result)

    def enter_event(self):
        self.error = False

        self.make_events()
        if self.events.empty():
            self.probability()

        if not self.running:
            self.click_thread = threading.Thread(target=self.do_click_events, daemon=True)
            self.click_thread.start()
            # self.show_situation(board)

    def load_classifier(self):
        self.label.setText("Loading classifier ...")
        self.classifier = tone.utils.learning.load_pickle(
            os.path.join(dirname, "model.pkl"))
        self.classifier.eval()
        self.label.setText("")
        return self.classifier

    def __init__(self, screen=None) -> None:
        super().__init__()
        self.setWindowTitle(f"MineSweeper Helper")
        if screen:
            self.setScreen(screen)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysStackOnTop)
        # self.setWindowOpacity(0.7)
        self.move(self.screen().geometry().topLeft())
        self.showMaximized()

        self.signal = Signal()
        self.signal.enter.connect(self.enter_event)

        with mss.mss() as sct:
            if screen == QGuiApplication.screens()[0]:
                geo = QRect(85, 170, 940, 510)
                self.left = 0
            else:
                geo = QRect(155, 190, 1195, 640)
                self.left = sct.monitors[1]['width']

        logger.debug(geo)

        self.vlines = [
            Line(self, pos=geo.x(), vertical=True),
            Line(self, pos=geo.x() + geo.width(), vertical=True)
        ]
        self.hlines = [
            Line(self, pos=geo.y(), vertical=False),
            Line(self, pos=geo.y() + geo.height(), vertical=False)
        ]
        self.label = QLabel(self)
        self.label.setGeometry(geo)
        self.label.setText("")
        self.label.setStyleSheet("QLabel{font-size: 24pt; color: blue;}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setScaledContents(True)
        self.label.show()

        self.label1 = QLabel(self)
        self.label1.setGeometry(0, geo.y(), geo.x(), geo.height())
        self.label1.setStyleSheet("background-color: rgba(0, 0, 255, 5)")
        self.label1.show()

        self.events = queue.Queue()
        self.click_thread = None

        self.running = False
        self.error = False
        self.classifier = None

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()
        # logger.debug(event)
        if key == Qt.Key.Key_Return:
            self.signal.enter.emit()
            return
        if key == Qt.Key.Key_Escape:
            self.label.setVisible(False)
            return
        if key == Qt.Key.Key_T:
            self.show_coordinate()
            return
        if key == Qt.Key.Key_P:
            self.show_board()
            return
        if key == Qt.Key.Key_H:
            for line in self.vlines:
                line.setVisible(not line.isVisible())
            for line in self.hlines:
                line.setVisible(not line.isVisible())
        return super().keyPressEvent(event)


def main():
    app = QApplication(sys.argv)
    window = MainWindow(app.screens()[1])
    # window.show()
    app.exec()


if __name__ == '__main__':
    main()
