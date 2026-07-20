# Функции генераторов

Этот файл заменяет отдельный список генераторов для реализации. Здесь есть все: что нужно написать, какие функции уже являются образцами, что принимает и возвращает каждая функция, как проверять результат и где такие генераторы применяются на практике.

## Базовые слова

Входные данные - это значения в скобках функции. Например, в `age(min_age=18, max_age=80)` входные данные - `min_age` и `max_age`.
Выходные данные - это то, что функция отдает через `return`.
`seed` - это число для `random`. С одинаковым `seed` случайный выбор повторяется. Это нужно для тестов: они заранее знают, какой результат ждать. Если `seed=None`, результат может меняться.
Внутренние переменные можно называть по-своему. Тесты проверяют результат функции, а не названия переменных.

## Что нужно реализовать

В процедурной версии часть функций пока является заданием: внутри них стоит `pass`. Если вызвать такую функцию, она вернет `None`, значит ее нужно дописать.

Команда 1 реализует:

- `user_id(length=6, only_digits=True, seed=None)`
- `first_name(min_length=None, max_length=None, seed=None)`
- `last_name(min_length=None, max_length=None, seed=None)`
- `full_name(max_total_length=None, seed=None)`
- `age(min_age=18, max_age=80, boundary=None, seed=None)`
- `birth_year(min_year=1950, max_year=2008, boundary=None, seed=None)`

Команда 2 реализует:

- `city(starts_with=None, seed=None)`
- `phone(valid=True, seed=None)`
- `email(valid=True, username_length=8, seed=None)`
- `username(length=10, seed=None)`
- `comment(length=100, seed=None)`
- `password(length=12, use_digits=True, use_symbols=True, seed=None)`
- `tags(count=None, unique=True, seed=None)`
- `user_profile(valid=True, seed=None)`

## Функции-образцы

Эти функции уже написаны полностью. Их не нужно дописывать, их нужно открыть и изучить.

- `score_example(min_score=1, max_score=100, boundary=None, seed=None)` -> `procedural_version/generators/score_example.py`
- `active_example(seed=None)` -> `procedural_version/generators/active_example.py`
- `plan_example(allowed_plans=None, seed=None)` -> `procedural_version/generators/plan_example.py`
- `reg_date_example(start_year=2020, end_year=2026, boundary=None, seed=None)` -> `procedural_version/generators/reg_date_example.py`

Эти файлы являются образцами: они уже работают и показывают, как писать похожий код.

## Как импортировать функции

Все процедурные генераторы можно импортировать из `procedural_version.generators` по настоящим коротким именам:

```python
from procedural_version.generators import email, password, reg_date_example

print(email(valid=True, seed=1))
print(password(length=12, seed=1))
print(reg_date_example(seed=1))
```

## Как генераторы используются на практике

Генераторы нужны, чтобы быстро получать данные для проверки программ. Вместо того чтобы каждый раз вручную придумывать имя, email, пароль, телефон или дату, программа вызывает функцию-генератор.

Пример 1. Проверка формы регистрации на сайте:

```python
from procedural_version.generators import email, password

user_email = email(valid=True, username_length=8, seed=1)
user_password = password(length=12, use_digits=True, use_symbols=True, seed=1)

print(user_email)
print(user_password)
```

Эти данные можно вставить в форму регистрации или отправить в API.

Пример 2. Проверка ошибки в форме:

```python
from procedural_version.generators import email

bad_email = email(valid=False, seed=1)
print(bad_email)
```

Такой email специально неправильный. Его используют, чтобы проверить, что сайт показывает ошибку.

Пример 3. Проверка минимального и максимального возраста:

```python
from procedural_version.generators import age

print(age(min_age=18, max_age=80, boundary="min"))
print(age(min_age=18, max_age=80, boundary="max"))
print(age(min_age=18, max_age=80, boundary="below_min"))
print(age(min_age=18, max_age=80, boundary="above_max"))
```

Так проверяют правила вроде “пользователь должен быть не младше 18 лет”.

Пример 4. Создание целого профиля пользователя:

```python
from oop_version.generators.profile_generator import ProfileGenerator

generator = ProfileGenerator(seed=1)
profile = generator.user_profile(valid=True)
print(profile)
```

Такой словарь можно использовать в автотесте, в демонстрационном проекте, в учебной базе данных или в моковом API.

Пример 5. Проверка повторяемости:

```python
from procedural_version.generators import reg_date_example

print(reg_date_example(seed=1))
print(reg_date_example(seed=1))
```

Обе строки должны быть одинаковыми. Это помогает искать ошибки: если результат повторяется, тест легче проверить.

## Общие правила проверки

