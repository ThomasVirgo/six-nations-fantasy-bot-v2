from typing import List
from .player import Country, Player

class LineUp:

    def __init__(self, country: Country) -> None:
        self.country = country
        self.players: List[Player] = []
    
    def add_player(self, player: Player):
        self.players.append(player)
    
    def __str__(self) -> str:
        rtn = ""
        for p in self.players:
            rtn += f"\n{p.__str__()}"
        return rtn