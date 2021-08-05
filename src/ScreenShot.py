#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : ScreenShot.py    
@Note : 截图功能类
'''

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, qAbs, QRect
from PyQt5.QtGui import QPen, QPainter, QColor, QGuiApplication

class CaptureScreen(QWidget):
    # 初始化变量
    beginPosition = None
    endPosition = None
    fullScreenImage = None
    captureImage = None
    isMousePressLeft = None
    painter = QPainter()

    def __init__(self):
        super(QWidget, self).__init__()
        self.initWindow()   # 初始化窗口
        self.captureFullScreen()    # 获取全屏

    def initWindow(self):
        self.setMouseTracking(True)     # 鼠标追踪
        self.setCursor(Qt.CrossCursor)  # 设置光标
        self.setWindowFlag(Qt.FramelessWindowHint)  # 窗口无边框
        self.setWindowState(Qt.WindowFullScreen)    # 窗口全屏

    def captureFullScreen(self):
        self.fullScreenImage = QGuiApplication.primaryScreen().grabWindow(QApplication.desktop().winId())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.beginPosition = event.pos()
            self.isMousePressLeft = True
        if event.button() == Qt.RightButton:
            # 如果选取了图片,则按一次右键开始重新截图
            if self.captureImage is not None:
                self.captureImage = None
                self.paintBackgroundImage()
                self.update()
            else:
                self.close()

    def mouseMoveEvent(self, event):
        if self.isMousePressLeft is True:
            self.endPosition = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        self.endPosition = event.pos()
        self.isMousePressLeft = False

    def mouseDoubleClickEvent(self, event):
        if self.captureImage is not None:
            self.saveImage()
            self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if self.captureImage is not None:
                self.saveImage()
                self.close()

    def paintBackgroundImage(self):
        shadowColor = QColor(0, 0, 0, 100)  # 黑色半透明
        self.painter.drawPixmap(0, 0, self.fullScreenImage)
        self.painter.fillRect(self.fullScreenImage.rect(), shadowColor)     # 填充矩形阴影

    def paintEvent(self, event):
        print(222)
        self.painter.begin(self)    # 开始重绘
        self.paintBackgroundImage()
        penColor = QColor(30, 144, 245)     # 画笔颜色
        self.painter.setPen(QPen(penColor, 1, Qt.SolidLine, Qt.RoundCap))    # 设置画笔,蓝色,1px大小,实线,圆形笔帽
        if self.isMousePressLeft is True:
            pickRect = self.getRectangle(self.beginPosition, self.endPosition)   # 获得要截图的矩形框
            self.captureImage = self.fullScreenImage.copy(pickRect)         # 捕获截图矩形框内的图片
            self.painter.drawPixmap(pickRect.topLeft(), self.captureImage)  # 填充截图的图片
            self.painter.drawRect(pickRect)     # 画矩形边框
        self.painter.end()  # 结束重绘

    def getRectangle(self, beginPoint, endPoint):
        pickRectWidth = int(qAbs(beginPoint.x() - endPoint.x()))
        pickRectHeight = int(qAbs(beginPoint.y() - endPoint.y()))
        pickRectTop = beginPoint.x() if beginPoint.x() < endPoint.x() else endPoint.x()
        pickRectLeft = beginPoint.y() if beginPoint.y() < endPoint.y() else endPoint.y()
        pickRect = QRect(pickRectTop, pickRectLeft, pickRectWidth, pickRectHeight)
        # 避免高度宽度为0时候报错
        if pickRectWidth == 0:
            pickRect.setWidth(2)
        if pickRectHeight == 0:
            pickRect.setHeight(2)

        return pickRect

    def saveImage(self):
        self.captureImage.save('picture.png', quality=95)

# from PyQt5.QtWidgets import QWidget,QFileDialog
# from PyQt5.QtCore import Qt,QRect,QRectF,QPoint
# from PyQt5.QtGui import QPainterPath,QPainter,QPen,QColor
#
# class ScreenShot(QWidget):
#     def __init__(self, parent):
#         super(ScreenShot, self).__init__()
#         # 属性
#         self.pw = parent
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowFlags(Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground, True)
#
#     def paintEvent(self, event):
#         backPath = QPainterPath()
#         backPath.addRect(0, 0, self.width(), self.height())
#         fillPath = QPainterPath()
#         if hasattr(self, "startPoint") and hasattr(self, "endPoint"):
#             movePath = QPainterPath()
#             movePath.addRect(QRectF(self.startPoint, self.endPoint))
#             fillPath = backPath.subtracted(movePath)
#         else:
#             fillPath = backPath
#         # 创建绘图设备
#         painter = QPainter(self)
#         painter.begin(self)
#         # 绘制背景图
#         painter.drawImage(QPoint(0, 0), self.backImg)
#         painter.setPen(QPen(QColor(87, 170, 255), 5, Qt.SolidLine))
#         painter.drawPath(fillPath)
#         # 填充非选择区域
#         painter.fillPath(fillPath, QColor(0, 0, 0, 100))
#         painter.end()
#
#     def mousePressEvent(self, event):
#         # 鼠标左键按下记录矩形开始点
#         if event.button() == Qt.LeftButton:
#             self.startPoint = event.pos()
#             self.isLeftPress = True
#         else:
#             self.isLeftPress = False
#
#     def mouseMoveEvent(self, event):
#         # 鼠标左键按下记录矩形结束点
#         if hasattr(self, "isLeftPress") and self.isLeftPress:
#             self.endPoint = event.pos()
#             self.repaint()
#
#     def mouseReleaseEvent(self, event):
#         # 鼠标左键按下记录矩形结束点
#         if event.button() == Qt.LeftButton:
#             self.endPoint = event.pos()
#             self.isLeftPress = False
#             self.repaint()
#
#     def keyReleaseEvent(self, event):
#
#         # esc键关闭窗口
#         if event.key() == Qt.Key_Escape:
#             self.close()
#             # 父窗口恢复显示
#             self.parentWin.showNormal()
#         # enter键(数字键盘为Key_Enter)返回主窗口识图
#         elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
#             if not (self.startPoint.x() == self.endPoint.x() and self.startPoint.y() == self.endPoint.y()):
#                 image = self.backImg.copy(QRect(self.startPoint, self.endPoint))
#                 self.close()
#                 # 父窗口恢复显示
#                 self.parentWin.showNormal()
#                 self.parentWin.childWinCallBack(image)
#         # space键保存选择区域为图片
#         elif event.key() == Qt.Key_Space:
#             if not (self.startPoint.x() == self.endPoint.x() and self.startPoint.y() == self.endPoint.y()):
#                 filePath, fileType = QFileDialog.getSaveFileName(self, "保存截图", "./",
#                                                                  "jpg图片 (*.jpg);;bmp图片(*.bmp);;png图片(*.png)")
#                 if filePath.strip() != "":
#                     image = self.backImg.copy(QRect(self.startPoint, self.endPoint))
#                     image.save(filePath)
#                     self.close()
#                     # 父窗口恢复显示
#                     self.parentWin.showNormal()
