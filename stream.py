import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
import json


def run_browser():
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
    email_input = driver.find_element(By.XPATH, '//*[@id="login-username"]')
    email_input.send_keys(email)

    password_input = driver.find_element(By.XPATH, '//*[@id="login-password"]')
    password_input.send_keys(password)

    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(5)
    driver.get(playlist)

    time.sleep(2)
    keyboard = Controller()
    keyboard.press(Key.enter)
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '//*[@id="main"]/'
                        'div/div[2]/div[3]/div[1]/div[2]/div[2]/'
                        'div/div/div[2]/main/div/section/div[2]/div[2]/div[4]/div/div/div/div/div/button').click()

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/'
                                  'div/section/div[2]/div[2]/div[4]/div/div/div/div/button[1]').click()


if __name__ == '__main__':
    start_time = time.time()
    file = open(r'./client_credentials_final.json')
    data = json.load(file)
    file = open(r'./playlist.json.json')
    songs = json.load(file)
    for items in data['users']:
        for playlist in songs['playlist']:
            start_streaming(items['email'], items['password'], playlist)
