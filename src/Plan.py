#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : Plan.py    
@Note : 界面tab2方案部分的自定义类逻辑部分
'''

from PyQt5.QtWidgets import QFileDialog
from UI_Plan import UI_Plan


class Plan(UI_Plan):
    def __init__(self):
        super().__init__()
        self.initModule()
        self.funcLink()

    def initModule(self):
        # self.hide()
        pass

    def funcLink(self):
        self.selectBtn.clicked.connect(self.selectScreenshot)
        self.doubleBtn.clicked.connect(self.sureOrDelete)

    def selectScreenshot(self):
        file_name, file_type = QFileDialog.getOpenFileNames(self,
                            "选取文件", "../screenshot/", "PNG Files(*.png)")

    def sureOrDelete(self):
        if self.label_plan.isHidden():
            #signal
            self.saveStatus()
        elif self.textEdit_plan.isHidden():
            #signal
            self.deleteLater()



