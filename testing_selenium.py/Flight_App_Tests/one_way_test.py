from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://localhost:5173/")
time.sleep(5)
wait = WebDriverWait(driver, 10)
#departure_box = driver.find_element(By.XPATH, "//a[@class ='EndDate']")
arrival_city = driver.find_element(By.XPATH, "//a[@href='/city/to']")
NULLdeparture_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Zpět"]')))
return_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='StartDate']")))
departure_city = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/city/from']")))
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='Buttons-list__change']")))
passenger_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class=''][@href='/passengers-count']")))

# test case TC_FT_01
# picks deparute city and arrival city
try:

    departure_city.click()
    time.sleep(5)

    city_picker_search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='CityPickerSearch']")))
    city_picker_search.click()
    time.sleep(3)
    city_picker_search.send_keys("Bulharsko")

    time.sleep(3)
    city_picker_search.send_keys(Keys.RETURN)
    time.sleep(3)
    

    article_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//article[.//span[contains(text(), 'Bulharsko')]]")))
    article_element.click()
    time.sleep(3)
    

    aside_element = wait.until(EC.element_to_be_clickable((By.XPATH, "(//aside)[2]")))
    aside_element.click()
    time.sleep(3)
    
    arrival_city_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Praha')]")))
    arrival_city_element.click()
    time.sleep(3)
    city_picker_search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='CityPickerSearch']")))
    city_picker_search.click()
    time.sleep(5)
    city_picker_search.send_keys("Rakousko")
    city_picker_search.send_keys(Keys.RETURN)
    time.sleep(3)
    
    article_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//article[@class='CountryName'][div/span[text()='Rakousko']]")))
    article_element.click()
    time.sleep(2)
    aside_element = wait.until(EC.element_to_be_clickable((By.XPATH, "(//aside)[1]")))
    aside_element.click()
    time.sleep(3)
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='Buttons-list__change']")))
    search_button.click()
    time.sleep(3)


except TimeoutException as ex:
    print("Timeout waiting for element:", ex)

except Exception as ex:
    print("An error occurred:", ex)

finally: 
    driver.quit()