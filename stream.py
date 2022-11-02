import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.proxy import Proxy, ProxyType


def run_browser():
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    op = webdriver.ChromeOptions()
    # op.add_argument('headless')
    op.add_argument("--disable-infobars")
    op.add_experimental_option('detach', True)
    path = ChromeDriverManager().install()
    driver = webdriver.Chrome(path, chrome_options=op)

    return driver


def start_streaming(email, password, playlist):
    url = 'https://accounts.spotify.com/en/login'
    driver = run_browser()
    driver.get(url)
    try:
        email_input = driver.find_element(By.XPATH, '//*[@id="login-username"]')
        email_input.send_keys(email)
        password_input = driver.find_element(By.XPATH, '//*[@id="login-password"]')
        password_input.send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        print(f"Log in successful with email: {email}")
        time.sleep(5)
        driver.get(playlist)
        time.sleep(2)
        keyboard = Controller()
        keyboard.press(Key.enter)
        time.sleep(2)
        # Play song
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]'
                                      '/main/section/div[3]/div[4]/div/div/div/div/div/button').click()
        print('Playing....')
        time.sleep(2)
        # Like song
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]'
                                      '/main/section/div[3]/div[4]/div/div/div/div/button[1]').click()
        print('Liked!....')
    except Exception as e:
        print(f'Failed to run: Error message is: {e}')




