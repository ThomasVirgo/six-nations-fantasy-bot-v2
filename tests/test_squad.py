import unittest
from game.factories import create_new_squad


class TestSquad(unittest.TestCase):

    def setUp(self):
        self.squad = create_new_squad()
    
    def test_total_price(self):
        tot = 0
        for player in self.squad.players:
            tot += player.price
        self.assertEqual(tot, self.squad.total_price)
    
    def test_players_per_team(self):
        players_per_team = self.squad.check_players_from_each_team()
        self.assertIsInstance(players_per_team, dict)
        print(self.squad)



if __name__ == '__main__':
    unittest.main()