# Инструкции для команд

В проекте 7 учеников: первая команда - 3 человека, вторая команда - 4 человека. Базовое распределение - по 2 функции на одного ученика. Команда 1 получает 6 основных функций и 4 функции-образца для изучения. Команда 2 получает 8 функций. Каждый генератор - это маленькая учебная задача про тестовые данные, а не просто случайный выбор.

## Общий порядок работы

1. Реализуйте функции своей команды в процедурной версии.
2. Запустите тесты процедурной версии.
3. Исправьте ошибки, если тесты упали.
4. Реализуйте такие же возможности в ООП-версии.
5. Запустите тесты ООП-версии.
6. Исправьте ошибки, если тесты упали.
7. Проверьте вручную, что обе версии работают по одинаковым правилам.

Команды запускаются из корня проекта:

```bash
python check.py all
python check.py oop
```

Тесты ООП-версии проверяют методы ООП напрямую. Они не зависят от процедурных функций, потому что в процедурной версии часть функций пока является заданием и внутри них стоит `pass`.

`seed` - это число для `random`. С одинаковым `seed` случайный выбор повторяется. Это нужно для тестов: они заранее знают, какой результат ждать.

## Команда 1. Числа и данные человека

Реализовать:

- `user_id(length=6, only_digits=True, seed=None)`
- `first_name(min_length=None, max_length=None, seed=None)`
- `last_name(min_length=None, max_length=None, seed=None)`
- `full_name(max_total_length=None, seed=None)`
- `age(min_age=18, max_age=80, boundary=None, seed=None)`
- `birth_year(min_year=1950, max_year=2008, boundary=None, seed=None)`

Функции-образцы, которые уже написаны полностью:

- `score_example(min_score=1, max_score=100, boundary=None, seed=None)` -> `procedural_version/generators/score_example.py`
- `active_example(seed=None)` -> `procedural_version/generators/active_example.py`
- `plan_example(allowed_plans=None, seed=None)` -> `procedural_version/generators/plan_example.py`
- `reg_date_example(start_year=2020, end_year=2026, boundary=None, seed=None)` -> `procedural_version/generators/reg_date_example.py`

Эти файлы уже работают, поэтому их можно открыть и изучить как примеры решения.

Команда учится задавать длину строки, проверять минимальную и максимальную длину, работать с диапазонами чисел, возвращать значения на минимуме, максимуме и за пределами диапазона, ограничивать выбор разрешенными значениями и генерировать даты.

Примеры требований:

- `user_id(length=8)` возвращает строку ровно из 8 символов.
- `age(boundary="min")` возвращает нижнее значение.
- `age(boundary="above_max")` возвращает значение выше максимума.
- `full_name(max_total_length=10)` не возвращает строку длиннее 10 символов.
- `plan_example(allowed_plans=["free", "premium"])` выбирает только из этих планов подписки.
- `reg_date_example(boundary="min")` возвращает первую разрешенную дату.

## Команда 2. Строки, контакты, списки и профиль

Реализовать:

- `city(starts_with=None, seed=None)`
- `phone(valid=True, seed=None)`
- `email(valid=True, username_length=8, seed=None)`
- `username(length=10, seed=None)`
- `comment(length=100, seed=None)`
- `password(length=12, use_digits=True, use_symbols=True, seed=None)`
- `tags(count=None, unique=True, seed=None)`
- `user_profile(valid=True, seed=None)`

Команда учится генерировать строки точной длины, делать валидные и невалидные данные, проверять формат email и телефона, добавлять цифры и спецсимволы в пароль, создавать списки нужного размера, делать элементы уникальными и собирать большой словарь профиля.

Примеры требований:

- `comment(length=255)` возвращает строку ровно 255 символов.
- `email(valid=True)` возвращает строку со знаком `@`.
- `email(valid=False)` возвращает намеренно неправильный email.
- `password(length=16, use_digits=True, use_symbols=True)` возвращает пароль длиной 16 символов с цифрой и спецсимволом.
- `tags(count=5, unique=True)` возвращает 5 уникальных тегов.
- `user_profile(valid=False)` возвращает профиль с намеренно неправильным email.
