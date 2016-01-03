import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

from views import views  # views resource file, pycharm will think it is unused

from models import test_model
# app should be created before view or any other widget (and importing navigation)
app = QApplication(sys.argv)

from controllers import navigation

view = navigation.view
loader = navigation.Loader()
foo = test_model.Foo()


def create_js_acces():
    models_to_js()
    controllers_to_js()


def models_to_js():
    view.page().mainFrame().addToJavaScriptWindowObject('foo', foo)


def controllers_to_js():
    view.page().mainFrame().addToJavaScriptWindowObject('loader', loader)

if __name__ == '__main__':
    view.page().mainFrame().javaScriptWindowObjectCleared.connect(create_js_acces)

    view.setUrl(QUrl('qrc:///index.html'))
    view.show()
    app.exec_()
