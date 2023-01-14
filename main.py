from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import random
import string
from datetime import datetime
from faker import Faker


class FirefoxDriver:
    def __init__(self) -> None:
        self.options = FirefoxOptions()
        self.driver = webdriver.Firefox(options=self.options)

        self.driver.get('https://signup.live.com/signup')

    def data_generator(self):
        fake = Faker(['pt_BR'])

        first_name = fake.unique.first_name()
        last_name = fake.unique.last_name()
        email = f'{first_name}{last_name}{random.randint(1000, 99999)}@hotmail.com'.replace(' ', '')

        values = string.ascii_lowercase + string.ascii_uppercase + string.digits
        password = ''
        for i in range(random.randint(10, 16)):
            password += random.choice(values)

        current_date = datetime.today()
        current_year = datetime.strftime(current_date, '%Y')

        birth_date = [random.randint(1, 31), random.randint(1, 12), random.randint(int(current_year) - 40, int(current_year) - 18)]

        return {
            'first name': first_name,
            'last name': last_name,
            'E-mail': email,
            'password': password,
            'birth date': birth_date
        }

        

if __name__ == '__main__':
    driver = FirefoxDriver()

    user_data = driver.data_generator()

    driver.driver.implicitly_wait(0.5)
    driver.driver.find_element(By.ID, 'MemberName').send_keys(user_data['E-mail'])
    driver.driver.find_element(By.ID, 'iSignupAction').click()

    driver.driver.implicitly_wait(4)
    driver.driver.find_element(By.ID, 'PasswordInput').send_keys(user_data['password'])
    driver.driver.find_element(By.ID, 'iSignupAction').click()

    driver.driver.implicitly_wait(4)
    driver.driver.find_element(By.ID, 'FirstName').send_keys(user_data['first name'])
    driver.driver.find_element(By.ID, 'LastName').send_keys(user_data['last name'])
    driver.driver.find_element(By.ID, 'iSignupAction').click()

    driver.driver.implicitly_wait(8)
    driver.driver.find_element(By.ID, 'BirthYear').send_keys(f'{user_data["birth date"][2]}')
    driver.driver.find_element(By.ID, 'BirthDay').click()
    driver.driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[2]/select/option[{user_data["birth date"][0] + 1}]').click()
    driver.driver.find_element(By.ID, 'BirthMonth').click()
    driver.driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[1]/select/option[{user_data["birth date"][1] + 1}]').click()
    driver.driver.find_element(By.ID, 'iSignupAction').click()

    driver.driver.implicitly_wait(15)
    driver.driver.find_element(By.XPATH, '/html/body/div[5]/span/a[2]/span').click()

    