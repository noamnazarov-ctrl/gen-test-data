# Генераторы для реализации

В проекте 18 генераторов.

Часть функций ученики реализуют сами.

4 функции уже сделаны как примеры:

- `generate_score_example(min_score=1, max_score=100, boundary=None, seed=None)`
- `generate_is_active_example(seed=None)`
- `generate_subscription_plan_example(allowed_plans=None, seed=None)`
- `generate_registration_date_example(start_year=2020, end_year=2026, boundary=None, seed=None)`

У этих примеров `example` есть и в названии файла, и в названии функции.

Смотрите эти 4 файла как образец готового решения:

- `procedural_version/generators/score_example.py`
- `procedural_version/generators/is_active_example.py`
- `procedural_version/generators/subscription_plan_example.py`
- `procedural_version/generators/registration_date_example.py`

---

# Что такое seed

`seed` помогает получать одинаковый случайный результат.

Например, если два раза вызвать функцию с `seed=1`, результат должен повториться.

Это удобно для тестов: тест знает, какой результат должен получиться.

Если `seed=None`, результат может быть разным при каждом запуске.

---

# Что нужно научиться делать

- создавать строки точной длины;
- выбирать случайные значения из списков;
- возвращать числа внутри диапазона;
- возвращать числа на границах диапазона;
- возвращать значения за границами для негативных тестов;
- делать валидные и невалидные email и телефоны;
- собирать списки и словари.

---

# Команда 1. Числа, границы и данные человека

Нужно реализовать:

- `generate_user_id(length=6, only_digits=True, seed=None)`
- `generate_first_name(min_length=None, max_length=None, seed=None)`
- `generate_last_name(min_length=None, max_length=None, seed=None)`
- `generate_full_name(max_total_length=None, seed=None)`
- `generate_age(min_age=18, max_age=80, boundary=None, seed=None)`
- `generate_birth_year(min_year=1950, max_year=2008, boundary=None, seed=None)`

Готовые примеры для изучения:

- `generate_score_example(min_score=1, max_score=100, boundary=None, seed=None)`
- `generate_is_active_example(seed=None)`
- `generate_subscription_plan_example(allowed_plans=None, seed=None)`
- `generate_registration_date_example(start_year=2020, end_year=2026, boundary=None, seed=None)`

---

# Команда 2. Строки, контакты, списки и профиль

Нужно реализовать:

- `generate_city(starts_with=None, seed=None)`
- `generate_phone(valid=True, seed=None)`
- `generate_email(valid=True, username_length=8, seed=None)`
- `generate_username(length=10, seed=None)`
- `generate_comment(length=100, seed=None)`
- `generate_password(length=12, use_digits=True, use_symbols=True, seed=None)`
- `generate_tags(count=None, unique=True, seed=None)`
- `generate_user_profile(valid=True, seed=None)`

---

# Что обязательно проверить

Для чисел:

- обычное значение внутри диапазона;
- `boundary="min"`;
- `boundary="max"`;
- `boundary="below_min"`;
- `boundary="above_max"`.

Для строк:

- точную длину строки;
- минимальную длину;
- максимальную длину;
- наличие обязательных символов.

Для форматов:

- валидный email;
- невалидный email;
- валидный телефон;
- невалидный телефон;
- дату в формате `YYYY-MM-DD`.

Для структур:

- количество тегов;
- уникальность тегов;
- наличие обязательных ключей в профиле;
- валидный и невалидный профиль.

---

# Как понять, что все нормально

Запустите нужный тест.

Если в конце вывода есть `OK`, значит тест прошел.

Если появилась ошибка, прочитайте, что ожидал тест и что вернула функция.
