import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.proxy import Proxy, ProxyType
import undetected_chromedriver as uc
import json


def run_browser():
    driver = uc.Chrome()

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
        driver.find_element(By.XPATH,
                            '//*[@id="main"]/'
                            'div/div[2]/div[3]/div[1]/div[2]/div[2]/'
                            'div/div/div[2]/main/div/section/div[2]/div[2]/div[4]/div/div/div/div/div/button').click()
        print('Playing....')
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/'
                                      'div/section/div[2]/div[2]/div[4]/div/div/div/div/button[1]').click()
        print('Liked!....')
    except Exception as e:
        print(f'Failed to run: Error message is: {e}')


def run():
    with open("./users/data_1.json", 'r') as user_file:
        data = json.load(user_file)
        email = data["email"]
        password = data["password"]
    with open("./playlist.json", "r") as playlist_file:
        playlist_data = json.load(playlist_file)
        playlist_url = "https://open.spotify.com/playlist/4lvalcAu0XGMyzPra6xwxb?si=4039bbf69f2a4e2c"
    start_streaming(email, password, playlist_url)


if __name__ == '__main__':
    run()
