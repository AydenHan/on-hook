#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : UI_Plan.py    
@Note : 界面tab2方案部分的自定义类UI部分
'''

from PyQt5.QtWidgets import QWidget,QTextEdit,QHBoxLayout,QPushButton,QLabel,QSizePolicy
from PyQt5.QtCore import Qt

class UI_Plan(QWidget):
    def __init__(self):
        super().__init__()
        self.initModdule()
        self.setModule()

    def initModdule(self):
        self.layout = QHBoxLayout()
        self.label_plan = QLabel()
        self.textEdit_plan = QTextEdit()
        self.selectBtn = QPushButton(u'选取')
        self.deleteBtn = QPushButton(u'删除')

        self.layout.addWidget(self.label_plan, 10, Qt.AlignLeft)
        self.layout.addWidget(self.textEdit_plan, 1, Qt.AlignLeft)
        self.layout.addWidget(self.deleteBtn, 1, Qt.AlignRight)
        self.layout.setContentsMargins(1, 10, 1, 10)
        self.layout.setSpacing(1)

        self.label_plan.hide()
        self.setLayout(self.layout)

    def setModule(self):
        self.setMinimumWidth(372)
        # set size
        self.label_plan.setMargin(5)
        self.label_plan.setWordWrap(True)    #自动换行
        self.label_plan.setMinimumSize(300, 30)
        self.label_plan.setMaximumSize(300, 30)
        self.textEdit_plan.setMinimumHeight(30)
        self.textEdit_plan.setMaximumHeight(30)
        self.deleteBtn.setMinimumSize(45, 30)
        self.deleteBtn.setMaximumSize(45, 30)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)




