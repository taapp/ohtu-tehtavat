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
        return sum([ostos.lukumaara() for ostos in self._ostokset_ls])

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return sum([ostos.hinta() for ostos in self._ostokset_ls])

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        tuote_korissa_bool = False
        for koriostos in self._ostokset_ls:
            if koriostos.tuotteen_nimi() == lisattava.nimi():
                koriostos.muuta_lukumaaraa(1)
                tuote_korissa_bool = True
                break
        if not tuote_korissa_bool:
            ostos = Ostos(lisattava)
            self._ostokset_ls.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for koriostos in self._ostokset_ls:
            if koriostos.tuotteen_nimi() == poistettava.nimi():
                koriostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self._ostokset_ls
