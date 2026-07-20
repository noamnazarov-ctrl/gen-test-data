# Подсказка ученику: create_random(seed) помогает получить одинаковый True или False при одинаковом seed.
from procedural_version.utils.random_utils import create_random

# Пример готового решения: по нему можно понять, как делать похожие генераторы.
def generate_is_active_example(seed=None):
    # Где почитать про эту функцию: открой docs/function_specifications.md и найди раздел generate_is_active_example.
    # Где посмотреть задание команды: открой docs/team_tasks.md и найди generate_is_active_example.
    # Где посмотреть пример использования: открой docs/usage.md и найди generate_is_active_example.
    # seed помогает получать одинаковый случайный результат.
    # Например, generate_is_active_example(seed=1) и еще раз generate_is_active_example(seed=1) должны вернуть одно и то же значение.
    # Это удобно для тестов: тест знает, какой результат должен получиться.
    # Если seed=None, результат может быть разным при каждом запуске.
    # Входные данные - это значения в скобках функции.
    # Входные данные: seed - число для повторения случайного результата или None.
    # Переменные внутри функции можно называть по-своему.
    # Тесты проверяют результат функции, а не названия переменных.
    # Ниже перечислен пример понятного названия переменной.
    # Внутренние переменные: randomizer - генератор случайности, который создается через create_random(seed).
    # Выходные данные - это значение, которое функция отдает с помощью return.
    # Выходные данные: функция должна вернуть булево значение True или False.
    # Шаг 1. Создай генератор случайности через create_random(seed).
    randomizer = create_random(seed)
    # Шаг 2. Выбери одно значение из списка [True, False].
    # Шаг 3. Верни выбранное значение.
    # Проверка тестом: результат должен иметь тип bool.
    # Дополнительная проверка: при одинаковом seed результат должен повторяться.
    # Как проверить работу: запусти в терминале python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_is_active_example_returns_boolean
    # Если все правильно, в самом конце появится слово OK.
    # Если вместо OK появилась ошибка, проверь, что функция возвращает True или False, а не строку и не число.
    return randomizer.choice([True, False])
