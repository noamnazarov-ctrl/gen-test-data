# Импортируем список готовых фраз для комментария.
from procedural_version.data.names_data import COMMENTS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть комментарий точной длины.
def comment(length=100, seed=None):
    # Что делает функция: возвращает строку ровно из length символов.
    # length=0 значит вернуть пустую строку "".
    # length=1 значит вернуть строку из одного символа.
    # length=255 значит вернуть строку длиной ровно 255 символов.
    # seed - число для random: с одним и тем же seed random выбирает одну и ту же фразу.
    # Можно вызвать comment() и получить комментарий длиной 100 символов.
    # Можно вызвать comment(length=0) и получить пустую строку.
    # Можно вызвать comment(length=255, seed=1) и получить комментарий длиной 255 символов.
    # Пример вызова: len(comment(length=255, seed=1)) должен быть 255.
    # Документация: docs/function_specifications.md, раздел comment.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py comment
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если length меньше 0, нужно вызвать ValueError.
    # Что вернуть: строку.
    # Тесты: test_comment_lengths, test_comment_bad_len.
    pass
