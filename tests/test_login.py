import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators, AccountPageLocators, MainPageLocators
from data import UrlList, Data
from helpers.helper_functions import random_name, random_email, random_password


class TestLogin:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page(self, driver):
        driver.get(UrlList.page_main_url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.login_button_main)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_email_field)
        ).send_keys(Data.email)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_password_field)
        ).send_keys(Data.password)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.login_button_login_page)
        ).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.order_button)
        )

    # Вход через кнопку «Личный кабинет»
    def test_login_from_account(self, driver):
        driver.get(UrlList.page_main_url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.personal_account_button)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_email_field)
        ).send_keys(Data.email)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_password_field)
        ).send_keys(Data.password)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.login_button_login_page)
        ).click()

        assert WebDriverWait(driver, 6).until(
            EC.visibility_of_element_located(Locators.order_button)
        )

    # Вход через кнопку в форме регистрации
    def test_login_after_registration(self, driver):
        driver.get(UrlList.page_registration_url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_name_field)
        ).send_keys(random_name())

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_email_field)
        ).send_keys(random_email())

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_password_field)
        ).send_keys(random_password())

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.registration_button)
        ).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.login_button_login_page)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_email_field)
        ).send_keys(Data.email)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_password_field)
        ).send_keys(Data.password)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.login_button_login_page)
        ).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.order_button)
        )

    # Вход через кнопку в форме восстановления пароля
    def test_login_from_recovery_pass(self, driver):
        driver.get(UrlList.page_login_url)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.recovery_pass_link)
        ).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.recovery_pass_button)
        )

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.login_link_from_recovery_pass)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_email_field)
        ).send_keys(Data.email)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.input_password_field)
        ).send_keys(Data.password)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.login_button_login_page)
        ).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.order_button)
        )
