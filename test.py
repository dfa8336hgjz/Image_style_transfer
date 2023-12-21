from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QMainWindow
from PyQt5.QtCore import Qt, QRunnable, pyqtSlot, pyqtSignal, QThread, QObject
from PyQt5.QtGui import QPixmap, QImage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Push me!', self)
        self.setCentralWidget(self.button)

        print('main running in:', QThread.currentThread())
        self.worker = Worker()
        thread = QThread(self)
        self.worker.moveToThread(thread)
        thread.start()
        self.button.clicked.connect(self.worker.do_something_slow)
        self.worker.change_text.connect(self.display_changes)

    @pyqtSlot(str)
    def display_changes( self, text ):
        self.button.setText(text)

class Worker(QObject):
    change_text = pyqtSignal(str)

    @pyqtSlot()
    def do_something_slow( self ):
        print('Slot doing stuff in:', QThread.currentThread())
        import time
        time.sleep(5)
        self.change_text.emit('I did something')