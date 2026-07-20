# Импортируем sys, чтобы прочитать короткое имя проверки из команды.
import sys
# Импортируем unittest, чтобы запускать уже готовые автотесты.
import unittest

# Сохраняем код зеленого цвета для успешного результата в терминале.
GREEN = "\033[32m"
# Сохраняем код красного цвета для ошибок в терминале.
RED = "\033[31m"
# Сохраняем код желтого цвета для подсказок в терминале.
YELLOW = "\033[33m"
# Сохраняем код сброса цвета до обычного цвета терминала.
RESET = "\033[0m"

# Объявляем функцию, которая красит текст только в обычном терминале.
def color_text(text, color):
    # Проверяем, подключен ли вывод к интерактивному терминалу.
    if not sys.stdout.isatty():
        # Возвращаем простой текст для файла, IDE или автоматической проверки.
        return text
    # Добавляем выбранный цвет перед текстом и сбрасываем цвет после текста.
    return f"{color}{text}{RESET}"

# Создаем словарь: короткая команда ученика -> список настоящих unittest-тестов.
TESTS = {
    # Проверки ID пользователя.
    "user_id": [
        # Тест ID из цифр и точной длины.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_id_digits",
        # Тест ID из букв и цифр.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_id_alnum",
        # Тест ошибки при неправильной длине ID.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_id_bad_length",
        # Тест повторяемости ID при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_id_seed",
    ],
    # Проверки имени.
    "first_name": [
        # Тест минимальной длины имени.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_first_name_min_len",
        # Тест максимальной длины имени.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_first_name_max_len",
        # Тест ошибки, если подходящих имен нет.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_first_name_no_match",
        # Тест повторяемости имени при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_first_name_seed",
    ],
    # Проверки фамилии.
    "last_name": [
        # Тест максимальной длины фамилии.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_last_name_max_len",
        # Тест минимальной длины фамилии.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_last_name_min_len",
        # Тест ошибки, если подходящих фамилий нет.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_last_name_no_match",
        # Тест повторяемости фамилии при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_last_name_seed",
    ],
    # Проверки полного имени.
    "full_name": [
        # Тест ограничения общей длины полного имени.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_full_name_max_len",
        # Тест имени и фамилии в одной строке.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_full_name_basic",
        # Тест повторяемости полного имени при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_full_name_seed",
    ],
    # Проверки возраста.
    "age": [
        # Тест специальных значений возраста.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_age_bounds",
        # Тест обычного возраста внутри диапазона.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_age_range",
        # Тест ошибки при неправильном диапазоне возраста.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_age_bad_range",
        # Тест повторяемости возраста при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_age_seed",
    ],
    # Проверки года рождения.
    "birth_year": [
        # Тест специальных значений года рождения.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_birth_year_bounds",
        # Тест обычного года внутри диапазона.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_birth_year_range",
        # Тест ошибки при неправильном диапазоне годов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_birth_year_bad_range",
        # Тест повторяемости года при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_birth_year_seed",
    ],
    # Проверки города.
    "city": [
        # Тест фильтра города по первой букве.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_city_prefix",
        # Тест города из учебного списка.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_city_list",
        # Тест ошибки, если подходящего города нет.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_city_bad_prefix",
        # Тест повторяемости города при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_city_seed",
    ],
    # Проверки email.
    "email": [
        # Тест правильного и неправильного email.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_email_validity",
        # Тест ошибки при неправильной длине username.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_email_bad_len",
        # Тест повторяемости email при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_email_seed",
    ],
    # Проверки username.
    "username": [
        # Тест точной длины username.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_username_len",
        # Тест ошибки при неправильной длине username.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_username_bad_len",
        # Тест повторяемости username при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_username_seed",
    ],
    # Проверки комментария.
    "comment": [
        # Тест комментария любой нужной длины.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_comment_lengths",
        # Тест ошибки при отрицательной длине.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_comment_bad_len",
        # Тест повторяемости комментария при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_comment_seed",
    ],
    # Проверки пароля.
    "password": [
        # Тест обязательных частей пароля.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_password_parts",
        # Тест ошибки при неправильной длине пароля.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_password_bad_len",
        # Тест повторяемости пароля при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_password_seed",
    ],
    # Проверки телефона.
    "phone": [
        # Тест правильного и неправильного телефона.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_phone_validity",
        # Тест кода оператора.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_phone_code",
        # Тест повторяемости телефона при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_phone_seed",
    ],
    # Проверки тегов.
    "tags": [
        # Тест количества и уникальности тегов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_tags_unique",
        # Тест ошибки при отрицательном количестве тегов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_tags_bad_count",
        # Тест тегов с повторами.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_tags_dupes",
        # Тест повторяемости тегов при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_tags_seed",
    ],
    # Проверки профиля.
    "user_profile": [
        # Тест богатого словаря профиля.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_user_profile_fields",
        # Тест профиля с неправильным email.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_user_profile_invalid_email",
        # Тест повторяемости профиля при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_user_profile_seed",
    ],
    # Проверки функции-образца балла.
    "score_example": [
        # Тест специальных значений балла.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_score_bounds",
        # Тест обычного балла внутри диапазона.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_score_range",
        # Тест повторяемости балла при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_score_seed",
        # Тест ошибки при неправильном диапазоне баллов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_score_bad_range",
    ],
    # Проверки функции-образца активности.
    "active_example": [
        # Тест булевого результата.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_active_bool",
        # Тест повторяемости активности при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_active_seed",
    ],
    # Проверки функции-образца плана подписки.
    "plan_example": [
        # Тест выбора только из разрешенных планов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_plan_allowed",
        # Тест выбора из общего списка планов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_plan_default",
        # Тест повторяемости плана при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_plan_seed",
        # Тест ошибки при пустом списке планов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_plan_empty",
    ],
    # Проверки функции-образца даты регистрации.
    "reg_date_example": [
        # Тест специальных значений даты.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_reg_date_bounds",
        # Тест обычной даты внутри диапазона.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_reg_date_range",
        # Тест повторяемости даты при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_reg_date_seed",
        # Тест ошибки при неправильном диапазоне лет.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_reg_date_bad_range",
    ],
    # Проверки всей ООП-версии.
    "oop": [
        # Запускаем весь файл тестов ООП-версии.
        "oop_version.tests.test_generators",
    ],
    # Проверки всей процедурной версии.
    "all": [
        # Запускаем весь файл тестов процедурной версии.
        "procedural_version.tests.test_generators",
    ],
}

