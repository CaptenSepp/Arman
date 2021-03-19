# -*- coding: utf-8 -*-

import sys

import matplotlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvasX(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.set_facecolor("None")
        self.fig = fig
        self.ax = fig.add_subplot(111)
        super().__init__(fig)
        self.clear()

    def clear(self):
        self.ax.cla()
        self.ax.patch.set_alpha(0.2)

    def draw(self):
        self.fig.tight_layout()
        super().draw()


class MplCanvas(QWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = QVBoxLayout()
        self.p1 = MplCanvasX(**kwargs)
        self.p2 = MplCanvasX(**kwargs)

        layout.addWidget(self.p1)
        layout.addWidget(self.p2)
        self.setLayout(layout)

        self.ax1 = self.p1.ax
        self.ax2 = self.p2.ax
        self.clear()

    def clear(self):
        self.p1.clear()
        self.p2.clear()

    def draw(self):
        self.p1.draw()
        self.p2.draw()

class App(QWidget):
    def __init__(self, creator_object, analyzer_object):
        super().__init__()

        self.creator = creator_object
        self.analyzer = analyzer_object

        self.guielements = dict()


        layout = QVBoxLayout()
        self.uiSetupCreator(layout)
        self.uiSetupAnalyzer(layout)
        self.setLayout(layout)

        self.show()

    def uiSetupAnalyzer(self, layout):
        locallayout = QVBoxLayout()
        locallayout.addLayout(self.labeledEditBox("Eingabedatei", ".xlsx"))
        locallayout.addLayout(self.analyzerPlotWindow())
        locallayout.addLayout(self.pushButton("Analyse", self.analyzeButtonPressed))


        groupbox = QGroupBox("Datenanalyse")
        groupbox.setLayout(locallayout)
        groupbox.setStyleSheet("""
        QGroupBox {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #E0E0E0, stop: 1 #A0FFA0);
            border: 2px solid gray;
            border-radius: 5px;
            margin-top: 1ex; /* leave space at the top for the title */
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left; /* position at the top center */
            padding: 0 3px;
        }
                """);
        layout.addWidget(groupbox)

    def analyzerPlotWindow(self):
        self.mplcanvas = MplCanvas()
        self.mplcanvas.setStyleSheet("background-color:transparent;")
        layout = QVBoxLayout()
        layout.addWidget(self.mplcanvas)
        return layout


    def uiSetupCreator(self, layout):
        locallayout = QVBoxLayout()
        locallayout.addLayout(self.labeledEditBox("Abtastfrequenz", 'Hz'))
        locallayout.addLayout(self.labeledEditBox("Dauer", "s"))
        locallayout.addLayout(self.labeledEditBox("Ausgabedatei", ".xlsx"))
        locallayout.addLayout(self.labeledEditBox("Mathematischer Ausdruck (t=Zeitvariable)", internal="Ausdruck"))
        locallayout.addLayout(self.pushButton("Erzeugen", self.createButtonPressed))

        groupbox = QGroupBox("Datenerzeugung")
        groupbox.setLayout(locallayout)
        groupbox.setStyleSheet("""
QGroupBox {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #E0E0E0, stop: 1 #FFA0A0);
    border: 2px solid gray;
    border-radius: 5px;
    margin-top: 1ex; /* leave space at the top for the title */
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left; /* position at the top center */
    padding: 0 3px;
}
        """);
        layout.addWidget(groupbox)


    def pushButton(self, label, callback):
        layout = QHBoxLayout()
        pb = QPushButton(label)
        layout.addWidget(pb)
        pb.clicked.connect(callback)
        return layout

    def labeledEditBox(self, label, unit=None, internal=None):
        if internal is None:
            internal = label

        layout = QHBoxLayout()
        lbl = QLabel(label)
        lbl.setFixedWidth(250)
        layout.addWidget(lbl)
        eb = QLineEdit()
        eb.setAlignment(Qt.AlignRight)
        layout.addWidget(eb)
        lblunit = QLabel(unit)
        lblunit.setFixedWidth(40)
        layout.addWidget(lblunit)
        self.guielements[internal] = eb
        return layout

    def getEditboxText(self, label):
        return self.guielements[label].text()

    def analyzeButtonPressed(self):
        params = dict()
        for lbl in ['Eingabedatei']:
            params[lbl] = self.getEditboxText(lbl) + '.xlsx'
        params['ax1'] = self.mplcanvas.ax1
        params['ax2'] = self.mplcanvas.ax2

        try:
            self.mplcanvas.clear()
            self.analyzer.set(**params)
            self.analyzer.do()
            self.mplcanvas.draw()
        except (ValueError, FileNotFoundError) as e:
            msgbox = QMessageBox()
            msgbox.setText(str(e))
            msgbox.setIcon(QMessageBox.Critical)
            msgbox.exec();


    def createButtonPressed(self):
        params = dict()
        for lbl in ['Abtastfrequenz', 'Dauer', 'Ausgabedatei', 'Ausdruck']:
            params[lbl] = self.getEditboxText(lbl)


        try:
            params['Ausgabedatei'] = params['Ausgabedatei'] + '.xlsx'
            params['Dauer'] = float(params['Dauer'])
            params['Abtastfrequenz'] = float(params['Abtastfrequenz'])
            self.creator.set(**params)
            self.creator.do()
            msgbox = QMessageBox()
            msgbox.setText("Datei wurde erfolgreich erzeugt")
            msgbox.setIcon(QMessageBox.Information)
            msgbox.exec();
        except (ValueError, FileNotFoundError, NameError, KeyError, Exception) as e:
            msgbox = QMessageBox()
            msgbox.setText(str(e))
            msgbox.setIcon(QMessageBox.Critical)
            msgbox.exec();


def run(*argv):
    app = QApplication(sys.argv)
    window = App(*argv)

    window.guielements['Abtastfrequenz'].setText("10000")
    window.guielements['Dauer'].setText("10e-3")
    window.guielements['Ausgabedatei'].setText("output")
    window.guielements['Eingabedatei'].setText("output")
    window.guielements['Ausdruck'].setText("sin(2*pi*t*1000) + 2*sin(2*pi*t*2000)")
    sys.exit(app.exec_())


