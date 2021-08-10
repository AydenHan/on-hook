#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : QSS.py    
@Note : 样式与路径
'''
img = "../img/"
# game = 'Launch.exe'

startBtn = img + "icon/start.png"
stopBtn = img + "icon/stop.png"
timeIcon = img + "icon/time.png"
settingsIcon = img + "icon/settings.png"
linkIcon = img + "icon/link.png"
poweroffIcon = img + "icon/poweroff.png"

screenshot = img + "screenshot/"

dailyCycle = [
    "challenge.png",
    "defeat.png",
    "victory.png",
    "award.png"
]
breakCycle = [
    "attack.png",
    "award.png",
    "breakaim.png",
    "defeat.png",
    "refresh.png"
]
exploreCycle = [
    "award.png",
    "explore.png",
    "leader.png",
    "target.png"
]

button_plan_qss = {
    "font-family": "SimSun",
    "font-size": 22,
    "color": (44, 44, 44),
    "border-width": 2,
    "border-color": (44, 44, 44)
}

label_count_qss = {
    "font-family": "Helvetica",
    "font-size": 40,
    "color": (216, 30, 6),
    "border-width": 2,
    "border-color": (216, 30, 6)
}

button_control_qss = {
    "border-width": 2,
    "border-color": (18, 150, 219)
}