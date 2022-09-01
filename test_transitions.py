import locators
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestTransitions:
        # Переходим в лк
    def test_login_personal_akk_main(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, locators.Enter_LK).click() # Переход в ЛК
        assert self.driver.find_element(By.XPATH, locators.email) # Ищем поля которые открываются при нажатии на кнопку личный кабинет
        assert self.driver.find_element(By.XPATH, locators.passs)
        self.driver.quit()
         # Переход с ЛК в лого
    def test_personal_akk_to_constructor(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, locators.Enter_LK).click()
        self.driver.find_element(By.XPATH, locators.logo).click()
        assert self.driver.find_element(By.XPATH, locators.bulka)  # Ищем поля которые открываются при нажатии на лого
        assert self.driver.find_element(By.XPATH, locators.bulka_inside)
        self.driver.quit()
        # Выходим из аккаунта
    def test_personal_akk_exit(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, locators.Enter_lk_right).click()  # Жмем на кнопку Войти в аккаунт
        self.driver.find_element(By.XPATH, locators.email).send_keys(email1)  # вводим емейл
        self.driver.find_element(By.XPATH, locators.passs).send_keys("123456")  # вводим пароль
        self.driver.find_element(By.XPATH, locators.Enter).click()  # Нажимаем кнопку Войти
        self.driver.find_element(By.XPATH, locators.Enter_LK).click()  # Нажатие на кнопку ЛК
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.exit))) #Ждем пока кнопка загрузится
        self.driver.find_element(By.XPATH, locators.exit).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.email))) # Ждем пока строка загрузится
        assert self.driver.find_element(By.XPATH, locators.email)  # Ищем поля которые открываются при выходе с аккаунта
        assert self.driver.find_element(By.XPATH, locators.passs)
        self.driver.quit()


