from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:
    def __init__(self):
        service = Service(executable_Path='C:/Users/Safi/Development/chromedriver-win64')
        self.driver = webdriver.Chrome(service=service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        go_btn = self.driver.find_element(by=By.CSS_SELECTOR, value=".start-button a")
        go_btn.click()
        sleep(50)
        down_span = self.driver.find_element(by=By.CLASS_NAME, value="download-speed")
        self.down = float(down_span.text)
        up_span = self.driver.find_element(by=By.CLASS_NAME, value="upload-speed")
        self.up = float(up_span.text)
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(10)
        google = self.driver.find_element(by=By.TAG_NAME, value="input")
        sleep(5)
        google.send_keys("innominate.0b1@gmail.com")
        sleep(5)
        google.send_keys(Keys.ENTER)
        sleep(50)
        password = self.driver.find_element(by=By.NAME, value="password")
        password.send_keys("illegit99_")
        password.send_keys(Keys.ENTER)
        sleep(30)
        tweet = self.driver.find_element(by=By.XPATH,
                                         value="//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
        tweet.send_keys(f"{self.down}\n{self.up}")
        post = self.driver.find_element(by=By.XPATH, value="//span[contains(text(),'Post')]")
        print(post)
        sleep(50)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
