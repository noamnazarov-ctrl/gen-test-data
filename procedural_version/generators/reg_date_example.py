# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем готовый пример функции даты регистрации.
def reg_date_example(start_year=2020, end_year=2026, boundary=None, seed=None):
    # Что делает функция: возвращает дату строкой в формате YYYY-MM-DD.
    # start_year - первый разрешенный год, например 2020.
    # end_year - последний разрешенный год, например 2026.
    # boundary - это режим для специальных проверок в тестах.
    # boundary="min" значит вернуть первую дату start_year: "2020-01-01".
    # boundary="max" значит вернуть дату в конце end_year: "2026-12-28".
    # boundary="below_min" значит вернуть дату до диапазона: "2019-12-31".
    # boundary="above_max" значит вернуть дату после диапазона: "2027-01-01".
    # boundary=None значит выбрать случайную дату от start_year до end_year.
    # seed - число для random: с одним и тем же seed random выбирает одну и ту же дату.
    # Можно вызвать reg_date_example() и получить случайную дату от 2020 до 2026 года.
    # Можно вызвать reg_date_example(boundary="min") и получить "2020-01-01".
    # Можно вызвать reg_date_example(start_year=2022, end_year=2024) и выбрать дату в этих годах.
    # Можно вызвать reg_date_example(start_year=2022, end_year=2024, boundary="max") и получить "2024-12-28".
    # Пример вызова: reg_date_example(boundary="min") должен вернуть "2020-01-01".
    # Документация: docs/function_specifications.md, раздел reg_date.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py reg_date_example
    # Если в конце написано OK, этот тест прошел.
    # Что вернуть: строку даты в формате год-месяц-день.
    # Проверка тестами: python check.py reg_date_example
    # Проверяем, что начальный год не больше конечного.
    if start_year > end_year:
        # Сообщаем ошибку, если годы написаны наоборот.
        raise ValueError("start_year не должен быть больше end_year")
    # Возвращаем первую дату начального года.
    if boundary == "min":
        # Возвращаем YYYY-01-01.
        return f"{start_year:04d}-01-01"
    # Возвращаем дату в конце конечного года.
    if boundary == "max":
        # Возвращаем YYYY-12-28.
        return f"{end_year:04d}-12-28"
    # Возвращаем дату раньше разрешенного диапазона.
    if boundary == "below_min":
        # Возвращаем 31 декабря предыдущего года.
        return f"{start_year - 1:04d}-12-31"
    # Возвращаем дату позже разрешенного диапазона.
    if boundary == "above_max":
        # Возвращаем 1 января следующего года.
        return f"{end_year + 1:04d}-01-01"
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Выбираем случайный год внутри диапазона.
    year = randomizer.randint(start_year, end_year)
    # Выбираем случайный месяц от 1 до 12.
    month = randomizer.randint(1, 12)
    # Выбираем случайный день от 1 до 28.
    day = randomizer.randint(1, 28)
    # Возвращаем дату строкой в формате YYYY-MM-DD.
    return f"{year:04d}-{month:02d}-{day:02d}"
