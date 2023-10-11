import json
import random
import names
import os
import string
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from core import postgres_connect
import signUp_Alternative

script_version = "1.0"
script_title = "Spotify Account Creator and Streamer By Frogleim"
script_info = f'''
	 ..: {script_title} :..

 [!] ABOUT SCRIPT:
 [-] With this script, you can register on Spotify.com
 [-] Version: {script_version}
 --------
 [!] ABOUT CODER:
 [-] ALIILAPRO, Programmer and developer from Armenia.
 [-] Github   : https://github.com/Frogleim
 --------
'''


class Main:

    def clear(self, text):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(text)

    def settitle(self, title_name: str):
        os.system("title {0}".format(title_name))

    def __init__(self):
        self.credentails_data = None
        self.alphabet = string.ascii_letters + string.digits
        self.settitle(script_title)
        self.clear(script_info)
        self.password = '077108803GBH'
        self.birth_year = random.randint(1990, 2002)
        self.birth_month = random.randint(1, 12)
        self.birth_day = random.randint(1, 28)
        self.gender = random.choice(['male', 'female'])
        self.account_list = []

    def gen_credentails_method(self):
        credentials = {'gender': self.gender, 'birth_year': self.birth_year, 'birth_month': self.birth_month,
                       'birth_day': self.birth_day, 'password': self.password}
        username = string.ascii_letters + string.digits
        username = ''.join(random.choice(username) for i in range(random.randint(7, 11)))
        credentials['username'] = username
        credentials['email'] = names.get_full_name().replace(' ', '').lower() + f'{random.randint(100, 200)}@gmail.com'

        # Append the generated credentials to the account_list
        self.account_list.append(credentials)

        print(f'Email: {credentials["email"]}')
        print(f'Password: {credentials["password"]}')

        return credentials

    def creator(self):
        credentials = self.gen_credentails_method()

        driver = uc.Chrome()

        driver.get('https://www.spotify.com/us/signup?flow_id=c9d573b3-b1da-4c29-88c4-e0f8e9c25d63%3A1696803002&forward_url=https%3A%2F%2Faccounts.spotify.com%2Fen%2Fstatus%3Fflow_ctx%3Dc9d573b3-b1da-4c29-88c4-e0f8e9c25d63%3A1696803002')
        try:
            time.sleep(random.uniform(2.2, 2.8))
            email = driver.find_element(By.ID, "email")
            email.send_keys(credentials['email'])
            time.sleep(random.uniform(0.5, 1))
            re_email = driver.find_element(By.ID, "confirm")

            re_email.send_keys(credentials['email'])
       
            time.sleep(random.uniform(0.8, 1.1))
            password = driver.find_element(By.ID, "password")
            password.send_keys(credentials['password'])
            time.sleep(random.uniform(0.7, 1.036))
            username = driver.find_element(By.XPATH, '//*[@id="displayname"]')
            username.send_keys(credentials['username'])
            time.sleep(random.uniform(0.9, 1.569))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(0.8, 1.3))
            drop_months = driver.find_element(By.XPATH,
                                            '//*[@id="month"]')
            select_months = Select(drop_months)
            select_months.select_by_visible_text("Июнь" or "June")
            time.sleep(random.uniform(1, 1.4))
            day = driver.find_element(By.XPATH, '//*[@id="day"]')
            day.send_keys("22")
            time.sleep(random.uniform(0.6, 1.2))
            year = driver.find_element(By.XPATH, '//*[@id="year"]')
            year.send_keys("1995")
            time.sleep(random.uniform(0.56, 0.96))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(1, 1.5))
            female = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/form/fieldset/div/div[2]/label/span[1]')
            female.click()
            time.sleep(random.uniform(0.6, 1.2))
            agreements = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/div[5]/div/label/span[1]")
            agreements.click()
            time.sleep(random.uniform(0.36, 0.88))
            login = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/form/div[6]/div/button/span[1]')
            login.click()
            time.sleep(random.uniform(8, 9.3))
            driver.close()
        except Exception:
            print("Re-email Passed...")
            new_signUp = signUp_Alternative.SignUP(driver=driver)
            new_signUp.create(
                user_email=credentials['email'],
                user_password=credentials['password'],
                username=credentials['username']
            )

    def run(self):
        while True:
            start_time = time.time()
            for _ in range(2):
                self.creator()
                time.sleep(2)
                save_data = postgres_connect.create_table_and_insert_data(self.account_list)
                print(save_data)
                time.sleep(random.uniform(2.2, 2.8))
            print(f'___Accounts created successfully___')
            end_time = time.time()
            exc_time = end_time - start_time
            print(f'Accounts create within {exc_time}')
            postgres_connect.remove_duplicates()
            time.sleep(600)

if __name__ == "__main__":
    create_accounts = Main()
    create_accounts.run()