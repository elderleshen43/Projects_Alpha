from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from PIL import ImageChops
from io import BytesIO
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import pickle
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium.webdriver.chrome.options import Options

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def login_with_basic_auth(driver, username, password, url):
    auth_url = f"http://{username}:{password}@{url}"
    driver.get(auth_url)
    print("logged in using basic auth")

driver = setup_driver()
login_with_basic_auth(driver, 'admin', 'admin', 'the-internet.herokuapp.com/basic_auth')

content = driver.find_element(By.TAG_NAME, 'p').text
print(content)
time.sleep(5)
driver.quit()
