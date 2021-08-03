#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : Window.py    
@Note : 界面逻辑部分
'''

from PyQt5.QtWidgets import QWidget,QBoxLayout
from PyQt5.QtCore import Qt,pyqtSignal
from UI import UI_Window
from Plan import Plan
from Data_Json import JsonHandle


class Window(UI_Window):
    def __init__(self):
        super().__init__()
        # 数据
        self.json_path = '../data/config.json'
        self.data = JsonHandle.getJson(self.json_path)
        # 各模块
        self.bllTab1()
        self.bllTab2()
        self.bllTab3()

    # 退出时更新本地文件数据
    def __del__(self):
        # Config.updateIni(self.ini)
        pass

    def bllTab1(self):
        pass

    def bllTab2(self):
        self.addBtn.clicked.connect(self.addPlan)
        self.loadPlan()

    def bllTab3(self):
        pass

    # tab1部分

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
        if not val:
            i = 0
            for x in self.data['plan']:
                i += 1
                if x['id'] == id:
                    self.data['plan'].pop(i - 1)
        JsonHandle.updateJson(self.json_path, self.data)

    # tab3部分

