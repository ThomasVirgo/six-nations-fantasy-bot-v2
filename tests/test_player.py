import unittest
from game.player import Player, Position, Country


class TestPlayer(unittest.TestCase):

    def test_string_representation(self):
        player = Player("Tom", "Virgo", Country.ENGLAND, Position.FLY_HALF, 10.1, False, False)
        expected_print = "Tom Virgo country=ENGLAND price=10.1 position=FLY_HALF"
        self.assertEqual(player.__str__(), expected_print)

if __name__ == '__main__':
    unittest.main()