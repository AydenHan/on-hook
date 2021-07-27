#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : OnHook.py
@Note : 挂机脚本部分
'''

import pyautogui as pag,cv2
import random,math,time,datetime
import gevent
#策略：
#   start时选取区域为挑战图标所在圆内随机位置点击
#   end时选取区域为整个客户端界面不会造成额外效果的位置，随机位置点击
#locateOnScreen:
#   返回元组 (左上角的x, 左上角的y, 图片的宽, 图片的高)
#   运行时间：没找到1.58s左右，找得到的时间不定暂未知晓

turn = 0


class OnHook(object):
    def __init__(self):
        time.sleep(3)
        print("Start!")
        self.ts = datetime.datetime.now()

    def __del__(self):
        self.te = datetime.datetime.now()
        print("End!")
        print("Total:%s rounds, Runtime:%ss" % (turn, self.te - self.ts))

    def clickEvent(self, picture):
        global turn

        while True:
            pic = '../img/screenshot/' + picture  # 路径改这里
            point = pag.locateOnScreen(pic, confidence=0.8)
            if point is None:
                gevent.sleep(1)     #暂停该协程，转而运行判断其余场景的协程
            else:
                click_num = random.randint(1, 2)    #各种随机，企图骗过检测
                click_time = math.ceil(random.uniform(0.15, 0.29)*100) / 100
                move_time = math.ceil(random.uniform(0.05, 0.25)*100) / 100
                x = random.randint(point[0], point[0] + point[2])
                y = random.randint(point[1], point[1] + point[3])

                pic = pic[pic.rfind('/')+1:pic.rfind('.png')]   #输出处理
                pic = pic.ljust(9)           
                if pic == "challenge":
                    turn+=1
                elif pic == "award    ":    #进一步掩盖机械行为
                    x = random.randint(point[0], point[0] + point[2]*5)
                    y = random.randint(point[1] - point[3]*2, point[1] + point[3]*2)
                elif pic == "defeat   ":
                    x = random.randint(point[1], point[1] + point[3]*7)
                    y = random.randint(point[0] - point[2]*5, point[0] - point[2]*2)

                pag.click(x, y, duration=move_time, clicks=click_num, interval=click_time)  #点击
                print("%s , [ %s, ClickPos:(%s, %s), ClickNum:%s次 ]"
                      % (pic, turn, x, y, click_num))
                gevent.sleep(0.7)     #卡一秒防止二次识别成功，在切换界面后误触

    #识别协程————可识别所有的御魂觉醒御灵关卡
    def dailyCycle(self):
        gevent.joinall([
            gevent.spawn(self.clickEvent, 'challenge.png'),
            gevent.spawn(self.clickEvent, 'defeat.png'),
            gevent.spawn(self.clickEvent, 'victory.png'),    #偶尔识别
            gevent.spawn(self.clickEvent, 'award.png')
        ])

if __name__ == '__main__':
    #自动控制类
    script = OnHook()
    script.dailyCycle()


