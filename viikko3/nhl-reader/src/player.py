class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        #return self.name
        #return f"{self.name:20} team {self.team}  goals {self.goals} assists {self.assists}"
        #return f"{self.name:20} {self.team} {self.goals:2} + {self.assists:2} = {self.goals + self.assists:2}"
        return f"{self.name:25} {self.team} {str(self.goals):>2} + {str(self.assists):>2} = {str(self.goals + self.assists):>2}"

