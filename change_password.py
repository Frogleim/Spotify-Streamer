import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json


class ChangePassword:
    def __init__(self):
        self.op = webdriver.ChromeOptions()
        self.op.add_argument('headless')
        self.op.add_experimental_option('detach', True)
        self.path = ChromeDriverManager().install()
        self.driver = webdriver.Chrome(self.path, chrome_options=self.op)

    def change_password_function(self, email, password):
        url = 'https://accounts.spotify.com/en/login'
        self.driver.get(url)

        email_input = self.driver.find_element(By.XPATH, '//*[@id="login-username"]')
        email_input.send_keys(email)
        time.sleep(1)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="login-password"]')
        password_input.send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(5)
        print('Login successfully')
        self.driver.find_element(By.XPATH, '//*[@id="account-settings-link"]/div[1]/p').click()
        time.sleep(3)
        change_password_url = 'https://www.spotify.com/am/account/change-password/'
        self.driver.get(change_password_url)
        time.sleep(3)
        current_password = self.driver.find_element(By.XPATH, '//*[@id="old_password"]')
        current_password.send_keys(password)
        time.sleep(1)
        new_passwords = '077108803Gb'
        new_password = self.driver.find_element(By.XPATH, '//*[@id="new_password"]')
        new_password.send_keys(new_passwords)
        time.sleep(1)
        repeat_new_password = self.driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
        repeat_new_password.send_keys(new_passwords)
        time.sleep(1)
        self.driver.find_element(By.XPATH,
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
        self.driver.close()

    def run(self):
        file = open(r'./users/data_1.json')
        data = json.load(file)
        num = 0
        for items in data['users']:
            self.change_password_function(items['email'], items['password'])
            time.sleep(1)
            num += 1
            print(f'{num} account with changes password')


if __name__ == '__main__':
    change = ChangePassword()
    change.run()
