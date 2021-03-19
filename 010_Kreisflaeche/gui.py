# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys

class App(QWidget):
    def __init__(self, callback):
        super().__init__()
        self.editbox = QLineEdit('')
        self.resultbox = QLabel('')
        self.button = QPushButton('Berechnen')
        self.button.clicked.connect(self.calcPressed)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Radius in Metern'))
        layout.addWidget(self.editbox)
        layout.addWidget(QLabel('Fläche'))
        layout.addWidget(self.resultbox)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.callback = callback
        self.setWindowTitle("Kreisfläche")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setFixedSize(400, 200)
        self.show()        

    def calcPressed(self):
        value = self.editbox.text()
        value = value.strip()
        if len(value) == 0:
            value = '0'
        try:
            value = float(value)
            result = self.callback(value)
            result = "{:.3f} qm".format(result)
        except ValueError:
            result = "Bitte Zahl eingeben!"        
    
        self.resultbox.setText(result)
        self.resultbox.repaint()

def run(callback):
    app = QApplication(sys.argv)
    ex = App(callback)
    sys.exit(app.exec_())
    
    
if __name__=='__main__':
    def f(r):
        return r
    run(f)