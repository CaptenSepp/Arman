# -*- coding: utf-8 -*-

import sys

import matplotlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class App(QWidget):
    def __init__(self, plotFunction):
        super().__init__()
        self.plotFunction = plotFunction

        layout = QVBoxLayout()

        self.mplcanvas = MplCanvas()
        layout.addWidget(self.mplcanvas)

        temp = QHBoxLayout()
        temp.addWidget(QLabel("Polynomgrad"))
        self.PolyN = QSpinBox()
        temp.addWidget(self.PolyN)

        temp.addWidget(QLabel("x0"))
        self.Polyx0 = QSlider(Qt.Horizontal)

        temp.addWidget(self.Polyx0)

        self.fktselect = QComboBox()
        self.fktselect.addItem("sin(x)")
        self.fktselect.addItem("exp(x)")
        temp.addWidget(self.fktselect)

        temp.addStretch()
        layout.addLayout(temp)

        self.setLayout(layout)
        self.setWindowTitle("Demo Taylorreihen")
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(800, 400)
        self.show()

        self.PolyN.setValue(3)
        self.Polyx0.setValue(53)
        self.Polyx0.setMinimum(-100)
        self.Polyx0.setMaximum(+100)

        self.Polyx0.valueChanged.connect(self.parameterChanged)
        self.PolyN.valueChanged.connect(self.parameterChanged)
        self.fktselect.currentTextChanged.connect(self.parameterChanged)
        self.parameterChanged()

    def parameterChanged(self, *args):
        x0 = float(self.Polyx0.value()) / 10
        N = int(self.PolyN.value())
        name = self.fktselect.currentText()

        ax = self.mplcanvas.ax
        ax.cla()
        self.plotFunction(ax, x0, N, name)
        self.mplcanvas.draw()


def run(*argv):
    app = QApplication(sys.argv)
    window = App(*argv)
    sys.exit(app.exec_())


if __name__ == '__main__':
    import numpy as np


    def plotFunction(ax, x0, N, fktname):
        x = np.linspace(x0 - 4, x0 + 4)
        if fktname == 'sin(x)':
            y = np.sin(x)
        elif fktname == 'exp(x)':
            y = np.exp(x)
        else:
            y = x

        ax.plot(x, y, label=fktname)
        ax.legend()


    run(plotFunction)
