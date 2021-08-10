#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : UI_Custom.py
@Note : 自定义类
'''

from pyqt5Custom import StyledButton,Toast, Animation, AnimationHandler,ImageBox
from PyQt5.QtCore    import Qt,pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui     import QPainter, QPen, QBrush, QColor, QFont
import QSS


class SegmentedButton(QWidget):

    clicked = pyqtSignal(int)

    def __init__(self, radio=False):
        super().__init__()

        self.styleDict = {
            "default" : {
                "background-image" : None,
                "background-color" : (255, 255, 255),

                "border-color"  : (0, 0, 0),
                "border-width"  : 1,
                "border-radius" : 6,
                "radius-corners" : (True, True, True, True),

                "font-family" : None,
                "font-size"   : 12,
                "font-weight" : "regular",
                "color"       : (0, 0, 0),

                "drop-shadow-radius" : 0,
                "drop-shadow-offset" : (0, 0),
                "drop-shadow-alpha"  : 120,

                "click-effect-radius" : 500,
                "click-effect-color"  : (0, 0, 0, 90),

                "render-fast"      : False,
                "render-aa"        : True,
                "font-subpixel-aa" : False
            },

            "hover" : {
                "background-image" : None,
                "background-color" : (245, 245, 245),

                "border-color"  : (0, 0, 0),
                "border-width"  : 1,
                "border-radius" : 11,

                "font-size"   : 12,
                "font-weight" : "regular",
                "color"       : (0, 0, 0),

                "drop-shadow-radius" : 0,
                "drop-shadow-offset" : (0, 0),
                "drop-shadow-alpha"  : 120
            },

            "press" : {
                "background-image" : None,
                "background-color" : (228, 228, 228),

                "border-color"  : (0, 0, 0),
                "border-width"  : 1,
                "border-radius" : 11,

                "font-size"   : 12,
                "font-weight" : "regular",
                "color"       : (0, 0, 0),

                "drop-shadow-radius" : 0,
                "drop-shadow-offset" : (0, 0),
                "drop-shadow-alpha"  : 120
            },

            "check-hover" : {
                "background-image" : None,
                "background-color" : (245, 245, 245),

                "border-color"  : (0, 0, 0),
                "border-width"  : 1,
                "border-radius" : 11,

                "font-size"   : 12,
                "font-weight" : "regular",
                "color"       : (0, 0, 0),

                "drop-shadow-radius" : 0,
                "drop-shadow-offset" : (0, 0),
                "drop-shadow-alpha"  : 120
            },
        }

        self.radio = radio

        self._buttons = list()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(2, 2, 2, 2)
        self.layout.setSpacing(0)

    def setStyleDict(self, styledict, state=None):
        if state is None:
            for k in styledict:
                self.styleDict["default"][k] = styledict[k]
                self.styleDict["hover"][k] = styledict[k]
                self.styleDict["press"][k] = styledict[k]
                self.styleDict["check-hover"][k] = styledict[k]
        else:
            for k in styledict:
                self.styleDict[state][k] = styledict[k]

    def addButton(self, text="", icon=None, tag=None):
        btn = StyledButton(text=text, icon=None)
        btn.setStyleDict(self.styleDict["default"])
        btn.setStyleDict(self.styleDict["hover"], "hover")
        btn.setStyleDict(self.styleDict["press"], "press")
        btn.setStyleDict(self.styleDict["check-hover"], "check-hover")
        if self.radio:
            btn.setCheckable(True)

        if tag is None: tag = id(btn)
        self._buttons.append((tag, btn))
        self.layout.addWidget(btn, alignment=Qt.AlignHCenter)

        if len(self._buttons) == 1:
            btn.setStyleDict({"radius-corners":(True, True, False, False)})
        else:
            if len(self._buttons) >= 3:
                btnPrev = self._buttons[-2][1]
                btnPrev.setStyleDict({"radius-corners":(False, False, False, False)})
            btn.setStyleDict({"radius-corners":(False, False, True, True)})

        for btnn in self._buttons:
            btnn[1].setFixedSize(self.width(), self.height()/len(self._buttons))

        @btn.clicked.connect
        def slot():
            self.clicked.emit(self._clicked(tag))

        l = len(self._buttons)
        self.layout.setContentsMargins(0, l*2, 0, l*2)
        return btn

    def getByTag(self, tag):
        for btn in self._buttons:
            if btn[0] == tag: return btn[1]

    def _clicked(self, tag):
        i = 0
        num = 0
        for btn in self._buttons:
            i += 1
            if btn[0] != tag:
                if btn[1].isChecked():
                    btn[1].anim_press.start(reverse=True)
                    btn[1]._was_checked = False
                    btn[1].setChecked(False)
            else:
                num = i
        return num

# —————————————————————————————以下参数需要修改—————————————————————————————#
class track:
    easeOutQuart = lambda x: 1 - pow(1 - x, 4)
    easeInQuart = lambda x: pow(x, 3)

'''
@note: 借鉴pyqt5Custom库中Toast类的思路修改
'''
class DynamicWidget(QWidget):
    def __init__(self, parent, text="", icon=None, closeButton=True):
        super().__init__(parent)
        # —————————————————————————————以下参数需要修改—————————————————————————————#
        self.setFixedSize(150,300)
        speed = 3.3

        w = self.width()
        h = self.height()
        self.setGeometry(0, 0, w, h)

        self.styleDict = {
            "background-color": (0, 0, 0, 200),
            "border-radius": 12,

            "font-family": None,
            "font-size": 17,
            "color": (255, 255, 255),

            "font-subpixel-aa": False
        }

        self._closeButton = closeButton

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 15, 0, 7)
        self.setLayout(self.layout)
        
        self.titlewdt = QWidget()
        self.titlelyt = QHBoxLayout()
        self.titlelyt.setContentsMargins(0, 0, 0, 0)
        self.titlewdt.setLayout(self.titlelyt)
        self.layout.addWidget(self.titlewdt, alignment=Qt.AlignTop)

        self.title = text
        self.titleLbl = QLabel("""<span style='font-size:17px; font-family:SimSun;
            font-weight: bold; color:rgb(255,255,255);'>%s</span>""" % text)
        self.titlelyt.addWidget(self.titleLbl, alignment=Qt.AlignCenter)

        self._icon = None
        if icon is not None:
            self.setIcon(icon)

        self.conwdt = QWidget()
        self.conlyt = QVBoxLayout()
        self.conlyt.setContentsMargins(5, 0, 0, 0)
        self.conlyt.setAlignment(Qt.AlignTop)
        self.conwdt.setLayout(self.conlyt)
        self.layout.addWidget(self.conwdt, alignment=Qt.AlignTop)

        self.close_btn = StyledButton("✕")
        self.layout.addWidget(self.close_btn, alignment=Qt.AlignHCenter | Qt.AlignBottom)
        self.close_btn.setFixedSize(40, 40)
        self.close_btn.setStyleDict({
            "border-color": (0, 0, 0, 0),
            "background-color": (0, 0, 0, 0),
            "font-size": 18,
            "color": (255, 255, 255, 200),
            "border-radius": 100,
        })
        self.close_btn.setStyleDict({
            "background-color": (255, 255, 255, 8),
            "color": (255, 255, 255, 255)
        }, "hover")
        self.close_btn.setStyleDict({
            "background-color": (255, 255, 255, 15),
            "color": (255, 255, 255, 147)
        }, "press")
        self.close_btn.clicked.connect(self.fall)

        self.risen = False
        self.hide()
        self.anim = AnimationHandler(self, 0, 1, Animation.easeOutQuart)
        self.anim.speed = speed
        
        self.customContent()    # 填充内容

    # 自定义内容
    def customContent(self):     
        self.conlyt.addWidget(QLabel('''<p style='font-size:17px; font-family:SimSun;
            color:rgb(255,255,255);'>挂机方案</p>'''),alignment=Qt.AlignHCenter)
        self.switch_plan = SegmentedButton(radio=True)
        self.switch_plan.setFixedSize(110, 100)
        self.switch_plan.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 122, 255),
            "border-radius": 4,
            "color": (0, 122, 255),
            "font-family": "SF Pro Display",
            "font-size": 18,
            "font-subpixel-aa": True
        })
        self.switch_plan.setStyleDict({
            "color": (107, 178, 255),
        }, "hover")
        self.switch_plan.setStyleDict({
            "background-color": (0, 122, 255),
            "color": (255, 255, 255),
        }, "press")
        self.switch_plan.setStyleDict({
            "background-color": (61, 154, 255),
            "color": (255, 255, 255),
        }, "check-hover")
        self.switch_plan.addButton("御魂")
        self.switch_plan.addButton("突破")
        self.switch_plan.addButton("困28")
        self.conlyt.addWidget(self.switch_plan, alignment=Qt.AlignHCenter | Qt.AlignTop)
        self.conlyt.addSpacing(5)

        self.button_shortcut = CustomButton('快捷方式', QSS.linkIcon)
        self.button_shortcut.setFixedSize(105, 30)
        self.button_shortcut.setStyleDict({
            "font-family": "SimSun",
            "font-size": 16,
            "color": (18, 150, 219),
            "border-width": 1,
            "border-color": (0, 122, 255)
        })
        self.conlyt.addWidget(self.button_shortcut, alignment=Qt.AlignHCenter)

        self.button_poweroff = CustomButton('退出', QSS.poweroffIcon)
        self.button_poweroff.setFixedSize(105, 30)
        self.button_poweroff.setStyleDict({
            "font-family": "SimSun",
            "font-size": 16,
            "color": (18, 150, 219),
            "border-width": 1,
            "border-color": (0, 122, 255)
        })
        self.conlyt.addWidget(self.button_poweroff, alignment=Qt.AlignHCenter)

    def rise(self, duration):
        if self.risen: return

        self.anim.type = track.easeOutQuart
        self.duration = duration
        self.risen = True
        self.anim.start()
        self.show()
        self.raise_()
        self.update()

    def fall(self):
        if not self.risen: return

        self.anim.type = track.easeInQuart
        self.anim.start(reverse=True)
        self.risen = False
        self.update()

    def setStyleDict(self, styledict):
        for k in styledict:
            self.styleDict[k] = styledict[k]

    def setIcon(self, icon):
        if self._icon is not None:
            self._icon.deleteLater()

        if isinstance(icon, str):
            self._icon = ImageBox(icon)
        else:
            self._icon = icon
        self._icon.setFixedSize(20, 20)
        if self.title:
            self.titlelyt.insertWidget(0, self._icon, alignment=Qt.AlignCenter)
            self.titlelyt.removeItem(self.titlelyt.itemAt(1))
            self.titlelyt.addWidget(self.titleLbl, alignment=Qt.AlignVCenter | Qt.AlignLeft)
        else:
            self.conlyt.insertWidget(0, self._icon, alignment=Qt.AlignCenter)

    def setIconSize(self, width, height):
        self._icon.setFixedSize(width, height)

    def setTitle(self, text):
        self.titleLbl.setText(text)

    def resizeEvent(self, event):
        w = self.width()
        h = self.height()
        self.setGeometry(0, 0, w, h)

    def update(self):
        self.anim.update()
        super().update()

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing, on=True)

        plt = self.titleLbl.palette()
        plt.setColor(self.titleLbl.foregroundRole(), QColor(*self.styleDict["color"]))
        self.titleLbl.setPalette(plt)

        fnt = self.titleLbl.font()
        fnt.setPixelSize(self.styleDict["font-size"])
        if not self.styleDict["font-subpixel-aa"]: fnt.setStyleStrategy(QFont.NoSubpixelAntialias)
        if self.styleDict["font-family"]: fnt.setFamily(self.styleDict["font-family"])
        self.titleLbl.setFont(fnt)

        pt.setPen(QPen(QColor(0, 0, 0, 0)))
        pt.setBrush(QBrush(QColor(*self.styleDict["background-color"])))
        r = self.styleDict["border-radius"]
        if r > self.height() / 2: r = self.height() / 2

        pt.drawRoundedRect(0, 0, self.width(), self.height(), r, r)

        pt.end()

        if not self.anim.done():
            w = self.width()
            h = self.height()
            ww = self.parent().width()
            #—————————————————————————————以下参数需要修改—————————————————————————————#
            self.setGeometry((1 - self.anim.current()) * (ww - 65), 5, w, h)
            # self.setFixedSize(self.anim.current() * 150 + 0.01, self.anim.current() * 220 + 0.01)

        if not self.anim.done():
            self.update()
        else:
            if self.isVisible() and not self.risen: self.hide()

'''
@note: 加个鼠标状态(箭头和手)
'''
class CustomButton(StyledButton):
    def __init__(self, text=None, icon=None):
        super().__init__(text, icon)

    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        self.anim_hover.start()
        self._hover = True

        if not self.isChecked():
            self._was_checked = False

    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        self.anim_hover.start(reverse=True)
        self._hover = False

        if not self.isChecked():
            self._was_checked = False

class CustomToast(Toast):
    def __init__(self, parent, text=None, icon=None):
        super().__init__(parent, text, icon)

