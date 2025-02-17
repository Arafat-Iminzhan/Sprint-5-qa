from locators.locators import Locators, AccountPageLocators, MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data import UrlList, Data


class TestNavigation:

    def test_go_to_personal_account(self, driver):
        """Тест перехода в личный кабинет"""
        driver.get(UrlList.page_main_url)

        # ✅ Ожидаем появления кнопки "Личный кабинет"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))

        # ✅ Пробуем несколько раз кликнуть, если первый клик не сработал
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        try:
            personal_account_button.click()
        except TimeoutException:
            driver.execute_script("arguments[0].click();", personal_account_button)

        # ✅ Ожидаем редирект (два возможных варианта URL)
        try:
            WebDriverWait(driver, 10).until(EC.url_contains("/account"))
        except TimeoutException:
            WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))

        # ✅ Логируем текущий URL
        current_url = driver.current_url
        print(f"Текущий URL: {current_url}")

        # ✅ Проверяем, что мы действительно на странице аккаунта
        assert any(substring in current_url for substring in ["/account", "/account/profile"]), \
            f"Неправильный URL: {current_url}"

    def test_go_to_constructor(self, driver):
        """Тест перехода в конструктор из личного кабинета"""
        driver.get(UrlList.page_main_url)

        # ✅ Авторизация перед переходом в аккаунт
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.login_button_main)).click()
        driver.find_element(*Locators.input_email_field).send_keys(Data.email)
        driver.find_element(*Locators.input_password_field).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()

        # ✅ Ждем входа и переходим в аккаунт
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.order_button))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        # ✅ Переход в конструктор
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)).click()

        # ✅ Проверка URL
        WebDriverWait(driver, 10).until(EC.url_to_be(UrlList.page_main_url))
        assert driver.current_url == UrlList.page_main_url

    def test_go_to_main_by_logo(self, driver):
        """Тест перехода на главную страницу через логотип"""
        driver.get(UrlList.page_main_url)

        # ✅ Авторизация перед переходом
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.login_button_main)).click()
        driver.find_element(*Locators.input_email_field).send_keys(Data.email)
        driver.find_element(*Locators.input_password_field).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()

        # ✅ Ждем входа и переходим в аккаунт
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.order_button))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        # ✅ Ожидаем появления логотипа и кликаем
        logo_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGO_BUTTON))
        try:
            logo_button.click()
        except TimeoutException:
            driver.execute_script("arguments[0].click();", logo_button)

        # ✅ Ожидаем загрузки главной страницы
        WebDriverWait(driver, 10).until(EC.url_to_be(UrlList.page_main_url))
        assert driver.current_url == UrlList.page_main_url
