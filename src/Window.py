#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : Window.py    
@Note : 界面逻辑部分
'''

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from UI import UI_Window
from Plan import Plan


class Window(UI_Window):
    def __init__(self):
        super().__init__()
        self.bllTab1()
        self.bllTab2()
        self.bllTab3()

    def bllTab1(self):
        pass

    def bllTab2(self):
        self.addBtn.clicked.connect(self.addPlan)

    def bllTab3(self):
        pass

    # tab1部分

    # tab2部分
    def addPlan(self):
        plan = Plan()
        all_count = self.layoutVP2.count()
        self.layoutVP2.insertWidget(all_count+1, plan, 0, Qt.AlignJustify)

    # tab3部分

