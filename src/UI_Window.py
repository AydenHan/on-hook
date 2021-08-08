#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : UI.py
@Note : 界面UI部分
'''

from pyqt5Custom import ToggleSwitch
from UI_Custom import CustomButton,CustomToast,DynamicWidget
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt
import QSS

class UI_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setupModule()
        self.setupUi()

    def setupModule(self):
        self.layout_global = QHBoxLayout(self)
        self.layout_global.setContentsMargins(0, 5, 0, 0)

        self.settings = DynamicWidget(self, '设置', QSS.settingsIcon)
        self.layout_global.addWidget(self.settings, alignment=Qt.AlignCenter)

        self.mainpage = QWidget()
        self.layout_global.addWidget(self.mainpage, alignment=Qt.AlignRight)
        self.layout_main = QVBoxLayout()
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.mainpage.setLayout(self.layout_main)
        self.button_plan = CustomButton('选项')
        self.label_count = CustomButton()
        self.button_control = CustomButton(icon=QSS.startBtn)
        self.layout_main.addWidget(self.button_plan, 0, Qt.AlignHCenter | Qt.AlignTop)
        self.layout_main.addWidget(self.label_count, 0, Qt.AlignHCenter | Qt.AlignTop)
        self.layout_main.addWidget(self.button_control, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.info_bar = QWidget()
        self.layout_info = QHBoxLayout()
        self.layout_info.setContentsMargins(0, 3, 0, 0)
        self.info_bar.setLayout(self.layout_info)
        self.layout_main.addWidget(self.info_bar, alignment=Qt.AlignTop)
        self.info = CustomToast(self, "", QSS.timeIcon)
        self.layout_info.addWidget(self.info, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.info.fall()

    def setupUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # size
        # self.mainpage.setFixedWidth(65)
        self.button_plan.setFixedSize(65, 65)
        self.label_count.setFixedSize(65, 65)
        self.button_control.setFixedSize(65, 65)
        self.button_plan.setContentsMargins(0, 0, 0, 5)
        self.label_count.setContentsMargins(0, 0, 0, 5)
        self.button_control.setContentsMargins(0, 0, 0, 5)
        # style
        self.button_plan.setStyleDict(QSS.button_plan_qss)
        self.label_count.setStyleDict(QSS.label_count_qss)
        self.button_control.setIconSize(42, 42)
        self.button_control.setStyleDict(QSS.button_control_qss)

    def startStatus(self):
        self.button_control.setIcon(QSS.startBtn)
        self.button_control.setIconSize(42, 42)
        self.info.rise(4)

    def stopStatus(self):
        self.button_control.setIcon(QSS.stopBtn)
        self.button_control.setIconSize(42, 42)


