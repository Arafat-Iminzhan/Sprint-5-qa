from selenium.webdriver.common.by import By

class Locators:
    # Кнопки входа и выхода
    login_button_main = (By.XPATH, "//button[contains(text(),'Войти')]")  # "Войти в аккаунт"
    login_button_login_page = (By.XPATH, "//button[contains(text(),'Войти')]")  # Кнопка "Войти" на странице логина
    login_link_from_recovery_pass = (By.XPATH, "//a[contains(text(),'Войти')]")  # Ссылка "Войти" со страницы восстановления пароля

    # Поля ввода
    input_name_field = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    input_email_field = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    input_password_field = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

    # Заголовки страниц
    header_h2 = (By.XPATH, "//h2")  # Заголовок страницы (например, "Вход" или "Регистрация")
    login_header_tag_h2 = (By.XPATH, "//h2[contains(text(),'Вход')]")  # Заголовок "Вход"
    make_burger_tag_h1 = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")  # "Соберите бургер"

    # Ссылки и кнопки
    personal_account_button = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    registration_button = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    recovery_pass_link = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    recovery_pass_button = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    profile_link = (By.XPATH, "//a[contains(text(),'Профиль')]")

    # Ошибки и уведомления
    incorrect_password_message = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    user_exists_message = (By.XPATH, "//div/main/div/p[contains(text(),'Такой пользователь уже существует')]")

    # Навигация
    constructor_button = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    order_button = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # Конструктор бургера
    sauces_span = (By.XPATH, "//span[contains(text(),'Соусы')]")
    filling_span = (By.XPATH, "//span[contains(text(),'Начинки')]")
    buns_span = (By.XPATH, "//span[contains(text(),'Булки')]")
    select_tab_constructor = (By.XPATH, "//div[contains(@class, 'current')]/span")

class AccountPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")

class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'logo')]")
