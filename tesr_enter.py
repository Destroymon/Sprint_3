import locators
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestEntrance:
    # успешный вход cуществующим пользователем через кнопку Войти в аккаунт
    def test_successful_login_by_an_existing_user_via_the_Login_to_account_button(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, locators.Enter_lk_right).click()  # Жмем на кнопку Войти в аккаунт
        self.driver.find_element(By.XPATH, locators.email).send_keys(email1)  # вводим емейл
        self.driver.find_element(By.XPATH, locators.passs).send_keys("123456")  # вводим пароль
        self.driver.find_element(By.XPATH, locators.Enter).click()  # Нажимаем кнопку Войти
        self.driver.find_element(By.XPATH, locators.Enter_LK).click()  # Нажатие на кнопку ЛК
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_info))) #Ждем пока страница с информацией прогрузится
        assert self.driver.find_element(By.XPATH, locators.profile_info)
        assert self.driver.find_element(By.XPATH, locators.history_orders)
        assert self.driver.find_element(By.XPATH, locators.exit)
        self.driver.quit()
        #  успешный вход cуществующим пользователем через кнопку Личный кабинет
    def test_successful_login_by_an_existing_user_via_the_Personal_Account_button(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.Enter_LK)))
        self.driver.find_element(By.XPATH, locators.Enter_LK).click()  # Нажатие на кнопку ЛК
        self.driver.find_element(By.XPATH, locators.email).send_keys(email1)  # вводим емейл
        self.driver.find_element(By.XPATH, locators.passs).send_keys("123456")  # вводим пароль
        self.driver.find_element(By.XPATH, locators.Enter).click()  # жмем кнопку Войти
        # проверяем результат авторизации
        self.driver.find_element(By.XPATH, locators.Enter_LK).click()  # кликаем на кнопку Личный кабинет
        self.driver.find_element(By.XPATH, locators.Enter_LK).click()
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_info)))
        assert self.driver.find_element(By.XPATH, locators.profile_info)
        assert self.driver.find_element(By.XPATH, locators.history_orders)
        assert self.driver.find_element(By.XPATH, locators.exit)
        self.driver.quit()
    #  успешный вход cуществующим пользователем на странице регистрации
    def test_successful_login_by_an_existing_user_on_the_registration_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, locators.Enter_lk_right).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.regestration)))
        self.driver.find_element(By.XPATH, locators.regestration).click()
        self.driver.find_element(By.XPATH, locators.enter_reg).click()
        self.driver.find_element(By.XPATH, locators.email).send_keys(email1)  # вводим емейл
        self.driver.find_element(By.XPATH, locators.passs).send_keys("123456")  # вводим пароль
        self.driver.find_element(By.XPATH, locators.Enter).click()
        # проверяем результат авторизации
        self.driver.find_element(By.XPATH, locators.Enter_LK).click()  # кликаем на кнопку Личный кабинет
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_info)))
        assert self.driver.find_element(By.XPATH, locators.profile_info)
        assert self.driver.find_element(By.XPATH, locators.history_orders)
        assert self.driver.find_element(By.XPATH, locators.exit)
        self.driver.quit()
    #  успешный вход cуществующим пользователем на странице восстановления пароля
    def test_successful_login_by_an_existing_user_on_the_password_recovery_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.Enter_LK)))  # ждем пока страничка не загрузится
        self.driver.find_element(By.XPATH, locators.Enter_LK).click()  # жмем Личный кабинет в хэдере
        self.driver.find_element(By.XPATH, locators.restore_pass).click()  # жмем Восстановить пароль
        self.driver.find_element(By.XPATH, locators.enter_reg).click()  # жмем Вход на странице восстановления пароля
        self.driver.find_element(By.XPATH, locators.email).send_keys(email1)  # вводим логин
        self.driver.find_element(By.XPATH, locators.passs).send_keys("123456")  # и пароль
        self.driver.find_element(By.XPATH, locators.Enter).click()  # жмем Войти
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.Enter_LK)))  # ждем пока страничка не загрузится
        # проверяем результат
        self.driver.find_element(By.XPATH, locators.Enter_LK).click()  # кликаем на кнопку Личный кабинет
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_info)))  # ждем пока загрузится линый кабинет
        assert self.driver.find_element(By.XPATH, locators.profile_info)
        assert self.driver.find_element(By.XPATH, locators.history_orders)
        assert self.driver.find_element(By.XPATH, locators.exit)
        self.driver.quit()