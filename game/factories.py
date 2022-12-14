from pickle import FALSE
from tkinter.messagebox import NO
from typing import Optional
from game.player import Player, Country, Position
from game.squad import Squad
from faker import Faker
import random

fake = Faker()

def create_new_player(country: Optional[Country] = None, position: Optional[Position] = None):
    first_name = fake.first_name()
    last_name = fake.last_name()
    if country is None:
        country = random.choice(list(Country))
    if position is None:
        position = random.choice(list(Position))
    price = fake.pyfloat(left_digits=None, right_digits=1, positive=True, min_value=1, max_value=20)
    return Player(first_name=first_name, last_name=last_name, country=country, position=position, price=price, is_starting=False, is_playing=False)

def create_new_squad():
    squad = Squad()
    for _ in range(15):
        try: # such that dont exceed max players per country
            player = create_new_player()
            squad.add_player(player)
        except:
            pass
    return squad
