from game.player import Player, Position, Country
from driver.driver import Driver
from driver.logic import Fixture
def main():
    print("----Running Main Script----")
    # driver = Driver()
    # driver.scrape_and_create_lineups()
    Fixture.from_scrape("1234")


if __name__ == "__main__":
    main()