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

from models import test_model


def add_loader():
    view.page().mainFrame().addToJavaScriptWindowObject('loader', loader)
    view.page().mainFrame().addToJavaScriptWindowObject('foo', foo)
    #frame.evaluateJavaScript("alert('Hello');")
    #frame.evaluateJavaScript("printer.text('Goooooooooo!');")

loader = Loader()
foo = test_model.Foo()
view.page().mainFrame().javaScriptWindowObjectCleared.connect(add_loader)