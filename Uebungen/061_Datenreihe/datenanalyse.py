def readData(fn):
    raise NotImplementedError  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

def extractData(datalines):
    raise NotImplementedError  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


def calcAmplification(Vin, Vout):
    raise NotImplementedError  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

def outputResult(fn, vu, Vin_minmax, Vout_minmax):
    raise NotImplementedError  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

if __name__ == '__main__':
    fn = "daten/schaltung.txt"

    datalines = readData(fn)
    Vin, Vout = extractData(datalines)
    vu, Vin_minmax, Vout_minmax = calcAmplification(Vin, Vout)
    outputResult(fn, vu, Vin_minmax, Vout_minmax)
