import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class SaveFile(QWidget):

    def __init__(self, file=''):
        super().__init__()
        self.title = 'Save File - Choose file location...'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.file = file
        self.saved = 0
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.saveFileDialog()
        
        self.close()
        
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getSaveFileName(self,"Save File","","All Files (*);;Text Files (*.txt)", options=options)
        if self.fileName:
            # print(self.fileName)
            
            with open(self.fileName, 'w') as f:
                f.write(self.file)
                self.saved = 1

class OpenFile(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Open File - Choose file location...'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.saved = 0
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.openFileDialog()
        
        self.close()
        
    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Open File","","All Files (*);;Text Files (*.txt)", options=options)
        # if self.fileName:
        #     print(self.fileName)

