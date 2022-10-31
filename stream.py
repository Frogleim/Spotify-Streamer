import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.proxy import Proxy, ProxyType
import firebase_admin
from firebase_admin import credentials, firestore
import json


cred = credentials.Certificate("./spotify-streamer-18cc3-firebase-adminsdk-us15t-2e400350e5.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection = db.collection('places')


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
    docs = collection.get()
    count = 0
    for _ in range(len(docs)):
        count += 1
        doc = collection.document(f'user_{str(count)}')
        res = doc.get().to_dict()
        song_file = open(r'./playlist.json')
        songs = json.load(song_file)
        for playlist in songs['playlist'][0:1]:
            start_streaming(res['email'], res['password'], playlist['song'])
        if count == 49:
            print('Passing 3....')
            time.sleep(10)


def radio():
    start_time = time.time()
    print(f'Starting time is: {start_time}')
    run()
    docs = collection.get()
    count = 0
    while True:
        print('Waiting for radio turning on...')
        time.sleep(25)
        if (start_time - time.time()) >= 10:
            other_songs = 0
            count += 50
            for _ in range(len(docs)):
                count += 1
                doc = collection.document(f'user_{str(count)}')
                res_1 = doc.get().to_dict()
                song_file = open(r'./playlist.json')
                songs = json.load(song_file)
                for playlists in songs['playlist'][other_songs + 1:other_songs + 2]:
                    start_streaming(res_1['email'], res_1['password'], playlists['song'])
        if (start_time - time.time()) >= 90:
            time.sleep(2 * 3600)


if __name__ == '__main__':
    radio()
