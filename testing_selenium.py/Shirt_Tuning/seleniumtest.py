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
from accounts import shirttuning_pass, shirttuning_email
# brrrrr
def capture_element_screenshot(driver, locator):
    try:
        element = driver.find_element(*locator)

        screenshot = element.screenshot_as_png
        image_stream = BytesIO(screenshot)
        cropped_image = Image.open(image_stream)

        return cropped_image
    
    except NoSuchElementException:
        print("Unable to locate element:", locator)
        return None
    
def compare_images(image1, image2):
    threshold = 20

    if image1.size != image2.size:
        return False
 
    diff = ImageChops.difference(image1, image2)
    diff = diff.convert('L')

    for pixel in diff.getdata():
        if pixel > threshold:
            return False

    return True

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get(url="https://www.shirttuning.cz/")
    time.sleep(3)
    cookies_button = driver.find_element(By.XPATH, "//button[text()='Povolit vše']").click()
    time.sleep(2)
    """"
    with open("shirt_tuning_cookies", "rb") as file:
        cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(3)
    driver.refresh()
    time.sleep(5)
    expected_name = "Pán peter griffin"
    actual_name = driver.find_element(By.XPATH, "//span[@data-bind='text: customer().fullname']").text
    if expected_name == actual_name:
        print("yahooo")
    else:
        print("boohoo")

    """
    """

    login_popup = driver.find_element(By.XPATH, "//span[normalize-space(text())='Přihlášení']")
    login_button = driver.find_element(By.XPATH, "//a[text()='Přihlásit se']")
    actions = ActionChains(driver)
    actions.move_to_element(login_popup)
    actions.click(login_button)
    actions.perform()
    time.sleep(3)
    login_input = driver.find_element(By.XPATH, "//input[@name= 'login[username]']")
    pass_input = driver.find_element(By.XPATH, "//input[@name= 'login[password]']")
    login_input.send_keys(shirttuning_email)
    pass_input.send_keys(shirttuning_pass)
    pass_input.send_keys(Keys.ENTER)
    time.sleep(2)
    pickle.dump(driver.get_cookies(), open("shirt_tuning_cookies", "wb"))    
    time.sleep(3)
    
    """
    
except Exception as ex:
    print(ex)

try:
    kreator_button = driver.find_element(By.XPATH, "//a[text()= 'Kreátor']").click()
    time.sleep(5)
    pridej_text = driver.find_element(By.NAME, "_rect153").click()    
    time.sleep(4)
    textbox = driver.find_element(By.XPATH, "//textarea[@class='sRobotoRegular']")
    textbox.send_keys("STEWIE STINKS")
    time.sleep(3)
    locator = (By.NAME, "_rect179")
    element_screensot = capture_element_screenshot(driver, locator)
    if element_screensot:
        element_screensot.save("actual_shirt_text.png")
    source_image = Image.open("expected_shirt_text.png")
    test_image = Image.open("actual_shirt_text.png")
    if compare_images(source_image, test_image):
        print("yahooo")
    else:
        print("boohoo")
    
except Exception as ex:
    print(ex)

try:
    first_span = driver.find_element(By.XPATH, "//span[text()='Doručení do 5-7 dnů']").click()
    time.sleep(2)
    locator = (By.XPATH, "//div[@class='deliveryPopup popUp openedPopup']")
    element_screensot = capture_element_screenshot(driver, locator)
    if element_screensot:
        element_screensot.save("firstbanneract.png")
    source_image = Image.open("firstbannerexp.png")
    test_image = Image.open("firstbanneract.png")
    if  compare_images(source_image, test_image):
        print("yahooo")
    else:
        print("boohoo")

    close_button = driver.find_element(By.XPATH, "//i[@class='material-icons closeAll']").click()
    time.sleep(2)
    second_span = driver.find_element(By.XPATH, "//span[text()='Množstevní slevy do výše 50%']").click()
    time.sleep(2)
    locator = (By.XPATH, "//div[@class='rabattPopup popUp openedPopup']")
    element_screensot = capture_element_screenshot(driver, locator)
    if element_screensot:
        element_screensot.save("secondbanneract.png")
    source_image = Image.open("secondbannerexp.png")
    test_image = Image.open("secondbanneract.png")
    if  compare_images(source_image, test_image):
        print("yahooo")
    else:
        print("boohoo")

    
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
    