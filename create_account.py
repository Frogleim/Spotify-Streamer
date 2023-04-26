import json
import time
import requests
import random
import names
import os
import secrets
import string
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

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
        self.credentails_data = []
        credentails = {}
        credentails['gender'] = self.gender
        credentails['birth_year'] = self.birth_year
        credentails['birth_month'] = self.birth_month
        credentails['birth_day'] = self.birth_day
        credentails['password'] = self.password
        username = string.ascii_letters + string.digits
        username = ''.join(random.choice(username) for i in range(random.randint(7, 11)))
        credentails['username'] = username
        credentails['email'] = names.get_full_name().replace(' ', '').lower() + f'{random.randint(100, 200)}@gmail.com'
        print(f'Email: {credentails["email"]}')
        print(f'Password: {credentails["password"]}')

        return credentails

    def creator(self):
        credentails = self.gen_credentails_method()
        driver = uc.Chrome()
        driver.get('https://www.spotify.com/us/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F')
        time.sleep(2.5)
        email = driver.find_element(By.XPATH, "email")
        email.send_keys(credentails['email'])
        time.sleep(0.5)
        try:
            re_email = driver.find_element(By.ID, "confirm")

            re_email.send_keys(credentails['email'])
        except Exception:
            print("Re-email Passed...")
        time.sleep(0.5)
        password = driver.find_element(By.ID, "password")
        password.send_keys(credentails['password'])
        time.sleep(0.7)
        username = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/div[4]/input")
        username.send_keys(credentails['username'])
        time.sleep(0.8)
        drop_months = driver.find_element(By.XPATH,
                                          "/html/body/div[1]/main/div/div/form/div[5]/div[2]/div[1]/div/div[2]/select")
        select_months = Select(drop_months)
        select_months.select_by_visible_text("Ocak")
        time.sleep(1)
        day = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/div[5]/div[2]/div[2]/div/input")
        day.send_keys("22")
        time.sleep(0.6)
        year = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/div[5]/div[2]/div[3]/div/input")
        year.send_keys("1995")
        time.sleep(0.5)
        female = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/fieldset/div/div[2]/label/span[1]")
        female.click()
        time.sleep(0.2)
        aggrements = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/div[6]/div/label/span[1]")
        aggrements.click()
        time.sleep(0.36)
        login = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/form/div[7]/div/button/span[1]')
        login.click()
        return credentails

    def run(self):
        credentails = None
        count = 0
        for i in range(1):
            credentails = self.creator()
            time.sleep(2)
            count += 1
            with open(f'users/data_1.json', 'w') as savefile:
                json.dump(credentails, savefile)
                # file_data = json.load(savefile)
                # file_data['users'].append(credentails)
                # savefile.seek(0)
                # json.dump(file_data, savefile, indent=7)
            print(f'{count} account')
        print(f'___Accounts created successfully___')
        return credentails


if __name__ == "__main__":
    main = Main()
    main.run()
