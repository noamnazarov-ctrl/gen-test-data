# Импортируем список фамилий, из которого нужно выбирать результат.
from procedural_version.data.names_data import LAST_NAMES
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть фамилию.
def last_name(min_length=None, max_length=None, seed=None):
    # Что делает функция: выбирает одну фамилию из LAST_NAMES.
    # min_length=None значит нет ограничения снизу.
    # min_length=8 значит фамилия должна быть длиной 8 символов или больше.
    # max_length=None значит нет ограничения сверху.
    # max_length=7 значит фамилия должна быть длиной 7 символов или меньше.
    # seed - число для random: с одним и тем же seed random выбирает одну и ту же фамилию.
    # Можно вызвать last_name() и получить любую фамилию из списка.
    # Можно вызвать last_name(min_length=8) и получить фамилию длиной 8 символов или больше.
    # Можно вызвать last_name(max_length=7) и получить фамилию длиной 7 символов или меньше.
    # Можно вызвать last_name(min_length=5, max_length=8, seed=1) и сочетать ограничения.
    # Пример вызова: last_name(max_length=7, seed=1) должен вернуть фамилию длиной 7 или меньше.
    # Документация: docs/function_specifications.md, раздел last_name.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py last_name
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если подходящих фамилий нет, нужно вызвать ValueError.
    # Что вернуть: строку с фамилией.
    # Тесты: test_last_name_max_len, test_last_name_min_len.
    pass
