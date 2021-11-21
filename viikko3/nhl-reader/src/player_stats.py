class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        players_new = [x for x in self.players if x.nationality == nationality]
        players_new = sorted(players_new, key=lambda y: y.goals + y.assists, reverse=True)
        return players_new
