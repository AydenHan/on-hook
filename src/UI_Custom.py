#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : UI_Custom.py
@Note : 自定义类
'''

from pyqt5Custom import StyledButton,Toast,ToggleSwitch, Animation, AnimationHandler,ImageBox
from PyQt5.QtCore    import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui     import QPainter, QPen, QBrush, QColor, QFont


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
        self.setFixedSize(150,210)

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
        self.titleLbl = QLabel(text)
        self.titlelyt.addWidget(self.titleLbl, alignment=Qt.AlignCenter)

        self._icon = None
        if icon is not None:
            self.setIcon(icon)

        self.conwdt = QWidget()
        self.conlyt = QVBoxLayout()
        self.conlyt.setContentsMargins(5, 0, 0, 0)
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
        # —————————————————————————————以下参数需要修改—————————————————————————————#
        self.anim.speed = 3.3
        self.customContent()

    def customContent(self):     #自定义内容
        # self.w1 = QWidget()
        # self.w2 = QWidget()
        # self.w3 = QWidget()
        # self.conlyt.addWidget(self.w1)
        # self.conlyt.addWidget(self.w2)
        # self.conlyt.addWidget(self.w3)
        self.layout_content1 = QHBoxLayout()
        self.layout_content2 = QHBoxLayout()
        self.layout_content3 = QHBoxLayout()
        self.conlyt.addLayout(self.layout_content1)
        self.conlyt.addLayout(self.layout_content2)
        self.conlyt.addLayout(self.layout_content3)
        self.content_style = '''
            QLabel{
                color:#FFFFFF;
                font-size:18px;
                font-weight:bold;
                font-family:'SimSun';
            }'''
        self.content1 = QLabel('御魂')
        self.content2 = QLabel('突破')
        self.content3 = QLabel('困28')
        self.content1.setStyleSheet(self.content_style)
        self.content2.setStyleSheet(self.content_style)
        self.content3.setStyleSheet(self.content_style)
        self.layout_content1.addWidget(self.content1, alignment=Qt.AlignLeft)
        self.layout_content2.addWidget(self.content2, alignment=Qt.AlignLeft)
        self.layout_content3.addWidget(self.content3, alignment=Qt.AlignLeft)
        self.switch1 = ToggleSwitch(style="ios")
        self.switch2 = ToggleSwitch('', 'ios', False)
        self.switch3 = ToggleSwitch('', 'android', False)
        self.switch1.raise_()
        self.switch1.setFixedWidth(120)
        self.switch2.setFixedWidth(120)
        self.switch3.setFixedWidth(120)
        self.layout_content1.addWidget(self.switch1)
        self.layout_content2.addWidget(self.switch2)
        self.layout_content3.addWidget(self.switch3)

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
            self.titlelyt.insertWidget(0, self._icon, alignment=Qt.AlignVCenter | Qt.AlignRight)
            self.titlelyt.removeItem(self.titlelyt.itemAt(1))
            self.titlelyt.addWidget(self.titleLbl, alignment=Qt.AlignVCenter | Qt.AlignLeft)
        else:
            self.conlyt.insertWidget(0, self._icon, alignment=Qt.AlignHCenter)

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
            self.setGeometry((1 - self.anim.current()) * (ww / 2 - 65), 5, w, h)
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