"""
WebScraper.py
Scrapes the provided URL to extract the current traffic camera image url.
This is needed because the URL encodes its access tokens in it, and they change frequenty, so we can't just hardlink to the image.
"""

# Imports
import time
import io

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

from urllib.request import urlopen
from PIL import Image

def save_image(baseUrl, fileName):
    # Selenium config (Disable SSL checking so we don't get a ton of obnoxious errors, and make Selenium headless, disable logging)
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--log-level=3")
    chromeOptions.add_argument("--silent")
    chromeOptions.add_argument("--ignore-certificate-errors")
    chromeOptions.add_argument("--ignore-ssl-errors")
    chromeOptions.add_argument("--allow-running-insecure-content")
    chromeOptions.add_argument("--ignore-certificate-errors-spki-list")

    driver = webdriver.Chrome(options=chromeOptions)

    url = baseUrl

    driver.get(url)
    print("Scraping page for base image...")
    try:
        imageLoaded = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Weather-Traffic Camera thumbnail']")))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Need this script to simulate user interaction on the page to let the page inject the image src
        time.sleep(2)
        html = driver.page_source
        print("Success: found base image.")
    except TimeoutException:
        print("Error: TimeoutException while scraping for base image!")

    driver.close()
    print("Parsing out base image src...")
    soup = BeautifulSoup(html, "html.parser")
    imageUrl = soup.find("img", alt="Weather-Traffic Camera thumbnail")["src"]
    print("Succesfully grabbed image url. " + imageUrl)

    print("Writing image to file...")

    try:
        img = Image.open(urlopen(imageUrl))
        img.save("images/" + fileName)
        print("Done. (Success)")
        return "success"
    except:
        print("Error - camera must be down")
        return "error"