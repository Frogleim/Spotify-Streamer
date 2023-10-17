import time
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import undetected_chromedriver as uc
from core import postgres_connect
import random


def run_browser():
    driver = uc.Chrome()

    return driver


def start_streaming(email, password):
    url = 'https://accounts.spotify.com/en/login'
    driver = run_browser()
    driver.get(url)
    try:
        email_input = driver.find_element(By.XPATH, '//*[@id="login-username"]')
        email_input.send_keys(email)
        time.sleep(random.uniform(0.5, 1.8))
        password_input = driver.find_element(By.XPATH, '//*[@id="login-password"]')
        password_input.send_keys(password)
        time.sleep(random.uniform(0.5, 1.8))
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        print(f"Log in successful with email: {email}")
        time.sleep(random.uniform(3.2, 5))
        driver.get('')
        time.sleep(random.uniform(1.2, 2))
        keyboard = Controller()
        keyboard.press(Key.enter)
        time.sleep(2)
        driver.find_element(By.XPATH,
                            '/html/body/div[4]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div['
                            '2]/main/section/div[3]/div[4]/div/div/div/div/div/button').click()
        print('Playing....')
        time.sleep(random.uniform(33, 45))
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div['
                                      '2]/main/section/div[3]/div[4]/div/div/div/div/button[1]').click()
        print('Liked!....')
    except Exception as e:
        print(f'Failed to run: Error message is: {e}')
    driver.close()


def run():
    accounts_data = postgres_connect.fetch_accounts_from_postgresql()
    for accounts in accounts_data:
        email, password = accounts
        start_streaming(email, password)
        time.sleep(random.randint(6, 12))


if __name__ == '__main__':
    run()
