from game.player import Player, Position, Country
def main():
    player = Player("t", "v", Country.ENGLAND, Position.FLY_HALF, 100, False, False)
    print(Position.HOOKER.name)
    print(Country.ENGLAND.value)
    print("----Running Main Script----")


if __name__ == "__main__":
    main()