#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : Plan.py    
@Note : 界面tab2方案部分的自定义类逻辑部分
'''

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt,pyqtSignal
from UI_Plan import UI_Plan


class Plan(UI_Plan):
    # 信号
    plan_config = pyqtSignal(bool, str)
    def __init__(self, parent, data=None):
        super().__init__()
        # 属性
        self.pw = parent
        self.data = data

        self.initModule()
        self.funcLink()

    def initModule(self):
        if self.data['id']:
            self.saveStatus()
            self.label_plan.setText(self.data['id'])

    def funcLink(self):
        self.selectBtn.clicked.connect(self.selectScreenshot)
        self.doubleBtn.clicked.connect(self.sureOrDelete)

    def selectScreenshot(self):
        file_name, file_type = QFileDialog.getOpenFileNames(self,
                            "选取文件", "../screenshot/", "PNG Files(*.png)")
        if file_name:
            fn = []
            for x in file_name:
                fn.append( x[x.rfind('/')+1 : ] )
            self.data['node'] = fn

    def sureOrDelete(self):
        if self.label_plan.isHidden():  #编辑状态
            # 状态更新
            self.saveStatus()
            # 数据更新
            self.data['id'] = self.label_plan.text()
            self.plan_config.emit(True, self.data['id'])
        elif self.textEdit_plan.isHidden(): #完成状态
            self.plan_config.emit(False, self.data['id'])
            self.deleteLater()

    def mouseDoubleClickEvent(self, QMouseEvent):   #双击再次进入编辑状态
        if QMouseEvent.button() == Qt.LeftButton:
            self.editStatus()



