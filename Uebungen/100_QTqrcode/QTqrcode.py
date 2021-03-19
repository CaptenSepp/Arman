import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import qrcode  #Bitte pip3 install qrcode auführen!
from PIL.ImageQt import ImageQt

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("qrCode")
        self.setGeometry(50, 50, 550, 550)
        # ERSTELLEN DER ELEMENTE

        # Ein Label erstellen, dass den QRcode darstellen kann

        # LineEdit erstellen und bei Textänderung
        # mit der Funktion generate_code verknüpfen

        # Button erstellen und mit der
        # Funktion save_qrcode verknüpfen

        # Ein Label erzeugen für die StatusBar zum Darstellen
        # des Status beim Speichern

        # LAYOUT QBoxLayouts sollen verwendet werden
        #   ------------
        #   |    ##    |    # Label Zentriert
        #   |    ##    |
        #   |          |    # Platz flexibel (stretch)
        #   | <======> |    # Input Feld
        #   |  <save>  |    # Speichern Button
        #   ------------    # StatusBar

        # Das Label mit dem QRCode soll ganz oben mittig stehen.
        # Der Platz zwischen dem QRCode soll gestreckt werden bis zu
        # den übrigen Elementen am unteren Rand.
        # Das Textfeld soll die ganze Breite nutzen
        # Der Button soll mittig stehen
        # Die StatusBar (StatusLabel) soll ganz unten stehen
        
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def generate_code(self, text):
        text = qrcode.make(text)
        self.my_code.setPixmap(QPixmap.fromImage(ImageQt(text)))

    def save_qrcode(self):
        img = qrcode.make(self.my_input.text())
        try:
            img.save('qrcode.png')
            #   Setzen Sie den Status im StatusLabel für den Erfolgsfall
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#
        except:
            pass
            #   Setzen Sie den Status im StatusLabel für den Fehlerfall
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
