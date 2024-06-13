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

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.shirttuning.cz/")
    base_url = driver.current_url
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print("HTML CODE OF SITE GOT SUCCESFULLY")

    links = soup.find_all('a')
    print(f"found{len(links)} links on page.")

    bad_links = []

    if links:
        for link in links:
            href = link.get('href')
            if href:
                if not(href.startswith('http://') or href.startswith('https://')):
                    href = urljoin(base_url, href)

                print("checking link", href)
                try:
                    response = requests.get(href, timeout=5)
                    print(f"code answer for link {href}: {response.status_code}")
                    if response.status_code != 200:
                        bad_links.append(href)
                        print(f"link not available, status code {href}.")
                    else:
                        print("link available")
                except requests.Timeout:
                    print(f"timeout during link verification {href}.")
                    bad_links.append(href)
                except Exception as e:
                    print(f"mistake during checking link {href} mistake {str(e)}")
                    bad_links.append(href)
    else:
        print("links not found on page")

    if bad_links:
        print("unavailable links:")
        for bl in bad_links:
            print(bl)
    else:
        print("all links on site available")
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
"""
    for link in links:
        href = link.get('href')
        print("test", href)
        try:
            response = requests.get(href, timeout=5)
            print(f"Code answer for link {href}: {response.status_code}")
            if response.status_code == 200:
                print("link availble")
            else:
                print(f"link unavailble coe: {response.status_code}")
        except requests.Timeout:
            print(f"timeout during testing of link {href}")
        except Exception as ex:
            print(f"mistake during link {href}. error code: {str(ex)}")
        if href == 'tags.html':
            tags_html_found = True
        
    else:
        print("links not found")
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
"""