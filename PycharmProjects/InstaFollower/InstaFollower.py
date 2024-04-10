from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class InstaFollower:
    def __init__(self):
        chrome_driver_path = "C:/Users/Safi/Development/chromedriver-win64/chromedriver.exe"
        service = Service(executable_path=chrome_driver_path)
        options = Options()
        options.add_argument("window-size=1200x600")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(10)
        fb = self.driver.find_element(by=By.XPATH, value="//span[@class='_ab37']")
        fb.click()
        sleep(15)
        email = self.driver.find_element(by=By.NAME, value="email")
        sleep(5)
        email.send_keys("saifurrehman1357@gmail.com")
        sleep(5)
        password = self.driver.find_element(by=By.NAME, value="pass")
        sleep(5)
        password.send_keys("Saifi118266")
        sleep(5)
        login_btn = self.driver.find_element(by=By.ID, value="loginbutton")
        login_btn.submit()
        sleep(50)

    def find_followers(self):
        sleep(20)
        search = self.driver.find_element(by=By.XPATH,
                                          value="//span[contains(text(),'Search')]")

        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(search).click(search).perform()
        search_bar = self.driver.find_element(by=By.XPATH, value="//input[@placeholder='Search']")
        search_bar.send_keys("Chefsteps")
        sleep(5)
        page = self.driver.find_element(by=By.XPATH,
                                        value="//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x1roi4f4 x10wh9bi x1wdrske x8viiok x18hxmgj']//span[@class='x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft'][normalize-space()='ChefSteps']")
        sleep(5)
        page.click()
        sleep(5)
        followers = self.driver.find_element(by=By.XPATH, value="//span[contains(text(),'265K')]")
        sleep(5)
        followers.click()
        sleep(10)
        follower_accounts = self.driver.find_element(by="css selector", value='div._aano')
        sleep(12)
        for _ in range(100):
            follower = self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",
                                                  follower_accounts)
            sleep(5)

    def follow(self):
        sleep(5)
        buttons = self.driver.find_elements(by=By.TAG_NAME, value="Button")
        for button in buttons:
            print(button.text)
            sleep(12)


follow = InstaFollower()
follow.login()
follow.find_followers()
follow.follow()
