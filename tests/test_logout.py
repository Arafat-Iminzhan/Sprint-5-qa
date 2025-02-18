from locators.locators import Locators, AccountPageLocators, MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import UrlList, Data


class TestLogout:
    def test_logout_from_personal_account(self, driver):
        """Тест выхода из аккаунта"""
        driver.get(UrlList.page_main_url)

        # ✅ Авторизация перед выходом
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.login_button_main)).click()
        driver.find_element(*Locators.input_email_field).send_keys(Data.email)
        driver.find_element(*Locators.input_password_field).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()

        # ✅ Ждём загрузки страницы после входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.order_button))

        # ✅ Переход в личный кабинет
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        # ✅ Ожидаем появления кнопки "Выход" и кликаем
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()

        # ✅ Ожидаем, что кнопка выхода **исчезнет**
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON))

        # ✅ Проверяем, что пользователь разлогинился (перенаправлен на главную или login)
        WebDriverWait(driver, 10).until(
            EC.any_of(
                EC.url_to_be(UrlList.page_main_url),
                EC.url_contains("/login")  # Иногда редиректит на login
            )
        )
        assert "/login" in driver.current_url or driver.current_url == UrlList.page_main_url


class TestNavigation:
    def test_go_to_personal_account(self, driver):
        """Тест перехода в личный кабинет"""
        driver.get(UrlList.page_main_url)

        # ✅ Авторизация перед переходом в аккаунт (чтобы избежать 403 ошибки)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.login_button_main)).click()
        driver.find_element(*Locators.input_email_field).send_keys(Data.email)
        driver.find_element(*Locators.input_password_field).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()

        # ✅ Ожидаем появления кнопки "Личный кабинет" и кликаем
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        # ✅ Ожидаем загрузки страницы аккаунта
        WebDriverWait(driver, 10).until(EC.url_contains("/account"))

        # ✅ Дополнительная проверка, что на странице аккаунта есть профиль
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.profile_link))

        # ✅ Проверка URL
        assert "/account" in driver.current_url, f"Ожидался переход в аккаунт, но текущий URL: {driver.current_url}"
