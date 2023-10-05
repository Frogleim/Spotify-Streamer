import time
from selenium.webdriver.common.by import By
import json
from core import create_driver


def change_passwords(email, password):
    url = 'https://accounts.spotify.com/en/login'
    driver = create_driver.create_firefox_driver()
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
        # driver.find_element(By.XPATH, '//*[@id="account-settings-link"]/div[1]/p').click()
        # time.sleep(3)
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
                            '/html/body/div[1]/div[1]/div/div[2]/div[2]/article/section/form/div[4]/button/span[1]') \
            .click()
        print(f'Change successfully. New password is {new_passwords} for user {email} ')
        data = {
            'email': email,
            'password': new_passwords

        }
        with open('./users/updated_data.json', 'w') as f:
            # write the data to the file in JSON format
            json.dump(data, f)
        driver.close()
    except Exception as e:
        print(f'Failed to change password! Error message is: {e}')


def run():
    # while True:
    file = open(r'./users/data_1.json')
    data = json.load(file)
    num = 0
    change_passwords(data['email'], data['password'])
    time.sleep(1)
    num += 1
    print(f'{num} account with changes password')



if __name__ == '__main__':
    run()