# Создаем список окончаний имен тестов и понятных подсказок для ученика.
HINTS = [
    # Подсказка для тестов, где неправильные границы должны вызывать ошибку.
    ("_bad_range", "Проверь: если минимум больше максимума, функция должна вызвать ValueError."),
    # Подсказка для тестов, где неправильная длина должна вызывать ошибку.
    ("_bad_len", "Проверь: неправильная длина должна вызывать ValueError."),
    # Подсказка для теста с неправильным количеством тегов.
    ("_bad_count", "Проверь: отрицательное количество тегов должно вызывать ValueError."),
    # Подсказка для теста с неизвестной первой буквой города.
    ("_bad_prefix", "Проверь: если городов на такую букву нет, функция должна вызвать ValueError."),
    # Подсказка для тестов, где подходящих имен или фамилий нет.
    ("_no_match", "Проверь: если подходящего варианта нет, функция должна вызвать ValueError."),
    # Подсказка для специальных значений на границах диапазона.
    ("_bounds", "Проверь boundary: min, max, below_min и above_max должны возвращать нужные значения."),
    # Подсказка для обычного результата внутри диапазона.
    ("_range", "Проверь: обычный случайный результат должен быть внутри указанного диапазона."),
    # Подсказка для повторяемой случайности.
    ("_seed", "Проверь seed: два одинаковых вызова с seed=1 должны дать одинаковый результат."),
    # Подсказка для точной длины.
    ("_len", "Проверь: результат должен иметь длину, которую передали в параметре length."),
    # Подсказка для проверки начала строки.
    ("_prefix", "Проверь: город должен начинаться с буквы из параметра starts_with."),
    # Подсказка для проверки списка городов.
    ("_list", "Проверь: функция должна выбирать значение только из учебного списка."),
    # Подсказка для правильного и неправильного формата.
    ("_validity", "Проверь valid=True и valid=False: правильный формат и специально неправильный формат должны отличаться."),
    # Подсказка для обязательных частей пароля.
    ("_parts", "Проверь: пароль должен содержать обязательные цифру и спецсимвол."),
    # Подсказка для кода оператора телефона.
    ("_code", "Проверь: код оператора должен быть числом от 900 до 999."),
    # Подсказка для уникальных тегов.
    ("_unique", "Проверь: при unique=True теги не должны повторяться."),
    # Подсказка для тегов с повторами.
    ("_dupes", "Проверь: при unique=False одинаковые теги разрешены."),
    # Подсказка для разрешенного списка планов.
    ("_allowed", "Проверь: результат должен быть только из списка allowed_plans."),
    # Подсказка для общего списка планов.
    ("_default", "Проверь: без allowed_plans нужно выбирать план из общего списка."),
    # Подсказка для пустого списка планов.
    ("_empty", "Проверь: пустой список allowed_plans должен вызывать ValueError."),
    # Подсказка для булевого результата.
    ("_bool", "Проверь: функция должна вернуть только True или False."),
    # Подсказка для ID из цифр.
    ("_digits", "Проверь: при only_digits=True ID должен состоять только из цифр."),
    # Подсказка для ID из букв и цифр.
    ("_alnum", "Проверь: при only_digits=False ID может содержать английские буквы и цифры."),
    # Подсказка для словаря профиля.
    ("_fields", "Проверь: в словаре профиля должны быть все обязательные ключи."),
    # Подсказка для неправильного email в профиле.
    ("_invalid_email", "Проверь: при valid=False email в профиле должен быть специально неправильным."),
    # Подсказка для простого полного имени.
    ("_basic", "Проверь: полное имя должно содержать имя и фамилию через пробел."),
    # Подсказка для правильного email.
    ("_valid", "Проверь: правильный email должен содержать знак @."),
    # Подсказка для неправильного телефона.
    ("_invalid", "Проверь: при valid=False телефон должен быть специально неправильным."),
]

