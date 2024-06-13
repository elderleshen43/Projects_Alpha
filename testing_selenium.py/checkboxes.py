from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    checkboxes[0].click()
    time.sleep(2)
    checkboxes[1].click()
    time.sleep(2)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()