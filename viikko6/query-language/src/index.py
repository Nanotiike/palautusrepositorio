from statistics_1 import Statistics
from player_reader import PlayerReader
from matchers import And, Or, All, Not, PlaysIn, HasAtLeast, HasFewerThan

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher1 = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )


    matcher2 = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )

    matcher3 = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )

    matcher4 = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    matcher5 = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    matcher = matcher5

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