Числа: проверяй обычное значение внутри диапазона, `boundary="min"`, `boundary="max"`, `boundary="below_min"`, `boundary="above_max"`.
Строки: проверяй точную длину, минимальную длину, максимальную длину и обязательные символы.
Форматы: проверяй валидный email, невалидный email, валидный телефон, невалидный телефон и дату `YYYY-MM-DD`.
Структуры: проверяй количество тегов, уникальность тегов, обязательные ключи профиля, валидный и невалидный профиль.

## Спецификации функций

### `user_id(length=6, only_digits=True, seed=None)`

Вход: `length` - сколько символов в ID; `only_digits=True` - только цифры; `only_digits=False` - цифры и английские буквы; `seed` - число для повторяемого random или `None`.
Выход: строка длиной ровно `length`.
Проверить: тип `str`, точную длину, только цифры при `only_digits=True`, буквы и цифры при `only_digits=False`, повторяемость при одинаковом `seed`, ошибку при `length <= 0`.
Пример:

```python
user_id(length=8, only_digits=True, seed=1)
```

### `first_name(min_length=None, max_length=None, seed=None)`

Вход: `min_length` - минимальная длина имени или `None`; `max_length` - максимальная длина имени или `None`; `seed` - число для повторяемого random или `None`.
Выход: имя из списка `FIRST_NAMES`.
Проверить: тип `str`, имя есть в списке, длина подходит под `min_length` и `max_length`, ошибка при отсутствии подходящих имен.
Пример:

```python
first_name(min_length=5, seed=1)
```

### `last_name(min_length=None, max_length=None, seed=None)`

Вход: `min_length` - минимальная длина фамилии или `None`; `max_length` - максимальная длина фамилии или `None`; `seed` - число для повторяемого random или `None`.
Выход: фамилия из списка `LAST_NAMES`.
Проверить: тип `str`, фамилия есть в списке, длина подходит под `min_length` и `max_length`, ошибка при отсутствии подходящих фамилий.
Пример:

```python
last_name(max_length=7, seed=1)
```

### `full_name(max_total_length=None, seed=None)`

Вход: `max_total_length` - максимальная длина полного имени или `None`; `seed` - число для повторяемого random или `None`.
Выход: строка вида `"Имя Фамилия"`.
Проверить: тип `str`, пробел между именем и фамилией, длину не больше `max_total_length`, если он передан.
Пример:

```python
full_name(max_total_length=10, seed=1)
```

### `age(min_age=18, max_age=80, boundary=None, seed=None)`

Вход: `min_age` - самый маленький разрешенный возраст; `max_age` - самый большой разрешенный возраст; `boundary` - специальный режим; `seed` - число для повторяемого random или `None`.
Выход: целое число.
Проверить: обычный режим возвращает число от `min_age` до `max_age`; `boundary="min"` возвращает `min_age`; `boundary="max"` возвращает `max_age`; `boundary="below_min"` возвращает `min_age - 1`; `boundary="above_max"` возвращает `max_age + 1`; при `min_age > max_age` нужна ошибка.
Пример:

```python
age(min_age=18, max_age=80, boundary="above_max")
```

### `birth_year(min_year=1950, max_year=2008, boundary=None, seed=None)`

Вход: `min_year` - самый ранний разрешенный год; `max_year` - самый поздний разрешенный год; `boundary` - специальный режим; `seed` - число для повторяемого random или `None`.
Выход: целое число.
Проверить: обычный режим возвращает год от `min_year` до `max_year`; `boundary="min"` возвращает `min_year`; `boundary="max"` возвращает `max_year`; `boundary="below_min"` возвращает `min_year - 1`; `boundary="above_max"` возвращает `max_year + 1`; при `min_year > max_year` нужна ошибка.
Пример:

```python
birth_year(min_year=1950, max_year=2008, boundary="min")
```

### `score_example(min_score=1, max_score=100, boundary=None, seed=None)`

Файл: `procedural_version/generators/score_example.py`. Это функция-образец для генератора числа.
Вход: `min_score` - самый маленький балл; `max_score` - самый большой балл; `boundary` - специальный режим; `seed` - число для повторяемого random или `None`.
Выход: целое число с баллом.
Пример:

```python
from procedural_version.generators import score_example

print(score_example(boundary="min"))
print(score_example(boundary="max"))
print(score_example(seed=1))
```

### `active_example(seed=None)`

Файл: `procedural_version/generators/active_example.py`. Это функция-образец для выбора `True` или `False`.
Вход: `seed` - число для повторяемого random или `None`.
Выход: `True` или `False`.
Пример:

```python
from procedural_version.generators import active_example

print(active_example(seed=1))
```

### `plan_example(allowed_plans=None, seed=None)`

