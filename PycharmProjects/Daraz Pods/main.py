import requests
import cloudscraper
import random
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import lxml
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
URL = "https://www.daraz.pk/products/tws-i358763147-s1972715081.html?spm=a2a0e.searchlist.list.13.29d45323WWB37u&search=1"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 "
                  "Safari/537.36",
    "x-https": "on",
    "X-Forwarded-For": "92.38.148.58",
    "Accept-Encoding": "gzip, deflate, br",
    "x-forwarded-proto": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "upgrade-insecure-requests": "1"
}
browser = {
    "browser": "chrome",
    "platform": "windows",
    "desktop": True
}
driver = webdriver.Chrome()
new = ChromeDriverManager().install()
driver.get(URL)
print(driver)
