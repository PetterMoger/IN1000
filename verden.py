from rutenett import Rutenett
from celle import Celle

class Verden:
    def __init__(self, rader, kolonner):
        self._rutenett = Rutenett(rader, kolonner)
        self._generasjonsnummer = 0
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()
        self._rader = rader
        self._kolonner = kolonner

    def tegn(self):
        self._rutenett.tegn_rutenett()
        print("Generasjonsnummer:", self._generasjonsnummer)
        print("Antall levende celler:", self._rutenett.antall_levende())

    def oppdatering(self):
        # tell antall naboer
        alleCeller = self._rutenett.hent_alle_celler()
        for celle in alleCeller:
                celle.tell_levende_naboer()
        
        # oppdater i henhold til antall naboer
        for rad in range(self._rader):
            for kol in range(self._kolonner):
                self._rutenett.hent_celle(rad, kol).oppdater_status()
        
        # oppdater generasjonsnummer
        self._generasjonsnummer += 1