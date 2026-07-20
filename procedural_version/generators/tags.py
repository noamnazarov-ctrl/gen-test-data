# Импортируем список тегов, из которого нужно выбирать результат.
from procedural_version.data.names_data import TAGS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть список тегов.
def tags(count=None, unique=True, seed=None):
    # Что делает функция: возвращает список строк-тегов.
    # count=None значит выбрать случайное количество тегов от 1 до 3.
    # count=5 значит вернуть ровно 5 тегов.
    # unique=True значит теги не должны повторяться.
    # unique=False значит повторы разрешены.
    # seed - число для random: с одним и тем же seed random выбирает один и тот же список тегов.
    # Можно вызвать tags() и получить от 1 до 3 разных тегов.
    # Можно вызвать tags(count=5) и получить ровно 5 разных тегов.
    # Можно вызвать tags(count=5, unique=False) и разрешить одинаковые теги.
    # Можно вызвать tags(count=5, unique=True, seed=1) и сочетать настройки.
    # Пример вызова: tags(count=5, unique=True, seed=1) должен вернуть 5 разных тегов.
    # Документация: docs/function_specifications.md, раздел tags.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py tags
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если count меньше 0, нужно вызвать ValueError.
    # Что вернуть: список строк.
    # Тесты: test_tags_unique, test_tags_dupes.
    pass
