# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *



class Canvas(QWidget):
    def __init__(self, callback_repaint, callback_mouseclick):
        super().__init__()
        self.callback_repaint = callback_repaint
        self.callback_mouseclick = callback_mouseclick


    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        
        painter = QPainter(self)
        self.callback_repaint(width, height, painter, self.parent())

    def mousePressEvent(self, e):
        if (e.button() == Qt.LeftButton):
            self.callback_mouseclick(e.x(), e.y(), self.width(), self.height(), self.parent())
            
        self.update()
        


        
        
    
class App(QWidget):
    thickBlackPen = QPen(Qt.black, 4)
    bluePen = QPen(Qt.blue, 3)
    redPen = QPen(Qt.red, 3)
    greenPen = QPen(Qt.green, 3)

    def __init__(self, callback_repaint, callback_init, callback_mouseclick):
        super().__init__()
        
        self.callback_init = callback_init
        self.initPending = True

        self.status = QLabel("")
        self.canvas = Canvas(callback_repaint, callback_mouseclick)
        self.status = QLabel("Status")
        self.restartbtn = QPushButton("Neu starten")
        self.restartbtn.clicked.connect(self.restart)


        layout = QVBoxLayout()
        layout.addWidget(self.restartbtn, stretch=0)
        layout.addWidget(self.canvas, stretch=1)
        layout.addWidget(self.status, stretch=0)
        self.setLayout(layout)

        self.setWindowTitle("TicTacToe")
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(400, 400)
        self.show()        

    def restart(self):
        self.callback_init(self)
        self.update()

    def showEvent(self, e):
        if not self.initPending:
            return
        
        self.callback_init(self)
        self.initPending = False

    def setStatus(self, msg):
        self.status.setText(msg)

window = None
firststatus = ""
def run(**argv):
    global window
    app = QApplication(sys.argv)
    window = App(**argv)
    window.setStatus(firststatus)
    sys.exit(app.exec_())

def status(msg):
    global firststatus
    if window is None:
        firststatus = msg
    else:
        window.setStatus(msg)


if __name__=='__main__':
    def callback_repaint(w, h, painter, window):
        painter.setPen(thickBlackPen)

        painter.drawLine(10,10,100,140)

        painter.setPen(Qt.blue)
        painter.drawRect(120,10,80,80)

        rectf = QRectF(230.0,10.0,80.0,80.0)
        painter.drawRoundedRect(rectf,20,20)

        p1 = [QPoint(10,100),QPoint(220,110),QPoint(220,190)]
        painter.drawPolyline(QPolygon(p1))

        p2 = [QPoint(120,110),QPoint(220,110),QPoint(220,190)]
        painter.drawPolygon(QPolygon(p2))

            
        
    def f(window):
        print("init")
        
    def callback_mouseclick(x,y, w, h, window):
        print("Click", x, y)
        
    run(callback_repaint = callback_repaint, callback_init = f, callback_mouseclick=callback_mouseclick)