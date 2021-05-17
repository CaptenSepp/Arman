def readData(fn):
    with open(fn) as fd:
        result = fd.readlines()


def extractData(datalines):

    print(datalines)
    Vin, Vout = [], []

    heading = datalines[0].split('\t')
    VinIndex = heading.index('V(in')

    for dl in datalines:
        VinValue = dl.split('\t')[VinIndex]
        Vin.append(float(VinValue))
    return {}


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
