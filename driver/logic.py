from game.lineup import LineUp
from game.player import Country, Player, Position, POSITION_MAP
from tests.constants_for_testing import FIXTURES_TEST_SCRAPE

class Fixture:
    def __init__(self, home_lineup: LineUp, away_lineup: LineUp) -> None:
        self.home_lineup = home_lineup
        self.away_lineup = away_lineup
    
    def is_playing(self, number: str):
        n = int(number)
        if n <= 15: return True
        return False
    
    @classmethod
    def from_scrape(cls, scrape):
        scrape = FIXTURES_TEST_SCRAPE
        countries = set(c.value for c in Country)
        country_prev = None
        country = None
        lineup = None
        lineups = []
        for x in scrape:
            if x[0] in countries:
                country = Country(x[0])
                if country != country_prev:
                    if lineup is not None: lineups.append(lineup)
                    lineup = LineUp(country)
                country_prev = country
                continue
            try:
                if len(x) == 3:
                    number, first_name, last_name = x
                    lineup.add_player(Player(first_name, last_name, country, POSITION_MAP[number], True, cls.is_playing(cls, number), number))
                    continue
                number, first_name = x[:2]
                last_name = " ".join(x[2:])
                lineup.add_player(Player(first_name, last_name, country, POSITION_MAP[number], True, cls.is_playing(cls, number), number))
            except Exception as e:
                print(e)
        lineups.append(lineup)
        home_lineup = lineups[0]
        away_lineup = lineups[1]
        return cls(home_lineup, away_lineup)
