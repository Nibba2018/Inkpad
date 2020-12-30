from PyQt5 import QtWidgets
from PyQt5 import QtCore
from main_ui import Ui_main_window

class Inkpad(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = Inkpad()
    MainWindow.show()
    app.exec_()
