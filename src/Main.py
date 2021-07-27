#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : main.py
@Note : 主程序入口
'''

from PyQt5.QtWidgets import QApplication
from Window import Window
import sys

def main():
    app = QApplication(sys.argv)
    on_hook = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


