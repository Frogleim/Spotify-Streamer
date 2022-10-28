import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
import schedule
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


def run_first_time():
    file = open(r'./users/client_credentials_final.json')
    data = json.load(file)
    song_file = open(r'./playlist.json')
    songs = json.load(song_file)
    for items in data['users'][0:2]:
        for playlist in songs['playlist'][0:1]:
            start_streaming(items['email'], items['password'], playlist['song'])


def radio():
    file = open(r'./users/client_credentials_final.json')
    data = json.load(file)
    song_file = open(r'./playlist.json')
    songs = json.load(song_file)
    other_users = 0
    other_songs = 1
    for items in data['users'][other_users:2 + other_users]:
        for playlist in songs['playlist'][other_songs:other_songs + 1]:
            start_streaming(items['email'], items['password'], playlist['song'])


def run_all():
    run_first_time()
    schedule.every(1).hour.do(radio)


if __name__ == '__main__':
    run_all()
