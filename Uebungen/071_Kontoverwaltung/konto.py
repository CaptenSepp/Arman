class Konto:
    def __init__(self, anfangswert = 0, zins = 0, dispogrenze = 0):
        """
        Erstellt ein Konto-Objekt
        :param anfangswert: Wert des Kontos bei Eröffnung
        :param zins:        Zinsatz des Kontos in Prozent
        :param dispogrenze: Maximaler Überziehungswert
        """
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def stand(self):
        """
        Gibt des aktuellen Kapitalwert des Kontos zurück.
        :return: Kapitalwert
        """
        return 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def einzahlung(self, wert):
        """
        Tätigt eine Einzahlung. Der Kapitalwert steigt.
        Bei Beträgen kleiner Null wird eine ValueError-Exception geworfen.
        :param wert: Einzahlungsbetrag
        :return: None
        """
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def auszahlung(self, wert):
        """
        Tätigt eine Auszahlung.
        Dabei wird das Dispolimit nicht unterschritten. Falls doch, wird der Auszahlungswert entsprechend gekürzt.
        Bei Beträgen kleiner Null wird eine ValueError-Exception geworfen.

        :param wert: Auswahlungswunsch
        :return: Wirklicher Auswahlungsbetrag
        """
        return 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def periodenAbschluss(self):
        """
        Führt einen Periodenabschluss durch. Dabei wird der Zins dem Konto gutgeschrieben.
        Der einfachheithalber wird davon ausgegangen, dass das vorhandene Kapital für die gesamte
        Periode auf dem Konto war.
        :return: None
        """
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def sparPlan(self, K, N):
        """
        Ausführung eines Sparplans über mehrere Perioden.
        Das Kapital K wird dabei immer am Anfang der Periode dem Konto gutgeschrieben
        und am Ende der Periode wird ein Periodenabschluss durchgeführt.

        :param K: Kaptial pro Periode
        :param N: Anzahl der Perioden
        :return:
        """

#
#
#               HIER KOMMT IHRE LÖSUNG
#
#
