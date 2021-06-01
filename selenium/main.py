from logging import exception
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager

class GoogleKeywordScreenshoter():
    def __init__(self, keyword, screenshots_dir):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir

    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        shitty_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"g-blk")))
        self.browser.execute_script(
            """
        const shitty = arguments[0];
        shitty.parentElement.removeChild(shitty)
        """,
            shitty_element,
        )
        search_results = self.browser.find_elements_by_class_name("g")
        for index, results in enumerate(search_results):
            results.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index}.png")
    def finish(self):
        self.browser.quit()

domain_competitor = GoogleKeywordScreenshoter("buy domain","screenshots")
domain_competitor.start()
domain_competitor.finish() 
        
        


