from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random


class SignUP:
    def __init__(self, driver):
        self.driver = driver

    def create(self, user_email, user_password, username):
        """

        :param user_email: str
        :param user_password: str
        :param username: str
        :return:
        """
        email = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/main/section/div/div/form/div/div/div"
                                                   "/div/div[2]/input")
        email.send_keys(user_email)
        time.sleep(random.uniform(0.8, 1.1))
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/main/section/div/div/form/button").click()
        time.sleep(random.uniform(1.8, 2.4))
        password = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/main/section/div/div/section/form"
                                                      "/div[1]/section/div[2]/div/div[2]/div[1]/input")
        password.send_keys(user_password)
        time.sleep(random.uniform(1.3, 1.5))
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/main/div/main/section/div/div/section/form/div[2]/button").click()
        time.sleep(random.uniform(1, 1.4))
        username_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/main/section/div/div/section"
                                                            "/form/div[1]/section/div[3]/div[1]/div[2]/input")
        username_field.send_keys(username)
        time.sleep(random.uniform(0.76, 0.99))
        drop_month = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/main/section/div/div/section/form"
                                                        "/div[1]/section/div[3]/div[2]/div[2]/div/div/select")
        select_month = Select(drop_month)
        select_month.select_by_visible_text("June")
        day = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/main/section/div/div/section/form/div["
                                                 "1]/section/div[3]/div[2]/div[2]/div[1]/input[1]")
        day.send_keys(random.randint(20, 30))
        time.sleep(random.uniform(0.8, 1.2))
        year = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/main/section/div/div/section/form/div["
                                                  "1]/section/div[3]/div[2]/div[2]/div[1]/input[2]")
        year.send_keys(random.randint(1990, 2002))
        time.sleep(random.uniform(1, 1.5))
        gender = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/main/section/div/div/section/form'
                                                    '/div[1]/section/div[3]/fieldset/div/div/div[1]/label/span[1]')
        gender.click()
        time.sleep(random.uniform(0.4, 0.7))
        next_button_2 = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/main/section/div/div/section"
                                                           "/form/div[2]/button/span[1]")
        next_button_2.click()
        time.sleep(random.uniform(0.8, 1.256))
        sign_up_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/main/section/div/div/section"
                                                            "/form/div[2]/button/span[1]")
        sign_up_button.click()
        time.sleep(random.uniform(2.8, 3.5))
        self.driver.close()
