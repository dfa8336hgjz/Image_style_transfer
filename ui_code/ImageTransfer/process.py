import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtCore import Qt
from ui_code.ui import *

class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.ui.style1.clicked.connect(self.update) # type: ignore
        self.ui.style2.clicked.connect(self.update) # type: ignore
        self.ui.style3.clicked.connect(self.update) # type: ignore
        self.ui.style4.clicked.connect(self.update) # type: ignore
        self.ui.pushButton.clicked.connect(self.update) # type: ignore
        self.ui.otherstyle.clicked.connect(self.chooseStyleImg) # type: ignore
        self.ui.actionOpen.triggered.connect(self.chooseOriginalImg)
    
    def update(self):
        sender = self.sender()
        self.ui.styleImg.setStyleSheet("border-image: url(:styles/" + sender.path + ");\n")

    def chooseStyleImg(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Images (*.png *.jpg)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filename = dialog.selectedFiles()
            self.ui.styleImg.setStyleSheet("border-image: url(" + filename[0] + ");\n")

    def chooseOriginalImg(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Images (*.png *.jpg)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filename = dialog.selectedFiles()
            self.ui.originalImg.setStyleSheet("border-image: url(" + filename[0] + ");\n")
        
    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PyQt events with keyboard')
        self.show()
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainUI()
    sys.exit(app.exec_())