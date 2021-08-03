#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : OnHook.py
@Note : 仅为做出来玩的，重在学习，封号了别怪我
'''

import pyautogui as pag
import cv2
import random
import math
import time
import datetime
import gevent
# 策略：
#   start时选取区域为挑战图标所在圆内随机位置点击
#   end时选取区域为整个客户端界面不会造成额外效果的位置，随机位置点击
# locateOnScreen:
#   返回元组 (左上角的x, 左上角的y, 图片的宽, 图片的高)
#   运行时间：没找到1.58s左右，找得到的时间不定暂未知晓

turn = 0

class OnHook(object):
    def clickEvent(self, picture):
        global turn

        while True:
            pic = '../data/yys/' + picture  # 截图保存的路径（建议截图区域内像素分明又不是很复杂）
            point = pag.locateOnScreen(pic, confidence=0.8)
            pic = pic[pic.rfind('/')+1:pic.rfind('.png')].ljust(9)  # 输出处理
            if point is None:
                # if turn == 1:  # 预防第一次弹出小动物奖励框导致无法识别卡死
                #     tf = datetime.datetime.now() - ts
                #     if int(str(tf).split(':')[1]) > 0 and pic == "challenge":
                #         pag.click(x, y)  # 点击
                gevent.sleep(1)  # 暂停该协程，转而运行判断其余场景的协程
            else:
                click_num = random.randint(1, 2)  # 各种随机，企图骗过检测
                click_time = math.ceil(random.uniform(0.15, 0.29)*100) / 100
                move_time = math.ceil(random.uniform(0.05, 0.25)*100) / 100
                x = random.randint(point[0], point[0] + point[2])
                y = random.randint(point[1], point[1] + point[3])
                # 御魂觉醒御灵等
                if pic == "challenge" or pic == "attack   ":
                    turn += 1
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
                    if not (turn != 0 and turn % 3 == 0):
                        break
                elif pic == "breakaim ":
                    if turn != 0 and turn % 3 == 0:
                        break
                    else:
                        click_num = 1
                        x += 370 * turn
                # 困28
                elif pic == "target   ":  # 很不好用
                    turn += 1
                    pos = pag.locateOnScreen('../data/yys/fight.png', confidence=0.8,
                                             region=(point[0]-160, point[1]-260, 370, 260))
                    x = random.randint(pos[0], pos[0] + pos[2])
                    y = random.randint(pos[1], pos[1] + pos[3])

                pag.click(x, y, duration=move_time, clicks=click_num,
                          interval=click_time)  # 点击
                print("%s , [ %s, ClickPos:(%s, %s), ClickNum:%s次 ]"
                      % (pic, turn, x, y, click_num))
                gevent.sleep(0.9)  # 该次协程结束后卡一定时间防止二次识别成功，在切换界面后误触

    # —————————添加识别协程————————— #
    def dailyCycle(self):
        gevent.joinall([
            gevent.spawn(self.clickEvent, 'challenge.png'),
            gevent.spawn(self.clickEvent, 'defeat.png'),
            gevent.spawn(self.clickEvent, 'victory.png'),  # 偶尔识别
            gevent.spawn(self.clickEvent, 'award.png')
        ])



