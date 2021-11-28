import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_korin_hinta_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        piima = Tuote("Piimä", 4)
        self.kori.lisaa_tuote(piima)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        piima = Tuote("Piimä", 4)
        self.kori.lisaa_tuote(piima)
        self.assertEqual(self.kori.hinta(), 7)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)


    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)

    # step 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostokset = self.kori.ostokset()
 
        # testaa että metodin palauttaman listan pituus 1
        self.assertEqual(len(ostokset), 1)

    # step 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
 
        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.
        self.assertEqual(ostos.tuote._nimi, "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        piima = Tuote("Piimä", 4)
        self.kori.lisaa_tuote(piima)
        ostokset = self.kori.ostokset()
 
        # testaa että metodin palauttaman listan pituus 2
        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
 
        # testaa että metodin palauttaman listan pituus 1
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), 'Maito')

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_ostosolio_jolla_oikea_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
    
        ostos = ostokset[0]
        self.assertEqual(ostos.tuotteen_nimi(), 'Maito')
        self.assertEqual(ostos.lukumaara(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_ja_yhden_poiston_jalkeen_korissa_ostos_jonka_maara_yksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()
    
        ostos = ostokset[0]
        self.assertEqual(ostos.lukumaara(), 1)

    def test_tuotteen_lisaamisen_ja_poiston_jalkeen_kori_on_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(ostokset), 0)

    def test_kahden_saman_ja_yhden_eri_tuotteen_lisaamisen_ja_korin_tyhjennyksen_jalkeen_kori_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        piima = Tuote("Piimä", 4)
        self.kori.lisaa_tuote(piima)
        self.kori.tyhjenna()
 
        ostokset = self.kori.ostokset()
        # testaa että kori on tyhjä
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(ostokset), 0)