from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
from config import DYNAMIC_SITES

# Setup Selenium WebDriver (Headless mode)
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Function to extract product URLs using Selenium
def extract_product_urls_with_selenium(url):
    """
    Extract product URLs from dynamic content using Selenium for rendering JavaScript.

    Args:
        url (str): The URL of the page to scrape.

    Returns:
        set: A set of product URLs.
    """
    driver = setup_driver()
    driver.get(url)

    # Simulate scrolling to trigger infinite scroll or AJAX loading
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(3, 5))  # Random delay to mimic human behavior

    page_content = driver.page_source
    driver.quit()

    from utils import extract_product_urls_from_page
    return extract_product_urls_from_page(page_content, url)