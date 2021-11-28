KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Virhe: kapasiteetti ei ole kokonaisluku tai se on negatiivinen") 
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Virhe: kasvatuskoko ei ole kokonaisluku tai se on negatiivinen") 
        else:
            self.kasvatuskoko = kasvatuskoko

        self._alusta_ljono(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def _alusta_ljono(self, koko):
        self.ljono = [0] * koko

    def kuuluu(self, n):
        kuuluu_bool = False

        for i in range(self.alkioiden_lkm):
            if n == self.ljono[i]:
                kuuluu_bool = True
        return kuuluu_bool

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.kasvata_kokoa()

            return True

        return False

    def kasvata_kokoa(self):
        taulukko_old = self.ljono
        self.kopioi_taulukko(self.ljono, taulukko_old)
        self._alusta_ljono(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.ljono)

    def poista(self, n):
        kohta = self.etsi_alkion_indeksi(n)
        if kohta != -1:
            self.ljono[kohta] = 0
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.ljono[j]
                self.ljono[j] = self.ljono[j + 1]
                self.ljono[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def etsi_alkion_indeksi(self,n):
        indeksi = -1
        for i in range(self.alkioiden_lkm):
            if n == self.ljono[i]:
                indeksi = i
                break
        return indeksi

    def kopioi_taulukko(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [self.ljono[i] for i in range(self.alkioiden_lkm)]

    @staticmethod
    def yhdiste(a, b):
        return IntJoukko._joukko_operaatio(a, b, 'yhdiste')

    @staticmethod
    def leikkaus(a, b):
        return IntJoukko._joukko_operaatio(a, b, 'leikkaus')

    @staticmethod
    def erotus(a, b):
        return IntJoukko._joukko_operaatio(a, b, 'erotus')

    @staticmethod
    def _joukko_operaatio(a, b, tyyppi):
        joukko_uusi = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        if tyyppi=='leikkaus':
            for i in range(len(a_taulu)):
                for j in range(len(b_taulu)):
                    if a_taulu[i] == b_taulu[j]:
                        joukko_uusi.lisaa(b_taulu[j])

        if tyyppi=='yhdiste':
            for i in range(len(a_taulu)):
                joukko_uusi.lisaa(a_taulu[i])
            for i in range(len(b_taulu)):
                joukko_uusi.lisaa(b_taulu[i])

        if tyyppi=='erotus':
            for i in range(len(a_taulu)):
                joukko_uusi.lisaa(a_taulu[i])
            for i in range(len(b_taulu)):
                joukko_uusi.poista(b_taulu[i])
        
        return joukko_uusi


    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            merkkijono = ""
            for i in range(self.alkioiden_lkm - 1):
                merkkijono = merkkijono + str(self.ljono[i])
                merkkijono = merkkijono + ", "
            merkkijono = merkkijono + str(self.ljono[self.alkioiden_lkm - 1])
            return "{" + merkkijono + "}"
