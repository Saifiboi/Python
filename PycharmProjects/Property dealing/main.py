from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class RealEstate:
    def __init__(self):
        chrome_driver_path = "C:/Users/Safi/Development/chromedriver-win64/chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        # options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        options.add_experimental_option("excludeSwitches", ['enable-logging'])
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.soup = ""
        self.driver.implicitly_wait(5)

    def find_homes(self):
        sleep(50)
        self.driver.get(
            url="https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C"
                "%22mapBounds%22%3A%7B%22north%22%3A37.90218348133198%2C%22east%22%3A-122.25136844042969%2C%22south"
                "%22%3A37.64818226220822%2C%22west%22%3A-122.61529055957031%7D%2C%22isMapVisible%22%3Atrue%2C"
                "%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C"
                "%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value"
                "%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C"
                "%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B"
                "%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId"
                "%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A11%7D")
        self.driver.maximize_window()
        sleep(10)
        flag = True
        while flag:
            All_data = self.driver.find_elements(by=By.XPATH,
                                                    value='//div[@id="grid-search-results"]/ul/li[not(p)]')
            print(len(All_data))
            try:
                address = [data.find_element(by=By.TAG_NAME, value="address").text for data in All_data]
                prices = [data.find_element(by=By.CSS_SELECTOR, value="span[class='PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr']").text for data in All_data]
                links = [data.find_element(by=By.TAG_NAME, value="a").get_attribute("href") for data in All_data]

            except (StaleElementReferenceException, NoSuchElementException):
                # Scroll down to load more results step by step
                self.scroll_down_smoothly(All_data[-1])
                sleep(5)  # Adjust this time as needed
            else:
                flag = False
        sleep(50)
        # # new_data = (links, address, prices)
        # print(All_data)
        # print(len(All_data))

    def scroll_down_smoothly(self, element):
        actions = ActionChains(self.driver)
        # Move the mouse to the last element
        actions.move_to_element(element)
        actions.perform()
        # Scroll down gradually by sending Page Down key multiple times
        num_steps = 50  # Adjust the number of steps as needed
        for _ in range(num_steps):
            actions.send_keys(Keys.PAGE_DOWN)
            actions.perform()
            sleep(3)  # Adjust this time as needed



houses = RealEstate()
houses.find_homes()
