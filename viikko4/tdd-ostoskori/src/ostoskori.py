from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset_ls = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        if len(self.ostokset())==0:
            return 0
        else:
            return sum([ostos.lukumaara() for ostos in self.ostokset()])

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        if len(self.ostokset())==0:
            return 0
        else:
            return sum([ostos.hinta() for ostos in self.ostokset()])

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        tuote_korissa_bool = False
        for koriostos in self.ostokset():
            if koriostos.tuotteen_nimi() == lisattava.nimi():
                koriostos.muuta_lukumaaraa(1)
                tuote_korissa_bool = True
                break
        if not tuote_korissa_bool:
            ostos = Ostos(lisattava)
            self.ostokset().append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for koriostos in self.ostokset():
            if koriostos.tuotteen_nimi() == poistettava.nimi():
                koriostos.muuta_lukumaaraa(-1)
                if koriostos.lukumaara() == 0:
                    self.ostokset().remove(koriostos)
                break

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._ostokset_ls = []

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self._ostokset_ls
