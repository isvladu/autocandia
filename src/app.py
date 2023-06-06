import os
import sys
import typing
import logging
from PyQt6 import QtCore
import log

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        
        self.setFixedSize(QSize(800, 600))
        
        self.setCentralWidget(button)
        
    def button_clicked(self):
        logger.info("Clicked!")
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()