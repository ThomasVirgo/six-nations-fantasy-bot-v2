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



if __name__ == '__main__':
    unittest.main()