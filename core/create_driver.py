from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


def create_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    path = ChromeDriverManager().install()
    driver = webdriver.Chrome(path)
    return driver


def create_firefox_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return driver
