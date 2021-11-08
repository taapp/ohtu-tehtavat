import unittest
from statistics import Statistics
from player import Player

"""
class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def lue(self, teksti):
        return self.inputs.pop(0)

    def kirjoita(self, teksti):
        self.outputs.append(teksti)


class TestStatistics(unittest.TestCase):
    def test_yksi_summa_oikein(self):
        io = StubIO(["1", "3", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs[0], "Summa: 4")
"""


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    # ...
    def test_search_existing_player(self):
        self.assertEqual(self.statistics.search("Semenko").name, "Semenko")
    
    def test_search_non_existing_player(self):
        self.assertEqual(self.statistics.search("Kasparov"), None)

    def test_team_getting_existing_team(self):
        self.assertEqual(self.statistics.team("EDM")[2].name, "Gretzky")

    def test_team_getting_non_existing_team(self):
        self.assertEqual(len(self.statistics.team("AAA")), 0)

    def test_top_scorers_top_1(self):
        self.assertEqual(self.statistics.top_scorers(1)[0].name, "Gretzky")

    def test_top_scorers_top_5(self):
        self.assertEqual(self.statistics.top_scorers(4)[4].name, "Semenko")
