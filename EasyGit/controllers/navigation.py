#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWebKitWidgets import QWebView

view = QWebView()

html = """
<html>
<body>
    <h1>Hello!</h1><br>
    <h2><a href="#" onclick="printer.text('Message from QWebView')">QObject Test</a></h2>
    <h2><a href="#" onclick="document.getElementById('test').innerHTML = printer.xd('msg')">JS test</a></h2>
    <div id="test">1</div>
</body>
</html>
"""


class Pages(QObject):
    def __init__(self, parent=None):
        super(Pages, self).__init__(parent)

    @pyqtSlot(str)
    def text(self, message):
        print(message)

    @pyqtSlot(str, result=str)
    def xd(self, message):
        return "xD"