# Объявляем функцию, которая объясняет причины упавших тестов.
def show_failure_hints(result):
    # Собираем вместе тесты с неправильным ответом и тесты с ошибкой программы.
    failed_tests = result.failures + result.errors
    # Проверяем, есть ли вообще упавшие тесты.
    if not failed_tests:
        # Ничего не печатаем, если все тесты уже прошли.
        return
    # Печатаем желтый заголовок раздела с понятными подсказками.
    print(color_text("\nПодсказки по ошибкам:", YELLOW))
    # Проходим по каждому упавшему тесту.
    for test, details in failed_tests:
        # Берем только короткое имя теста из полного имени unittest.
        test_name = test.id().split(".")[-1]
        # Печатаем желтым имя теста, который нужно исправить.
        print(color_text(f"- {test_name}:", YELLOW))
        # Проверяем, не вернула ли функция None из-за оставшегося pass.
        if "None" in details:
            # Печатаем желтым самую частую причину None в учебном задании.
            print(color_text("  Функция вернула None. Проверь, не остался ли внутри pass вместо return.", YELLOW))
            # Переходим к следующему тесту.
            continue
        # Ищем подсказку по окончанию имени теста.
        for suffix, hint in HINTS:
            # Проверяем, подходит ли окончание к имени теста.
            if test_name.endswith(suffix):
                # Печатаем желтым найденную подсказку.
                print(color_text(f"  {hint}", YELLOW))
                # Останавливаем поиск после первой подходящей подсказки.
                break
        # Выполняем этот блок, если подходящей подсказки не нашли.
        else:
            # Просим желтым прочитать текст ошибки unittest и сравнить результат с заданием.
            print(color_text("  Прочитай текст ошибки выше и сравни результат с инструкцией в функции.", YELLOW))

