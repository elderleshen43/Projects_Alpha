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