from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
mail = "belachao774@gmail.com"
password = "Aq)Kc7A@jATzBs2"
chrome_driver_path = "C:/Users/Safi/Development/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3661267631&f_AL=true&keywords=intern&refresh=true")
sleep(5)
sign_in = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sleep(5)
sign_in.click()
sleep(10)
email = driver.find_element(by=By.NAME, value="session_key")
email.send_keys(mail)
sleep(10)
email = driver.find_element(by=By.NAME, value="session_password")
email.send_keys(password)
sleep(10)
sign_btn = driver.find_element(by=By.CSS_SELECTOR, value=".login__form_action_container button")
sign_btn.submit()
sleep(50)
top_jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".scaffold-layout__list-container li")
for job in top_jobs:
    print(job.tag_name)
    sleep(5)
    link = job.find_element(by=By.TAG_NAME, value="a")
    print(link.text)
    # link.click()
    # sleep(5)
    # easy_apply_btn = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button')
    # easy_apply_btn.click()
//*[@id="ember1006"]
sleep(5)