Файл: `procedural_version/generators/plan_example.py`. Это функция-образец для выбора плана подписки. План подписки - это вариант аккаунта пользователя, например `"free"` или `"premium"`.
Вход: `allowed_plans` - список разрешенных планов подписки или `None`; `seed` - число для повторяемого random или `None`.
Выход: строка с названием плана подписки.
Пример:

```python
from procedural_version.generators import plan_example

print(plan_example(allowed_plans=["free", "premium"], seed=1))
```

### `reg_date_example(start_year=2020, end_year=2026, boundary=None, seed=None)`

Файл: `procedural_version/generators/reg_date_example.py`. Это функция-образец для генерации даты.
Вход: `start_year` - первый разрешенный год; `end_year` - последний разрешенный год; `boundary` - специальный режим; `seed` - число для повторяемого random или `None`.
Выход: строка даты в формате `YYYY-MM-DD`.
Пример:

```python
from procedural_version.generators import reg_date_example

print(reg_date_example(boundary="min"))
print(reg_date_example(boundary="max"))
print(reg_date_example(seed=1))
```

### `city(starts_with=None, seed=None)`

Вход: `starts_with` - начало названия города или `None`; `seed` - число для повторяемого random или `None`.
Выход: город из списка `CITY_NAMES`.
Проверить: тип `str`, город есть в списке, город начинается с `starts_with`, если этот параметр передан, ошибка при отсутствии подходящих городов.
Пример:

```python
city(starts_with="М", seed=1)
```

### `phone(valid=True, seed=None)`

Вход: `valid=True` - правильный телефон; `valid=False` - телефон с ошибкой; `seed` - число для повторяемого random или `None`.
Выход: словарь с ключами `country_code`, `operator_code`, `number`.
Проверить: при `valid=True` код страны равен `"+7"`, `operator_code` от `900` до `999`, `number` от `1000000` до `9999999`; при `valid=False` данные намеренно неправильные.
Пример:

```python
phone(valid=False, seed=1)
```

### `email(valid=True, username_length=8, seed=None)`

Вход: `valid=True` - правильный email; `valid=False` - email с ошибкой; `username_length` - длина части email до `@`; `seed` - число для повторяемого random или `None`.
Выход: строка email.
Проверить: при `valid=True` строка содержит `@`, часть до `@` имеет длину `username_length`; при `valid=False` email намеренно неправильный; при `username_length <= 0` нужна ошибка.
Пример:

```python
email(valid=True, username_length=8, seed=1)
```

### `username(length=10, seed=None)`

Вход: `length` - нужная длина username; `seed` - число для повторяемого random или `None`.
Выход: строка username.
Проверить: тип `str`, длину ровно `length`, символы из маленьких английских букв, цифр и `_`, ошибку при `length <= 0`.
Пример:

```python
username(length=12, seed=1)
```

### `comment(length=100, seed=None)`

Вход: `length` - нужная длина комментария; `seed` - число для повторяемого random или `None`.
Выход: строка ровно заданной длины.
Проверить: `length=0` возвращает пустую строку; `length=1`, `length=255`, `length=1000` возвращают строки нужной длины; при `length < 0` нужна ошибка.
Пример:

```python
comment(length=255, seed=1)
```

### `password(length=12, use_digits=True, use_symbols=True, seed=None)`

Вход: `length` - длина пароля; `use_digits=True` - нужна хотя бы одна цифра; `use_symbols=True` - нужен хотя бы один спецсимвол; `seed` - число для повторяемого random или `None`.
Выход: строка пароля.
Проверить: длину ровно `length`, цифру при `use_digits=True`, спецсимвол при `use_symbols=True`, ошибку при `length <= 0`.
Пример:

```python
password(length=16, use_digits=True, use_symbols=True, seed=1)
```

### `tags(count=None, unique=True, seed=None)`

Вход: `count` - сколько тегов вернуть или `None`; `unique=True` - теги не повторяются; `unique=False` - повторы разрешены; `seed` - число для повторяемого random или `None`.
Выход: список тегов.
Проверить: тип `list`, длину `count`, уникальность при `unique=True`, наличие всех тегов в списке `TAGS`, ошибку при `count < 0`.
Пример:

```python
tags(count=5, unique=True, seed=1)
```

### `user_profile(valid=True, seed=None)`

Вход: `valid=True` - профиль с правильным email; `valid=False` - профиль с email-ошибкой; `seed` - число для повторяемого random или `None`.
Выход: словарь профиля пользователя.
Проверить: тип `dict`; ключи `user_id`, `first_name`, `last_name`, `age`, `city`, `is_active`, `username`, `email`, `password`, `tags`, `registration_date`, `subscription_plan`; длину `user_id` 6, `username` 10, `password` 12; 3 уникальных тега; правильный email при `valid=True`; неправильный email при `valid=False`.
Пример:

```python
user_profile(valid=False, seed=1)
```
