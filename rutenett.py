from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()

    def _lag_tomt_rutenett(self):
        rutenett = []
        for rad in range(self._ant_rader):
            rutenett.append(self._lag_tom_rad())
        return rutenett

    def _lag_tom_rad(self):
        radListe = []
        for kol in range(self._ant_kolonner):
            radListe.append(None)
        return radListe

    def fyll_med_tilfeldige_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self.lag_celle(rad, kol)

    def lag_celle(self, rad, kol):
        celle = Celle()
        randomTall = randint(0,2)
        if randomTall == 0:
            celle.sett_levende()
        self._rutenett[rad][kol] = celle
        
    def hent_celle(self, rad, kol):
        if rad in range(self._ant_rader) and kol in range(self._ant_kolonner):
            return self._rutenett[rad][kol]
        return None
    
    def tegn_rutenett(self):
        for rad in range(self._ant_rader):
            print(end="\n")
            for kol in range(self._ant_kolonner):
                print(self.hent_celle(rad, kol).hent_status_tegn(), end="")
        print(end="\n")
    
    def _sett_naboer(self, rad, kol):
        celle = self.hent_celle(rad, kol)
        for differanseRader in range(-1, 2):
            radIndeks = rad + differanseRader
            for differanseKolonner in range(-1, 2):
                kolonneIndeks = kol + differanseKolonner
                # sjekker at ikke fokalcellen blir med i listen. Heller ikke celler utenfor rutenettet. 
                if differanseRader == 0 and differanseKolonner == 0:
                    continue
                if radIndeks < 0 or kolonneIndeks < 0 or radIndeks >= self._ant_rader or kolonneIndeks >= self._ant_kolonner:
                    continue
                
                tmpCelle = self.hent_celle(radIndeks, kolonneIndeks)
                celle._naboer.append(tmpCelle)
            
    def koble_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self._sett_naboer(rad, kol)


    def hent_alle_celler(self):  
        alleCeller = []
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                alleCeller.append(self.hent_celle(rad, kol))
        return alleCeller
        
    def antall_levende(self):
        antallLevende = 0
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                tmpCelle = self.hent_celle(rad, kol)
                if tmpCelle.er_levende():
                    antallLevende += 1
        return antallLevende