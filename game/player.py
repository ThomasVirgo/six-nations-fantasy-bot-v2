from dataclasses import dataclass
from enum import Enum

class Position(Enum):
    PROP =  "Prop",
    HOOKER = "Hooker",
    SECOND_ROW = "Second-row",
    BACK_ROW = "Back-row",
    SCRUM_HALF = "Scrum-half",
    FLY_HALF = "Fly-half",
    WING = "Wing",
    CENTRE = "Centre",
    FULLBACK = "Fullback"
    BENCH = "Bench"

class Country(Enum):
    ENGLAND = "England"
    FRANCE = "France"
    SCOTLAND = "Scotland"
    WALES= "Wales"
    IRELAND = "Ireland"
    ITALY = "Italy"

POSITION_MAP = {
    "1": Position.PROP,
    "2": Position.HOOKER,
    "3": Position.PROP,
    "4": Position.SECOND_ROW,
    "5": Position.SECOND_ROW,
    "6": Position.BACK_ROW,
    "7": Position.BACK_ROW,
    "8": Position.BACK_ROW,
    "9": Position.SCRUM_HALF,
    "10": Position.FLY_HALF,
    "11": Position.WING,
    "12": Position.CENTRE,
    "13": Position.CENTRE,
    "14": Position.WING,
    "15": Position.FULLBACK,
    "16": Position.BENCH,
    "17": Position.BENCH,
    "18": Position.BENCH,
    "19": Position.BENCH,
    "20": Position.BENCH,
    "21": Position.BENCH,
    "22": Position.BENCH,
    "23": Position.BENCH,
}

@dataclass
class Player:
    first_name: str
    last_name: str
    country: Country
    position: Position
    is_playing: bool
    is_starting: bool
    number: str
    price: float = 0

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} country={self.country.name} price={self.price} position={self.position.name}"
