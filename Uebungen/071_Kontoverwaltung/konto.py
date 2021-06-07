class Konto:
    def __init__(self, anfangswert=0, zins=0, dispogrenze=0):
        """
        Erstellt ein Konto-Objekt
        :param anfangswert: Wert des Kontos bei Eröffnung
        :param zins:        Zinsatz des Kontos in Prozent
        :param dispogrenze: Maximaler Überziehungswert
        """
        self.anfangswert = anfangswert
        self.zins = zins
        self.dispogrenze = dispogrenze
        self.kapital = anfangswert

    def stand(self):
        """
        Gibt des aktuellen Kapitalwert des Kontos zurück.
        :return: Kapitalwert
        """
        return self.kapital

    def einzahlung(self, wert):
        """
        Tätigt eine Einzahlung. Der Kapitalwert steigt.
        Bei Beträgen kleiner Null wird eine ValueError-Exception geworfen.
        :param wert: Einzahlungsbetrag
        :return: None
        """
        if wert < 0:
            raise ValueError('Wert muss großer oder gleich Null sein')
        self.kapital += wert

    def auszahlung(self, wert):
        """
        Tätigt eine Auszahlung.
        Dabei wird das Dispolimit nicht unterschritten. Falls doch, wird der Auszahlungswert entsprechend gekürzt.
        Bei Beträgen kleiner Null wird eine ValueError-Exception geworfen.

        :param wert: Auswahlungswunsch
        :return: Wirklicher Auswahlungsbetrag
        """

        if wert < 0:
            raise ValueError('Wert muss großer oder gleich Null sein')

        neg_dispogrenze = -self.dispogrenze  # marze hesab

        neuerKontoStand = self.kapital - wert  # meghdar jadid = meghdare feeli - vajh
        if self.kapital < neg_dispogrenze:
            wert = 0
        elif neuerKontoStand < neg_dispogrenze:
            wert = self.kapital - neg_dispogrenze

        self.kapital -= wert
        return wert

    def periodenAbschluss(self):
        """
        Führt einen Periodenabschluss durch. Dabei wird der Zins dem Konto gutgeschrieben.
        Der einfachheithalber wird davon ausgegangen, dass das vorhandene Kapital für die gesamte
        Periode auf dem Konto war.
        :return: None
        """

        self.kapital += self.kapital * self.zins * 100

    def sparPlan(self, K, N):
        """
        Ausführung eines Sparplans über mehrere Perioden.
        Das Kapital K wird dabei immer am Anfang der Periode dem Konto gutgeschrieben
        und am Ende der Periode wird ein Periodenabschluss durchgeführt.

        :param K: Kaptial pro Periode
        :param N: Anzahl der Perioden
        :return:
        """

        if N < 0: #todo inja dare chi mishe?
            raise ValueError()

        for i in range(N):
            self.einzahlung(K)
            self.periodenAbschluss()
