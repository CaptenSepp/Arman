import unittest
from pathlib import Path
import pandas as pd
import logging
import sys

log = logging.getLogger(__name__)


class TabularTestResult(unittest.TestResult):
    def __init__(self):
        super().__init__()
        self.result = []

    def startTest(self, test):
        super().startTest(test)

        Gewichtung = 1
        try:
            Gewichtung = test.Gewichtung
        except:
            pass

        methodname = test._testMethodName
        aufgabe = test.__class__.__module__.split('.')[0]
        self.result.append({'Aufgabe': aufgabe, 'test': methodname, 'StatusText':'Failed', 'Punkte': 0, 'Maxpunkte': 1, 'Gewichtung': Gewichtung})

    def addError(self, test, err):
        log.error("Fehler im Modul {}".format(test))
        self.result[-1]['StatusText'] = 'ERROR'
        
    def addSuccess(self, test):
        super().addSuccess(test)
        self.result[-1]['Punkte'] = 1
        self.result[-1]['StatusText'] = 'OK'

    def addFailure(self, test, err):
        super().addFailure(test, err)
        try:
            self.result[-1]['StatusText'] = test.UploaderHint
        except:
            pass


    def toDataframe(self):
        df = pd.DataFrame(self.result)
        return df

    def toCompressedHtmlTable(self):
        rowTemplate = ('<tr style="margin-top: 10px;">'
                       '<td style="">{aufgabe}</td>'
                       '<td style="align:right;background-color:{bkcolor}">{punkte}</td>'
                       '<td style="align:right;background-color:{bkcolor}">{maxpunkte}</td>'
                       '</tr>'
                       ).format

        df = self.toDataframe()

        df = df.groupby('Aufgabe').agg({'Punkte': 'sum', 'Maxpunkte': 'sum', 'Gewichtung': 'mean'})
        df = df.reset_index()
        tableRows = []
        f = lambda row: self._htmlrow(tableRows, row, rowTemplate)
        df.apply(f, axis=1)
        heading = "<tr><th>Aufgabe</th><th>Punkte</th><th>Max. Punkte</th></tr>"
        html = '<table style="border: 1px solid black"> {} {} </table>'.format(heading, ' '.join(tableRows))
        return html

    def toHtmlTable(self):
        rowTemplate = ('<tr style="margin-top: 10px;">'
                       '<td style="">{aufgabe}</td>'
                       '<td style="align:right;background-color:{bkcolor}">{testmethode}</td>'
                       '<td style="align:right;background-color:{bkcolor}">{statustext}</td>'
                       '</tr>'
                       ).format

        df = self.toDataframe()

        #        df = df.groupby('Aufgabe').agg({'Punkte': 'sum', 'Maxpunkte': 'sum', 'Gewichtung': 'mean'})
        df = df.reset_index()
        tableRows = []
        f = lambda row: self._htmlrow(tableRows, row, rowTemplate)
        df.apply(f, axis=1)
        heading = "<tr><th>Aufgabe</th><th>Testname</th><th>Status</th></tr>"
        html = '<table style="border: 1px solid black"> {} {} </table>'.format(heading, ' '.join(tableRows))
        return html

    def _htmlrow(self, tableRows, dfRow, rowTemplate):
        Punkte = dfRow['Punkte'] * dfRow['Gewichtung']
        Maxpunkte = dfRow['Maxpunkte'] * dfRow['Gewichtung']
        StatusText = dfRow.get('StatusText', '')
        if Punkte == Maxpunkte:
            bkcolor = 'lightgreen'
        elif Punkte > 0:
            bkcolor = 'yellow'
        elif Punkte == 0:
            bkcolor = 'salmon'

        if StatusText == 'ERROR':
            bkcolor = 'red'

        tableRow = rowTemplate(aufgabe = dfRow['Aufgabe'],
                               testmethode = dfRow.get('test', ''),
                               punkte = Punkte, maxpunkte = Maxpunkte,
                               statustext = StatusText, bkcolor=bkcolor)
        tableRows.append(tableRow)

    def __str__(self):
        df = self.toDataframe()
        df = df.groupby('Aufgabe').sum()
        return df.to_string()

def runTest(basepath, compressedReport):

    result = TabularTestResult()

    for subpath in filter(lambda f: f.is_dir(), basepath.iterdir()):
        if not subpath.joinpath('__init__.py').is_file():
            continue
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        tests = loader.discover(str(subpath), top_level_dir=str(basepath))
        suite.addTests(tests)
        suite.run(result)
        removeModulesFromSysWhichContain(subpath.name)

    if compressedReport:
        return result.toCompressedHtmlTable()
    else:
        return result.toHtmlTable()

def removeModulesFromSysWhichContain(pathfragment):
    keyToRemove = list()
    for modA, modB in sys.modules.items():
        try:
            modfilename = modB.__file__
            if modfilename is None:
                continue
        except AttributeError:
            continue

        if pathfragment in modfilename:
            keyToRemove.append(modA)

    for key in keyToRemove:
        del sys.modules[key]



if __name__ == '__main__':
    basepath = Path(__file__).parent.joinpath('..')

    result = runTest(basepath)
    with open('output.html', 'w') as fd:
        fd.write(result)