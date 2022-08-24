from typing import List
from .player import Player, Country
from .constants import MAX_PLAYERS_PER_TEAM


class Squad:
    def __init__(self, players: List[Player] = []) -> None:
        self.players = players
    
    def __str__(self) -> str:
        rtn = ""
        for player in self.players:
            rtn += f"\n{player.__str__()}"
        return rtn

    def add_player(self, player:Player):
        num_players_for_country = self.number_of_players_for_country(player.country)
        if num_players_for_country >= MAX_PLAYERS_PER_TEAM: 
            raise ValueError(f"This country already has {MAX_PLAYERS_PER_TEAM}")
        self.players.append(player)

    @property
    def total_price(self):
        total = 0
        for player in self.players:
            total += player.price
        return total
    
    def number_of_players_for_country(self, country: Country):
        total = 0
        for player in self.players:
            if player.country == country: total += 1
        return total
    
    def check_players_from_each_team(self):
        players_per_team = {}
        for country in Country:
            players_per_team[country] = 0
        for player in self.players:
            players_per_team[player.country] += 1
        for country in Country:
            if players_per_team[country] > MAX_PLAYERS_PER_TEAM:
                raise ValueError(f"{country.name} has more than 4 players, this is not allowed")
        return players_per_team
