from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or, QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    #matcher = And(
    #    HasAtLeast(5, "goals"),
    #    HasAtLeast(5, "assists"),
    #    PlaysIn("PHI")
    #)
    matcher = And(
       Not(HasAtLeast(1, "goals")),
       PlaysIn("NYR")
    )
    matcher = And(
       HasFewerThan(1, "goals"),
       PlaysIn("NYR")
    )
    
    #matcher = Or(
    #    HasAtLeast(30, "goals"),
    #    HasAtLeast(50, "assists")
    #)

    matcher = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )

    query = QueryBuilder()
    #matcher = query.build()
    #matcher = query.playsIn("NYR").build()
    #matcher = query.hasAtLeast(20, "goals").build()
    #matcher = query.hasFewerThan(10, "goals").build()
    #matcher = query.playsIn("NYR").hasFewerThan(10, "goals").build()
    #matcher = query.hasFewerThan(10, "goals").playsIn("NYR").build()
    matcher = query.playsIn("NYR").hasAtLeast(5, "goals").hasFewerThan(10, "goals").build()


    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
