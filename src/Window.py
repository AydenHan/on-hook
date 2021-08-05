#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : Window.py    
@Note : 界面逻辑部分
'''

from PyQt5.QtCore import Qt
from datetime import datetime
from UI import UI_Window
from Plan import Plan
from OnHook import OnHook
from ScreenShot import CaptureScreen
from Data_Json import JsonHandle


class Window(UI_Window):
    def __init__(self):
        super().__init__()
        # 数据
        self.json_path = '../data/config.json'
        self.screenshot_path = '../screenshot/'
        self.data = JsonHandle.getJson(self.json_path)
        self.time_start = datetime.now()
        # 各模块
        # self.on_hook = OnHook()
        self.bllTab1()
        self.bllTab2()
        self.bllTab3()

    # 退出时更新本地文件数据
    def __del__(self):
        # Config.updateIni(self.ini)
        pass

    def bllTab1(self):
        # 初始化
        self.selectPlan()
        # 事件绑定
        self.startBtn.clicked.connect(self.startOnHook)
        self.stopBtn.clicked.connect(self.stopOnHook)

    def bllTab2(self):
        # 初始化
        self.loadPlan()
        # 事件绑定
        self.addBtn.clicked.connect(self.addPlan)

    def bllTab3(self):
        self.screenshotBtn.clicked.connect(self.screenShot)

    # tab1部分
    def rstPrintf(self, mes):
        self.textBrowser_feedback.append(mes)  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser_feedback.textCursor()
        self.textBrowser_feedback.moveCursor(self.cursot.End)

    def selectPlan(self):   #下拉选项
        for item in self.data['plan']:
            self.comboBox_plan.addItem(item['id'])

    def startOnHook(self):
        index = self.comboBox_plan.currentIndex()
        times = self.textEdit_time.toPlainText()
        if not times:
            times = 0
        else:
            times = int(times)
        self.on_hook = OnHook(self, self.data['plan'][index]['node'], times)
        self.on_hook.finished.connect(self.stopOnHook)
        self.on_hook.start()
        self.rstPrintf("—————————开始—————————")
        self.time_start = datetime.now()

    def stopOnHook(self):
        turn = self.on_hook.turn
        self.on_hook.quit()
        del self.on_hook
        self.rstPrintf("共完成: %s轮, 用时: %s\n" % (turn, datetime.now() - self.time_start))

    # tab2部分
    def createPlan(self, data):
        plan = Plan(self, data)
        all_count = self.layoutVP2.count()
        self.layoutVP2.insertWidget(all_count-1, plan, 0, Qt.AlignTop)
        # 连接方案配置数据的信号
        plan.plan_config.connect(self.planHandle)

    def addPlan(self):
        exp = {
            'id': '',
            'node': ''
        }
        self.data['plan'].append(exp)
        self.createPlan(exp)

    def loadPlan(self):
        if len(self.data['plan']):
            for i in self.data['plan']:
                self.createPlan(i)

    def planHandle(self, val, id):
        # 数据部分
        if not val:
            i = 0
            for x in self.data['plan']:
                i += 1
                if x['id'] == id:
                    self.data['plan'].pop(i - 1)
        JsonHandle.updateJson(self.json_path, self.data)
        # UI部分
        self.comboBox_plan.clear()
        self.selectPlan()

    # tab3部分
    def screenShot(self):
        shot = CaptureScreen()
        shot.show()
        print(111)
