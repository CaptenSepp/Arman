import datetime
import logging
import os
import sys
import zipfile
import globals
from pathlib import Path

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *

import json

PROGRAMVERSION = globals.versionstr

class GuiLogger(logging.Handler):
    def emit(self, record):
        datestr = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        if record.levelname == "ERROR":
            msg = '<span style="color:red;">{}</span>'.format(self.format(record))
        else:
            msg = self.format(record)

        html = '<span style="font-family: Courier New"> <b>{}</b> {} </span> <br>'.format(datestr, msg)
        self.logWidget.printText(html)


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

h = GuiLogger()
h.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
log.addHandler(h)

class LoggingTextWidget(QTextEdit):
    printTextSignal = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.printTextSignal.connect(self._printText)
    def printText(self, html):
        self.printTextSignal.emit(html)

    def _printText(self, html):
        self.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
        self.textCursor().insertHtml(html)

class ConfigAwareLineEdit(QLineEdit):
    def __init__(self, config, name):
        self.config = config
        self.name = name
        super().__init__(config.get(name, ''))

    def keyPressEvent(self, e):
        result = super().keyPressEvent(e)
        self.config[self.name] = self.text()
        return result

class ConfigAwareCheckBox(QCheckBox):
    def __init__(self, label, config, name):
        super().__init__(label)
        self.config = config
        self.name = name
        self.setChecked(self.config.get('komptest', False))
        self.stateChanged.connect(self.change)

    def change(self, state):
        self.config[self.name] = (state == 2)


