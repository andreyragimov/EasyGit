#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWindow = QWidget()
    MainWindow.resize(250, 150)
    MainWindow.move(300, 300)
    MainWindow.setWindowTitle('Happy New Year!')
    MainWindow.show()

    sys.exit(app.exec_())
