import json
import random
import names
import os
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
        options = uc.ChromeOptions()
        options.arguments.extend(["--no-sandbox", "--disable-setuid-sandbox"])
        driver = uc.Chrome(options, use_subprocess=True)
        driver.get('https://www.spotify.com/us/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F')
        time.sleep(2.5)
        email = driver.find_element(By.ID, "email")
        email.send_keys(credentials['email'])
        time.sleep(0.5)
        try:
            re_email = driver.find_element(By.ID, "confirm")

            re_email.send_keys(credentials['email'])
        except Exception:
            print("Re-email Passed...")
        time.sleep(0.5)
        password = driver.find_element(By.ID, "password")
        password.send_keys(credentials['password'])
        time.sleep(0.7)
        username = driver.find_element(By.XPATH, '//*[@id="displayname"]')
        username.send_keys(credentials['username'])
        time.sleep(0.9)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.8)
        drop_months = driver.find_element(By.XPATH,
                                          '//*[@id="month"]')
        select_months = Select(drop_months)
        select_months.select_by_visible_text("Июнь" or "June")
        time.sleep(1)
        day = driver.find_element(By.XPATH, '//*[@id="day"]')
        day.send_keys("22")
        time.sleep(0.6)
        year = driver.find_element(By.XPATH, '//*[@id="year"]')
        year.send_keys("1995")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.68)
        female = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/form/fieldset/div/div[2]/label/span[1]')
        female.click()
        time.sleep(0.2)
        agreements = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/form/div[5]/div/label/span[1]")
        agreements.click()
        time.sleep(0.36)
        login = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/form/div[6]/div/button/span[1]')
        login.click()
        return credentials

    def run(self):
        for i in range(2):
            credentials = self.creator()
            time.sleep(2)
            with open(f'users/accounts.json', 'w') as savefile:
                # Save the entire account_list to the JSON file
                json.dump(self.account_list, savefile, indent=4)
            print(f'{len(self.account_list)} accounts created')
        print(f'___Accounts created successfully___')


if __name__ == "__main__":
    main = Main()
    main.run()
