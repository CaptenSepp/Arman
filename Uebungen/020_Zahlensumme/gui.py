# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys

class App(QWidget):
    def __init__(self, callback):
        super().__init__()
        self.editbox = QLineEdit('5, 10, 0.001, 6e-2')
        self.resultbox = QLabel('')
        self.button = QPushButton('Berechnen')
        self.button.clicked.connect(self.calcPressed)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Kommagetrennte Zahlenliste'))
        layout.addWidget(self.editbox)
        layout.addWidget(QLabel('Summe'))
        layout.addWidget(self.resultbox)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.callback = callback
        self.setWindowTitle("Zahlen summieren")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setFixedSize(400, 200)
        
        self.calcPressed()
        
        self.show()        

    def calcPressed(self):
        value = self.editbox.text()
        result = self.callback(value)
        try:
            result = float(result)
            result = "{:.3f}".format(result)
        except (ValueError, TypeError):
            result = "ACHTUNG: Bitte eine Zahl zurückgeben!"
            
    
        self.resultbox.setText(result)
        self.resultbox.repaint()

def run(callback):
    def f(s):
        arglist = "'{}'".format(s)
        print("berechnung({})".format(arglist))
        return callback(s)
    app = QApplication(sys.argv)
    ex = App(f)
    sys.exit(app.exec_())
    
