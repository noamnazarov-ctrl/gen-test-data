# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть ID пользователя.
def user_id(length=6, only_digits=True, seed=None):
    # Что делает функция: возвращает строку-ID ровно из length символов.
    # length=8 значит ID должен быть длиной ровно 8 символов.
    # only_digits=True значит ID состоит только из цифр, например "123456".
    # only_digits=False значит можно использовать цифры и английские буквы.
    # seed - число для random: с одним и тем же seed random собирает один и тот же ID.
    # Можно вызвать user_id() и получить ID из 6 цифр.
    # Можно вызвать user_id(length=8) и получить ID из 8 цифр.
    # Можно вызвать user_id(only_digits=False) и разрешить английские буквы и цифры.
    # Можно вызвать user_id(length=8, only_digits=False, seed=1) и сочетать настройки.
    # Пример вызова: user_id(length=8, only_digits=True, seed=1).
    # Документация: docs/function_specifications.md, раздел user_id.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py user_id
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если length меньше или равен 0, нужно вызвать ValueError.
    # Что вернуть: строку.
    # Тесты: test_id_digits, test_id_alnum.
    pass
