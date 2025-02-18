import random  # ✅ Все импорты в начале файла
import string
import logging
from data.data import TEST_EMAIL  # ✅ Корректный импорт

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def example_function():
    return "This is a helper function"

def mail_with_error_domain():
    return "testuser@invalid"

def random_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

def random_email():
    return f"{random_name()}@example.com"

def random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def log_current_url(driver):
    """Логирует текущий URL"""
    current_url = driver.current_url
    logger.info(f"Текущий URL: {current_url}")
    return current_url  # ✅ Возвращаем URL, чтобы использовать в тестах
