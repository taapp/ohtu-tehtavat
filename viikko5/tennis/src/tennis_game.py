class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def score_component_to_str(self, score):
        score_component_to_str_dict = {
            0: 'Love',
            1: 'Fifteen',
            2: 'Thirty',
            3: 'Forty'
        }
        return score_component_to_str_dict[score]

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_score_even()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_score_not_even_at_least_four()
        return self.get_score_not_even_less_than_four()

    def get_score_not_even_less_than_four(self):
        return f"{self.score_component_to_str(self.m_score1)}-{self.score_component_to_str(self.m_score2)}"

    def get_score_not_even_at_least_four(self):
        difference_score = self.m_score1 - self. m_score2
        status_str = 'Advantage player' if abs(difference_score)==1 else "Win for player"
        player_str = '1' if difference_score > 0 else "2"
        return status_str + player_str
    
    def get_score_even(self):
        if self.m_score1 > 3:
            return "Deuce"
        return f"{self.score_component_to_str(self.m_score1)}-All"
