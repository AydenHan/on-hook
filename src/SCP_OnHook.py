#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : OnHook.py
@Note : 挂机脚本类
'''

from PyQt5.QtCore import QThread,pyqtSignal
from datetime import datetime
import pyautogui as pag,cv2
import random,math
import gevent
import QSS

class OnHook(QThread):
    times_change = pyqtSignal(int)

    def __init__(self, parent, data):
        super().__init__()
        self.data = data
        self.pw = parent
        self.turn = 0
        self.g_list = []

    def run(self):
        matrix = []
        for node in self.data:
            matrix.append(gevent.spawn(self.clickHandle, node))
            self.g_list = matrix
        gevent.joinall(matrix)

    def quit(self):
        for i in self.g_list:
            gevent.kill(i)

    def clickHandle(self, picture):
        while True:
            pic = QSS.screenshot + picture  # 截图保存的路径（建议截图区域内像素分明又不是很复杂）
            point = pag.locateOnScreen(pic, confidence=0.8)
            pic = pic[pic.rfind('/')+1:pic.rfind('.png')].ljust(9)  # 输出处理
            if point is None:
                if self.turn == 1:  # 预防第一次弹出小动物奖励框导致无法识别卡死
                    tf = datetime.now() - self.pw.time_start
                    if int(str(tf).split(':')[1]) > 0 and pic == "challenge":
                        pag.click(x, y)  # 点击
                gevent.sleep(1)  # 暂停该协程，转而运行判断其余场景的协程
            else:
                click_num = random.randint(1, 2)  # 各种随机，企图骗过检测
                click_time = math.ceil(random.uniform(0.15, 0.29)*100) / 100
                move_time = math.ceil(random.uniform(0.05, 0.25)*100) / 100
                x = random.randint(point[0], point[0] + point[2])
                y = random.randint(point[1], point[1] + point[3])
                # 御魂觉醒御灵等
                if pic == "challenge" or pic == "attack   ":
                    self.turn += 1
                    self.times_change.emit(self.turn)
                elif pic == "award    ":  # 进一步掩盖机械行为
                    x = random.randint(point[0], point[0] + point[2]*5)
                    y = random.randint(point[1] - point[3]
                                       * 2, point[1] + point[3]*2)
                elif pic == "defeat   ":
                    x = random.randint(point[1], point[1] + point[3]*7)
                    y = random.randint(point[0] - point[2]
                                       * 5, point[0] - point[2]*2)
                # 结界突破
                elif pic == "refresh  ":
                    if not (self.turn != 0 and self.turn % 3 == 0):
                        break
                elif pic == "breakaim ":
                    if self.turn != 0 and self.turn % 3 == 0:
                        break
                    else:
                        click_num = 1
                        x += 370 * self.turn
                # 困28
                elif pic == "target   ":  # 很不好用
                    self.turn += 1
                    pos = pag.locateOnScreen(QSS.screenshot + 'fight.png', confidence=0.8,
                                             region=(point[0]-160, point[1]-260, 370, 260))
                    x = random.randint(pos[0], pos[0] + pos[2])
                    y = random.randint(pos[1], pos[1] + pos[3])

                # 模拟点击
                pag.click(x, y, duration=move_time, clicks=click_num,
                          interval=click_time)  # 点击

                gevent.sleep(0.9)  # 该次协程结束后卡一定时间防止二次识别成功，在切换界面后误触