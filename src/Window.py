#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : Window.py    
@Note : 
'''

import win32gui,os,sys
from PyQt5.QtCore import QTimer,QFile,QStandardPaths
from PyQt5.QtWidgets import qApp
from datetime import datetime
from UI_Window import UI_Window
from SCP_OnHook import OnHook
import QSS

class Window(UI_Window):
    def __init__(self):
        super().__init__()
        self.isStart = False
        self.time_start = datetime.now()
        self.check_timer = QTimer()
        self.plan = QSS.dailyCycle

        # self.startGame('../', QSS.game)
        self.funcLink()
        self.check_timer.start(35)

    def startGame(self, path, filename):
        for root, dirs, files in os.walk(path):
            for file in files:
                if filename in file:
                    os.system(os.path.abspath((os.path.join(root, file))))

    def funcLink(self):
        self.button_plan.clicked.connect(self.openSettings)
        self.button_control.clicked.connect(self.controlOnHook)
        self.check_timer.timeout.connect(self.followHang)
        self.settings.switch_plan.clicked.connect(self.selectPlan)
        self.settings.button_shortcut.clicked.connect(self.addShortcut)
        self.settings.button_poweroff.clicked.connect(self.quiApp)

    def followHang(self):
        hwnd = win32gui.FindWindow(None, "阴阳师-网易游戏")
        if hwnd:
            rect = win32gui.GetWindowRect(hwnd)
            self.move(rect[0] - 10 - self.button_plan.width() -
                      self.mainpage.x() - self.button_plan.x(), rect[1]) #使可视化区域与窗口始终保持相同距离而不是窗体
            if self.isVisible() == False:
                self.setVisible(True)
        else:
            if self.isVisible() == True:
                self.setVisible(False)

    def openSettings(self):
        if self.settings.isVisible():
            self.settings.fall()
        else:
            self.settings.rise(3)

    def selectPlan(self, val):
        if val == 1:
            self.plan = QSS.dailyCycle
        elif val == 2:
            self.plan = QSS.breakCycle
        elif val == 3:
            self.plan = QSS.exploreCycle

    def addShortcut(self):
        pathExe = sys.executable
        pathIcon = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation) + "/" + "OnHook.lnk"
        if not os.path.exists(pathIcon):
            QFile.link(pathExe, pathIcon)

    def quiApp(self):
        self.close()
        qApp.quit()

    def timesDisplay(self, val):
        self.label_count.setText(str(val))

    def controlOnHook(self):
        if not self.isStart:
            self.startOnHook()
            self.stopStatus()
            self.isStart = True
        else:
            self.stopOnHook()
            self.startStatus()
            self.isStart = False

    def startOnHook(self):
        self.timesDisplay(0)
        self.on_hook = OnHook(self, self.plan)
        self.on_hook.times_change.connect(self.timesDisplay)
        self.time_start = datetime.now()
        self.on_hook.start()

    def stopOnHook(self):
        time = str(datetime.now() - self.time_start)
        self.info.setText("耗时: %s" % time[0 : time.rfind(':') + 3])     #对datetime格式进行处理
        self.on_hook.quit()
        del self.on_hook
