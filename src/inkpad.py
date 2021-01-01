from PyQt5 import QtWidgets, QtCore, QtGui
from main_ui import Ui_main_window

class Inkpad(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.actionNew.triggered.connect(self.new_file_event)
        self.actionOpen.triggered.connect(self.open_file_event)

    def new_file_event(self):
        new_tab = QtWidgets.QWidget()
        gridLayout = QtWidgets.QGridLayout(new_tab)
        new_text_edit = QtWidgets.QPlainTextEdit(new_tab)
        new_text_edit.viewport().setProperty("cursor",
                                             QtGui.QCursor(QtCore.Qt
                                                           .IBeamCursor))
        new_text_edit.setMouseTracking(False)
        new_text_edit.setDocumentTitle("")
        new_text_edit.setPlainText("")
        new_text_edit.setOverwriteMode(False)
        new_text_edit.setBackgroundVisible(False)
        new_text_edit.setPlaceholderText("Start Typing...")
        gridLayout.addWidget(new_text_edit, 0, 0, 1, 2)
        self.content_tab.addTab(new_tab, "Untitled*")

    def open_file_event(self):
        file_path, _ = (QtWidgets.QFileDialog
                        .getOpenFileName(self, "Open File",
                                         QtCore.QDir.homePath(),
                                         "All Files (*);;Text Files (*.txt)"))

        with open(file_path, 'r') as opened_file:
            self.content_edit.setPlainText(opened_file.read())

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = Inkpad()
    MainWindow.show()
    app.exec_()