class App(QFrame):
    CONFIGFILENAME = 'config.json'
    def __init__(self):
        basedir = os.path.dirname(os.path.realpath(__file__))
        self.CONFIGFILENAME = os.path.join(basedir, self.CONFIGFILENAME)
        super().__init__()
        self.logWidget = LoggingTextWidget()
        self.logWidget.setFontFamily("Courier New")
        self.logWidget.setLineWrapMode(0)

        h.logWidget = self.logWidget
        self.testPythonVersion()
        self.readConfigFile()

        self.eb_akennung = ConfigAwareLineEdit(self.config, 'akennung')
        self.eb_uid = ConfigAwareLineEdit(self.config, 'matrikelnummer')
        self.pb_Abgabe = QPushButton('Abgabe')
        self.pb_Abgabe.clicked.connect(self.abgabe)
        self.pb_Test = QPushButton('Test')
        self.pb_Test.clicked.connect(self.runTests)


        layout = QGridLayout()
        templayout = QVBoxLayout()
        templayout.addWidget(QLabel("A-Kennung"))
        templayout.addWidget(self.eb_akennung)
        layout.addItem(templayout, 1, 1)

        templayout = QVBoxLayout()
        templayout.addWidget(QLabel("Matrikelnummer"))
        templayout.addWidget(self.eb_uid)
        layout.addItem(templayout, 2, 1)


        templayout = QGridLayout()
        templayout.addWidget(self.pb_Test)
        templayout.addWidget(self.pb_Abgabe)
        layout.addItem(templayout, 1, 2, rowSpan=2)
        self.pb_Test.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.pb_Abgabe.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)


        templayout = QVBoxLayout()
        self.cb_SelectCompressedReport = ConfigAwareCheckBox("Komprimierte Darstellung der Testausgabe", self.config, 'komptest')
        templayout.addWidget(self.cb_SelectCompressedReport)
        layout.addItem(templayout, 3, 1, columnSpan=2)

        templayout = QVBoxLayout()
        templayout.addWidget(QLabel("Log Ausgabe"))
        templayout.addWidget(self.logWidget)

        layout.addItem(templayout, 4, 1, columnSpan=2)

        self.setLayout(layout)
        self.setWindowTitle("Uploader Version {}".format(PROGRAMVERSION))
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        #        self.setFixedSize(400, 200)
        self.resize(800, 600)


        self.show()

    def testPythonVersion(self):
        minor = sys.version_info.minor
        major = sys.version_info.major

        log.info("Python-Version: {}.{}".format(major, minor))

        if not (major == 3 and minor >= 8):
            log.error("Achtung!!! Dieses Programm ist getestet für Python-Version >= 3.8 !!!")


    def closeEvent(self, *args, **kwargs):
        self.writeConfigFile()
        return super().closeEvent(*args, **kwargs)
    def writeConfigFile(self):
        log.info("Schreibe Konfiguration in die Datei {}".format(self.CONFIGFILENAME))
        with open(self.CONFIGFILENAME, 'w') as fp:
            json.dump(self.config, fp)

    def readConfigFile(self):
        if not os.path.isfile(self.CONFIGFILENAME):
            log.info("Konfigurationsdatei {} existiert nicht. Erstelle leere Konfiguration".format(self.CONFIGFILENAME))
            self.config = {}
            return

        log.info("Lese Konfiguration aus der Datei {}".format(self.CONFIGFILENAME))
        with open(self.CONFIGFILENAME) as fp:
            self.config = json.load(fp)


    def runTests(self):
        import autotester
        autotester.log.addHandler(h)


        log.info("Führe für alle Aufgaben die Tests aus:")

        modules = sys.modules.copy()
        basepath = Path(__file__).parent.joinpath('..')
        try:
            html = autotester.runTest(basepath, compressedReport = self.cb_SelectCompressedReport.isChecked(),
                                      processGuiEvents=QApplication.processEvents)
        except Exception as e:
            log.error("Fehler beim Ausführen der Tests: {}".format(str(e)))
            return

        newmodules = sys.modules.copy()

        self.logWidget.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
        self.logWidget.textCursor().insertHtml(html)
        self.logWidget.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)

        for nb in newmodules:
            if nb in modules:
                continue
            log.debug("Unloading Module {}".format(nb))
            del sys.modules[nb]

    def abgabe(self):
        akennung = self.eb_akennung.text()
        akennung = akennung.strip()

        uid = self.eb_uid.text()
        uid = uid.strip()

        if len(akennung) == 0:
            log.error("Bitte geben Sie Ihre A-Kennung ein!")
            return

        if len(uid) == 0:
            log.error("Bitte geben Sie Ihre Matrikelnummer ein!")
            return

        basedirectory = os.path.dirname(__file__)
        basedirectory = os.path.join(basedirectory, "..")
        basedirectory = os.path.abspath(basedirectory)

        log.info("Basisverzeichnis: {}".format(basedirectory))
        try:
            filename = self.packfiles(basedirectory, akennung)
        except IOError as e:
            log.error(str(e))
            return
        except Exception as e:
            log.error(str(e))
            return

        try:
            self.sendzipfile(akennung, uid, basedirectory, filename)
        except Exception as e:
            log.error(str(e))
            return

    def sendzipfile(self, akennung, uid, basedirectory, filename):
        log.info("Starte Übertragung der Datei {}".format(filename))
        log.info("A-Kennung: {}".format(akennung))
        # importing the requests library
        import requests
        from requests.exceptions import ConnectionError

        def retry_on_connectionerror(max_retries=5):
            retries = 0
            while retries < max_retries:
                try:
                    req = requests.post(url=API_ENDPOINT, data=data, files=files)
                    return req
                except ConnectionError:
                    retries += 1
            raise Exception("Maximum retries exceeded")

        # defining the api-endpoint
        API_ENDPOINT = globals.uploadurl
        log.info("Nutze URL {}".format(API_ENDPOINT))

        # your API key here
        API_KEY = "12345"

        data = {'bearer': API_KEY, 'uid': uid}
        log.info('File: ' + str(filename))
        files = [('file', (filename, open(filename, 'rb'), 'zip'))]
        
        log.info("Verbinde zu Server [Dies kann etwas dauern] ...")
        QApplication.processEvents()

        r = retry_on_connectionerror(max_retries=5)
        # r = requests.post(url=API_ENDPOINT, data=data, files=files)

        if r.status_code == 200:
            log.info("Upload erfolgreich!")
        else:
            error_code = str(r.status_code)
            error_message = r.text
            import json
            try:
                error_json = json.loads(error_message)
                error_message = 'Error ' + error_code + ' - '
                error_message += error_json["error"]
            except:
                error_message = "Error!"
            log.error(error_message)

    def packfiles(self, basedirectory, akennung):
        outputdir = os.path.join(basedirectory, "Abgabenordner")
        if not os.path.exists(outputdir):
            log.info("Erstelle Abgabenordner")
            os.mkdir(outputdir)

        if not os.path.isdir(outputdir):
            raise IOError("Abgabenordner kann nicht erstellt werden.... Abbruch")

        nowstr = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
        zipfilename = "{}_{}.zip".format(nowstr, akennung)
        zipfilename = os.path.join(outputdir, zipfilename)

        log.info("Erstelle ZIP-Datei '{}'".format(os.path.relpath(zipfilename, basedirectory)))

        files = self.createFileListForArchive(basedirectory)
        zf = zipfile.ZipFile(zipfilename, mode='w')
        for fn in files:
            arcname = os.path.relpath(fn, basedirectory)

            log.debug("{} -> {}".format(fn, arcname))
            zf.write(fn, arcname)
        zf.close()

        log.info("Insgesamt wurden {} Dateien in die ZIP-Datei gespeichert".format(len(files)))

        return zipfilename

    def createFileListForArchive(self, root):
        ExcludePaths = ['__pycache__', 'venv', '.idea', 'uploader', 'Abgabenordner']
        result = list()
        for subdir, dirs, files in os.walk(root):
            path = os.path.normpath(subdir)
            pathsplit = path.split(os.sep)

            if any([x in pathsplit for x in ExcludePaths]):
                continue

            for filename in files:
                fn = os.path.join(subdir, filename)
                result.append(fn)

        return result


def run():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
