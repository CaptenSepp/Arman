def readData(fn):
    with open(fn) as fd:
        result = fd.readlines()
    return result


def extractData(datalines):
    print(datalines)
    Vin, Vout = [], []

    headings = datalines[0].rstrip('\n')
    headings = headings.split('\t')
    VinIndex = headings.index('V(in)')
    VoutIndex = headings.index('V(out)')

    datalines.pop(0)
    for dl in datalines:
        VinValue = dl.split('\t')[VinIndex]
        Vin.append(float(VinValue))

        VoutValue = dl.split('\t')[VoutIndex]
        Vout.append(float(VoutValue))
    return {'Vin': Vin, 'Vout': Vout}


def calcAmplification(data):                                                                #

    if len(data['Vin']) != len(data['Vout']):
        raise ValueError()
    # Vin = data['Vin']
    # Vin.sort()
    # VinMin = Vin[0]
    # VinMax = Vin[-1]
    # VinDiff = VinMax - VinMin
    VinMax = max(data['Vin'])
    VinMin = min(data['Vin'])
    VinDiff = VinMax-VinMin

    VoutMax = max(data['Vout'])
    VoutMin = min(data['Vout'])
    VoutDiff = VoutMax-VoutMin

    vu = VoutDiff/VinDiff

    return vu, (VinMin, VinMax), (VoutMin, VoutMax)



def outputResult(fn, vu, Vin_minmax, Vout_minmax):
    print(fn, vu)



if __name__ == '__main__':                                                                          #
    fn = "daten/schaltung.txt"

    datalines = readData(fn)
    data = extractData(datalines)
    vu, Vin_minmax, Vout_minmax = calcAmplification(data)
    outputResult(fn, vu, Vin_minmax, Vout_minmax)
