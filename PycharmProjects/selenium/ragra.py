import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:/Users/Safi/Development/chromedriver-win64/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

store = []

cookie = driver.find_element(by=By.ID, value="cookie")

def find_store():
    global store
    store = driver.find_elements(by=By.XPATH, value='//div[@id="store"]/*')
    store.pop()
    store_price = [item.find_element(by=By.TAG_NAME, value="b").text.split("-")[1].strip().replace(",","") for item in store]
    store_price.reverse()
    return [int(price) for price in store_price]


def buy_from_store(money, store_price: list):
    for item in store_price:
        if int(money) > item:
            try:
                store[7 - store_price.index(item)].click()
            except StaleElementReferenceException:
                break


t_end = time.time() + 60 * 5
test = 1
while time.time() < t_end:
    cookie.click()
    money = driver.find_element(by=By.ID, value="money").text
    if test % 150 == 0:
        buy_from_store(money.replace(",", ""), find_store())
        test = 1
    test += 1

print(driver.find_element(by=By.ID, value="cps").text)

driver.quit()