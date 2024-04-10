from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_Path='C:/Users/Safi/Development/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
name = driver.find_element(by=By.ID, value="cookie")


def recur_fun():
    timeout = time.time() + 5  # 5 minutes from now
    while True:
        name.click()
        if time.time() > timeout:
            break
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#store div")))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#money")))
    new_arr = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
    money = driver.find_element(by=By.CSS_SELECTOR, value="#money").text
    str_mon = "".join(money.split(","))
    list_serv = [item for item in new_arr if item.get_attribute(name="class") != "grayed"]
    maximum = 0
    for ser in list_serv:
        try:
            moni = ser.find_element(by=By.CSS_SELECTOR, value="b").text
            new_val = moni.split('-')[1]
            new_val_prime = "".join(new_val.split(","))
            print(new_val_prime)
            if maximum < int(new_val_prime) <= int(str_mon):
                maximum = int(new_val_prime)
                max_element = ser
        except (StaleElementReferenceException, NoSuchElementException):
            pass
    try:
        if max_element is not None:
            print(max_element.click())
    except UnboundLocalError:
        pass

    recur_fun()


recur_fun()
