# helpers/helper_functions.py
def example_function():
    return "This is a helper function"
# helpers/helper_functions.py

def mail_with_name_only():
    return "testuser@yandex.ru"

def mail_with_error_domain():
    return "testuser@invalid"
import random
import string

def random_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

def random_email():
    return f"{random_name()}@example.com"

def random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))  # Генерация случайного пароля