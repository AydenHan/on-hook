#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : UI_Plan.py    
@Note : 界面tab2方案部分的自定义类UI部分
'''

from PyQt5.QtWidgets import QWidget,QTextEdit,QHBoxLayout,QPushButton,QLabel
from PyQt5.QtCore import Qt

class UI_Plan(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.label_plan = QLabel()
        self.textEdit_plan = QTextEdit()
        self.selectBtn = QPushButton(u'选取')
        self.doubleBtn = QPushButton(u'确认')

        self.layout.addWidget(self.label_plan, 1, Qt.AlignLeft)
        self.layout.addWidget(self.textEdit_plan, 1, Qt.AlignLeft)
        self.layout.addWidget(self.selectBtn, 0, Qt.AlignRight)
        self.layout.addWidget(self.doubleBtn, 0, Qt.AlignRight)
        self.layout.setContentsMargins(0, 0, 0, 0)      #左上右下，边距
        # self.layout.setSpacing(0)

        self.label_plan.hide()
        self.setLayout(self.layout)

    def setUI(self):
        self.setMinimumWidth(372)
        # set size
        self.label_plan.setWordWrap(True)    #自动换行
        self.label_plan.setMinimumSize(300, 30)
        self.label_plan.setMaximumSize(300, 30)
        self.textEdit_plan.setMinimumHeight(30)
        self.textEdit_plan.setMaximumHeight(30)
        self.selectBtn.setMinimumSize(45, 30)
        self.selectBtn.setMaximumSize(45, 30)
        self.doubleBtn.setMinimumSize(45, 30)
        self.doubleBtn.setMaximumSize(45, 30)
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def editorStatus(self):
        self.doubleBtn.setText(u'确认')
        self.textEdit_plan.show()
        self.label_plan.hide()

    def saveStatus(self):
        self.label_plan.setText(self.textEdit_plan.toPlainText())
        self.doubleBtn.setText(u'删除')
        self.textEdit_plan.hide()
        self.label_plan.show()