# Объявляем функцию, которая печатает яркий итог запуска тестов.
def show_summary(result):
    # Считаем тесты с неправильным ответом.
    failed_count = len(result.failures)
    # Считаем тесты, в которых программа завершилась ошибкой.
    error_count = len(result.errors)
    # Считаем пропущенные тесты, если они появятся в будущем.
    skipped_count = len(result.skipped)
    # Считаем тесты, которые прошли успешно.
    passed_count = result.testsRun - failed_count - error_count - skipped_count
    # Проверяем, прошли ли все запущенные тесты.
    if result.wasSuccessful():
        # Выбираем зеленый цвет для успешного запуска.
        color = GREEN
        # Сохраняем понятный заголовок успеха.
        title = "ПРОВЕРКА ПРОЙДЕНА"
    # Выполняем этот блок, если есть падения или ошибки.
    else:
        # Выбираем красный цвет для неуспешного запуска.
        color = RED
        # Сохраняем понятный заголовок ошибки.
        title = "ПРОВЕРКА НЕ ПРОЙДЕНА"
    # Печатаем верхнюю линию цветного блока.
    print(color_text("\n================================", color))
    # Печатаем цветной заголовок результата.
    print(color_text(title, color))
    # Печатаем количество успешно пройденных тестов.
    print(color_text(f"Пройдено: {passed_count} из {result.testsRun}", color))
    # Печатаем количество тестов с неправильным результатом.
    print(color_text(f"Падений: {failed_count}", color))
    # Печатаем количество ошибок программы во время тестов.
    print(color_text(f"Ошибок: {error_count}", color))
    # Печатаем количество пропущенных тестов.
    print(color_text(f"Пропущено: {skipped_count}", color))
    # Печатаем нижнюю линию цветного блока.
    print(color_text("================================", color))

# Объявляем функцию, которая печатает подсказку по коротким командам.
def show_help():
    # Печатаем заголовок подсказки.
    print("Использование: python check.py <имя>")
    # Печатаем пример самой частой команды.
    print("Пример: python check.py city")
    # Печатаем пустую строку для читаемости.
    print()
    # Печатаем список доступных коротких имен.
    print("Доступные имена:")
    # Проходим по всем коротким именам в алфавитном порядке.
    for name in sorted(TESTS):
        # Печатаем одно короткое имя.
        print(f"- {name}")

# Объявляем главную функцию запуска.
def main():
    # Проверяем, передал ли ученик короткое имя проверки.
    if len(sys.argv) != 2:
        # Показываем подсказку, если имя не передали.
        show_help()
        # Возвращаем код ошибки, потому что команда неполная.
        return 1
    # Забираем короткое имя из команды.
    check_name = sys.argv[1]
    # Проверяем, знает ли программа такое короткое имя.
    if check_name not in TESTS:
        # Печатаем понятную ошибку.
        print(f"Не знаю проверку: {check_name}")
        # Показываем список доступных проверок.
        show_help()
        # Возвращаем код ошибки.
        return 1
    # Создаем загрузчик тестов unittest.
    loader = unittest.defaultTestLoader
    # Создаем пустой набор тестов.
    suite = unittest.TestSuite()
    # Проходим по настоящим именам тестов для выбранной короткой команды.
    for test_name in TESTS[check_name]:
        # Загружаем нужный тест по его полному пути внутри проекта.
        suite.addTests(loader.loadTestsFromName(test_name))
    # Создаем запускатель тестов с обычной подробностью вывода.
    runner = unittest.TextTestRunner(verbosity=1)
    # Запускаем выбранные тесты.
    result = runner.run(suite)
    # Печатаем цветной итог со статистикой после запуска тестов.
    show_summary(result)
    # Печатаем понятные подсказки, если хотя бы один тест не прошел.
    if not result.wasSuccessful():
        # Передаем результат unittest в функцию с подсказками.
        show_failure_hints(result)
    # Возвращаем 0, если тесты прошли, и 1, если была ошибка.
    return 0 if result.wasSuccessful() else 1

# Проверяем, что файл запустили напрямую из терминала.
if __name__ == "__main__":
    # Запускаем главную функцию и передаем ее код системе.
    raise SystemExit(main())
