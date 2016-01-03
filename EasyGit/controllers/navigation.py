#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWebKitWidgets import QWebView

view = QWebView()
frame = view.page().mainFrame()  # todo check is it changing


class Loader(QObject):
    def __init__(self):
        QObject.__init__(self)

    @pyqtSlot(str)
    def load(self, url):
        view.setUrl(QUrl('qrc:///' + url))
        print("url changed to:" + url)

    @pyqtSlot(str, result=str)
    def xd(self, message):
        return "xD"

