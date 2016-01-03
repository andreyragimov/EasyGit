import sys

from PyQt5.QtWidgets import QApplication

# app should be created before view or any other vidget
app = QApplication(sys.argv)
from controllers import navigation

if __name__ == '__main__':
    view = navigation.view
    frame = view.page().mainFrame()
    printer = navigation.Pages()
    view.setHtml(navigation.html)
    frame.addToJavaScriptWindowObject('printer', printer)
    #frame.evaluateJavaScript("alert('Hello');")
    frame.evaluateJavaScript("printer.text('Goooooooooo!');")
    #frame.evaluateJavaScript('document.getElementById("test).innerHTML = "xD"')
    view.show()
    app.exec_()