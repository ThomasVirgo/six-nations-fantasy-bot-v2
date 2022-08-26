import time
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By

from game.lineup import LineUp
from game.player import Country, POSITION_MAP, Player
from .logic import Fixture

class Driver:
    def __init__(self) -> None:
        self.driver = webdriver.Safari()
        self.driver.maximize_window()
        self.lineups: List[LineUp] = []

    def get_page(self, page:str):
        self.driver.get(page)
        time.sleep(2)

    def finish(self):
        self.driver.close()
    
    def scrape_fixtures(self) -> List[Fixture]:
        self.get_page("https://www.sixnationsrugby.com/fixtures/")
        fixtures = self.driver.find_elements(By.CSS_SELECTOR, '[title^="Preview"]')
        fixtures = fixtures[:3] # 3 games each week
        fixture_urls = [fixture.get_attribute("href") + "#teams" for fixture in fixtures]
        fixture_urls = ["https://www.sixnationsrugby.com/report/conway-at-the-double-as-ireland-defeat-wales-in-dublin#teams"]
        fixtures: List[Fixture] = []
        for url in fixture_urls:
            self.get_page(url)
            player_divs = self.driver.find_elements(By.CLASS_NAME, "ta-left")
            text_lists: List[List[str]] = [div.text.split() for div in player_divs] # see PLAYER_DIVS_LISTS in constants
            fixture = Fixture.from_scrape(text_lists)
            fixtures.append(fixture)
        self.finish()
        return fixtures