from game.player import Player, Position, Country
from driver.driver import Driver
from driver.logic import Fixture
def main():
    print("----Running Main Script----")
    # driver = Driver()
    fixture = Fixture.from_scrape("1234")
    print(fixture.home_lineup)


if __name__ == "__main__":
    main()