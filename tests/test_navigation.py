import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators, MainPageLocators
from data import UrlList, Data

# Настраиваем логгер
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestNavigation:

    def test_go_to_personal_account(self, driver):
        """Тест перехода в личный кабинет"""
        driver.get(UrlList.page_main_url)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/account"))

        current_url = driver.current_url
        logger.info(f"Текущий URL: {current_url}")

        assert "/account" in current_url or "/account/profile" in current_url, f"Неправильный URL: {current_url}"

    def test_go_to_constructor(self, driver):
        """Тест перехода в конструктор из личного кабинета"""
        driver.get(UrlList.page_main_url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(UrlList.page_main_url))
        assert driver.current_url == UrlList.page_main_url

    def test_go_to_main_by_logo(self, driver):
        """Тест перехода на главную страницу через логотип"""
        driver.get(UrlList.page_main_url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGO_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(UrlList.page_main_url))
        assert driver.current_url == UrlList.page_main_url

    # 🆕 **Тест переходов по разделам в конструкторе**
    def test_go_to_buns_section(self, driver):
        """Тест переключения в раздел 'Булки'"""
        driver.get(UrlList.page_main_url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.buns_span)).click()

        active_tab = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.select_tab_constructor))
        assert active_tab.text == "Булки", "Раздел 'Булки' не активен!"

    def test_go_to_sauces_section(self, driver):
        """Тест переключения в раздел 'Соусы'"""
        driver.get(UrlList.page_main_url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.sauces_span)).click()

        active_tab = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.select_tab_constructor))
        assert active_tab.text == "Соусы", "Раздел 'Соусы' не активен!"

    def test_go_to_fillings_section(self, driver):
        """Тест переключения в раздел 'Начинки'"""
        driver.get(UrlList.page_main_url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.filling_span)).click()

        active_tab = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.select_tab_constructor))
        assert active_tab.text == "Начинки", "Раздел 'Начинки' не активен!"
