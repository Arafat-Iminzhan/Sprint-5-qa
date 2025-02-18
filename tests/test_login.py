from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from data import UrlList, Data
from helpers.helper_functions import random_name, random_email, random_password


class TestLogin:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page(self, driver):
        driver.get(UrlList.page_main_url)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.login_button_main)).click()
        wait.until(EC.presence_of_element_located(Locators.input_email_field)).send_keys(Data.email)
        wait.until(EC.presence_of_element_located(Locators.input_password_field)).send_keys(Data.password)
        wait.until(EC.element_to_be_clickable(Locators.login_button_login_page)).click()

        assert wait.until(EC.visibility_of_element_located(Locators.order_button))

    # Вход через кнопку «Личный кабинет»
    def test_login_from_account(self, driver):
        driver.get(UrlList.page_main_url)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.personal_account_button)).click()
        wait.until(EC.presence_of_element_located(Locators.input_email_field)).send_keys(Data.email)
        wait.until(EC.presence_of_element_located(Locators.input_password_field)).send_keys(Data.password)
        wait.until(EC.element_to_be_clickable(Locators.login_button_login_page)).click()

        assert wait.until(EC.visibility_of_element_located(Locators.order_button))

    # Вход через кнопку в форме регистрации
    def test_login_after_registration(self, driver):
        driver.get(UrlList.page_registration_url)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(Locators.input_name_field)).send_keys(random_name())
        wait.until(EC.presence_of_element_located(Locators.input_email_field)).send_keys(random_email())
        wait.until(EC.presence_of_element_located(Locators.input_password_field)).send_keys(random_password())
        wait.until(EC.element_to_be_clickable(Locators.registration_button)).click()

        wait.until(EC.element_to_be_clickable(Locators.login_button_login_page)).click()
        wait.until(EC.presence_of_element_located(Locators.input_email_field)).send_keys(Data.email)
        wait.until(EC.presence_of_element_located(Locators.input_password_field)).send_keys(Data.password)
        wait.until(EC.element_to_be_clickable(Locators.login_button_login_page)).click()

        assert wait.until(EC.visibility_of_element_located(Locators.order_button))

    # Вход через кнопку в форме восстановления пароля
    def test_login_from_recovery_pass(self, driver):
        driver.get(UrlList.page_login_url)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.recovery_pass_link)).click()
        wait.until(EC.visibility_of_element_located(Locators.recovery_pass_button))
        wait.until(EC.element_to_be_clickable(Locators.login_link_from_recovery_pass)).click()

        wait.until(EC.presence_of_element_located(Locators.input_email_field)).send_keys(Data.email)
        wait.until(EC.presence_of_element_located(Locators.input_password_field)).send_keys(Data.password)
        wait.until(EC.element_to_be_clickable(Locators.login_button_login_page)).click()

        assert wait.until(EC.visibility_of_element_located(Locators.order_button))
