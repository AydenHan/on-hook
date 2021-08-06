#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : UI.py
@Note : 界面UI部分
'''

from pyqt5Custom import StyledButton,Toast
from PyQt5.QtWidgets import QWidget,QVBoxLayout
from PyQt5.QtCore import Qt
import QSS

class UI_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setupModule()
        self.setupUi()

    def setupModule(self):
        self.layout_global = QVBoxLayout(self)
        self.button_plan = StyledButton('选项')
        self.label_count = StyledButton()
        self.button_control = StyledButton(icon=QSS.startBtn)
        self.info = Toast(self, "", QSS.toastBtn)
        self.layout_global.addWidget(self.button_plan, 0, Qt.AlignHCenter)
        self.layout_global.addWidget(self.label_count, 0, Qt.AlignHCenter)
        self.layout_global.addWidget(self.button_control, 0, Qt.AlignHCenter)
        self.layout_global.addWidget(self.info, 0, Qt.AlignHCenter)
        self.info.fall()

    def setupUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMaximumSize(75, 300)
        # size
        self.button_plan.setMaximumSize(65, 65)
        self.button_plan.setMinimumSize(65, 65)
        self.label_count.setMaximumSize(65, 65)
        self.label_count.setMinimumSize(65, 65)
        self.button_control.setMaximumSize(65, 65)
        self.button_control.setMinimumSize(65, 65)
        # style
        self.button_control.setIconSize(42, 42)
        self.button_plan.setStyleDict(QSS.button_plan_qss)
        self.label_count.setStyleDict(QSS.label_count_qss)
        self.button_control.setStyleDict(QSS.button_control_qss)

    def startStatus(self):
        self.button_control.setIcon(QSS.startBtn)
        self.button_control.setIconSize(42, 42)
        self.info.rise(4)

    def stopStatus(self):
        self.button_control.setIcon(QSS.stopBtn)
        self.button_control.setIconSize(42, 42)


