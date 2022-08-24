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

class Number(Enum):
    UNDECIDED = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    ELEVEN = 11
    TWELVE = 12
    THIRTEEN = 13
    FOURTEEEN = 14
    FIFTEEN = 15

class Country(Enum):
    ENGLAND = "England"
    FRANCE = "France"
    SCOTLAND = "Scotland"
    WALES= "Wales"
    IRELAND = "Ireland"
    ITALY = "Italy"

POSITION_MAP = {
    Number.ONE: Position.PROP,
    Number.TWO: Position.HOOKER,
    Number.THREE: Position.PROP,
    Number.FOUR: Position.SECOND_ROW,
    Number.FIVE: Position.SECOND_ROW,
    Number.SIX: Position.BACK_ROW,
    Number.SEVEN: Position.BACK_ROW,
    Number.EIGHT: Position.BACK_ROW,
    Number.NINE: Position.SCRUM_HALF,
    Number.TEN: Position.FLY_HALF,
    Number.ELEVEN: Position.WING,
    Number.TWELVE: Position.CENTRE,
    Number.THIRTEEN: Position.CENTRE,
    Number.FOURTEEEN: Position.WING,
    Number.FIFTEEN: Position.FULLBACK
}

@dataclass
class Player:
    first_name: str
    last_name: str
    country: Country
    position: Position
    price: float
    is_playing: bool
    is_starting: bool
    number: Number = Number.UNDECIDED

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} country={self.country.name} price={self.price} position={self.position.name}"
