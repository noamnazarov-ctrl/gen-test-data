# Подсказка ученику: create_random(seed) нужен, чтобы дата повторялась при одинаковом seed.
from procedural_version.utils.random_utils import create_random

# Пример готового решения: по нему можно понять, как делать похожие генераторы.
def generate_registration_date_example(start_year=2020, end_year=2026, boundary=None, seed=None):
    # Где почитать про эту функцию: открой docs/function_specifications.md и найди раздел generate_registration_date_example.
    # Где посмотреть задание команды: открой docs/team_tasks.md и найди generate_registration_date_example.
    # Где посмотреть пример использования: открой docs/usage.md и найди generate_registration_date_example.
    # seed помогает получать одинаковый случайный результат.
    # Например, generate_registration_date_example(seed=1) и еще раз generate_registration_date_example(seed=1) должны вернуть одну и ту же дату.
    # Это удобно для тестов: тест знает, какой результат должен получиться.
    # Если seed=None, результат может быть разным при каждом запуске.
    # Входные данные - это значения в скобках функции.
    # Входные данные: start_year - первый разрешенный год регистрации.
    # Входные данные: end_year - последний разрешенный год регистрации.
    # Входные данные: boundary - режим границы: "min", "max", "below_min", "above_max" или None.
    # Входные данные: seed - число для повторения случайного результата или None.
    # Переменные внутри функции можно называть по-своему.
    # Тесты проверяют результат функции, а не названия переменных.
    # Ниже перечислены примеры понятных названий переменных.
    # Внутренние переменные: randomizer - генератор случайности, который создается через create_random(seed).
    # Внутренние переменные: year - случайный год регистрации.
    # Внутренние переменные: month - случайный месяц регистрации.
    # Внутренние переменные: day - случайный день регистрации.
    # Выходные данные - это значение, которое функция отдает с помощью return.
    # Выходные данные: функция должна вернуть строку с датой в формате YYYY-MM-DD.
    # Шаг 1. Проверь ошибочный случай: start_year не должен быть больше end_year.
    if start_year > end_year:
        # Проверка тестом: при перепутанных годах функция должна выбросить ValueError.
        raise ValueError("start_year не должен быть больше end_year")
    # Шаг 2. Проверь boundary="min": нужно вернуть первую дату начального года.
    if boundary == "min":
        # Проверка тестом: generate_registration_date_example(boundary="min") должен вернуть YYYY-01-01.
        return f"{start_year:04d}-01-01"
    # Шаг 3. Проверь boundary="max": нужно вернуть дату в конце конечного года.
    if boundary == "max":
        # Проверка тестом: generate_registration_date_example(boundary="max") должен вернуть YYYY-12-28.
        return f"{end_year:04d}-12-28"
    # Шаг 4. Проверь boundary="below_min": это дата раньше разрешенного диапазона.
    if boundary == "below_min":
        # Проверка тестом: год должен быть на 1 меньше start_year.
        return f"{start_year - 1:04d}-12-31"
    # Шаг 5. Проверь boundary="above_max": это дата позже разрешенного диапазона.
    if boundary == "above_max":
        # Проверка тестом: год должен быть на 1 больше end_year.
        return f"{end_year + 1:04d}-01-01"
    # Шаг 6. Если boundary не передан, создай генератор случайности.
    randomizer = create_random(seed)
    # Шаг 7. Сгенерируй год от start_year до end_year включительно.
    year = randomizer.randint(start_year, end_year)
    # Шаг 8. Сгенерируй месяц от 1 до 12.
    month = randomizer.randint(1, 12)
    # Шаг 9. Сгенерируй день от 1 до 28, чтобы не думать о разной длине месяцев.
    day = randomizer.randint(1, 28)
    # Шаг 10. Верни строку в формате YYYY-MM-DD.
    # Проверка тестом: строка должна иметь формат даты и год должен быть в разрешенном диапазоне.
    # Как проверить работу: запусти в терминале python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_registration_date_example_returns_boundary_values
    # Если все правильно, в самом конце появится слово OK.
    # Если вместо OK появилась ошибка, проверь даты для boundary="min" и boundary="max".
    return f"{year:04d}-{month:02d}-{day:02d}"
