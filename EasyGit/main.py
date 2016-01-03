import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

from views import views  # views resource file, pycharm will think it is unused

# app should be created before view or any other widget
app = QApplication(sys.argv)

from controllers import navigation

if __name__ == '__main__':
    view = navigation.view
    view.setUrl(QUrl('qrc:///index.html'))
    view.show()
    app.exec_()