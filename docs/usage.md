# Инструкция по использованию библиотеки

## Общая идея

Проект содержит две версии одной библиотеки генерации тестовых данных:

1. `procedural_version` — процедурная версия.
2. `oop_version` — объектно-ориентированная версия.

Библиотека нужна не только для случайного выбора данных.

Она помогает создавать тестовые данные под конкретные проверки:

- строки точной длины;
- числа на границах диапазона;
- числа за границами диапазона;
- валидные форматы;
- невалидные форматы;
- списки нужного размера;
- сложные профили пользователей.

`seed` - это число для `random`.
Если два раза запустить функцию с одинаковым `seed`, случайный выбор должен повториться.
Например, два запуска с `seed=1` должны вернуть одно и то же значение.

В процедурной версии часть функций пока является заданием для учеников.
В таких функциях внутри стоит `pass`.

А 4 функции уже написаны полностью.
Они нужны не для задания, а как образец: ученик может открыть файл, посмотреть готовый код и понять, как писать похожие функции.

Эти функции-образцы находятся в папке:

```text
procedural_version/generators/
```

Файлы-образцы:

- `score_example.py`
- `active_example.py`
- `plan_example.py`
- `reg_date_example.py`

Функции внутри этих файлов:

- `score_example(min_score=1, max_score=100, boundary=None, seed=None)`
- `active_example(seed=None)`
- `plan_example(allowed_plans=None, seed=None)`
- `reg_date_example(start_year=2020, end_year=2026, boundary=None, seed=None)`

Например, короткая функция `score` связана с файлом:

```text
procedural_version/generators/score_example.py
```

Запускать команды нужно из корня проекта. Это папка, где лежат `procedural_version`, `oop_version` и `docs`.

Пример структуры:

```text
gen_test_data/
  procedural_version/
  oop_version/
  docs/
```

Linux/macOS:

```bash
cd ~/projects/gen_test_data
```

Windows PowerShell:

```powershell
cd C:\Users\Student\Projects\gen_test_data
```

Путь может быть другим. Важно запускать команды из папки проекта.

---

# Как проверить функцию руками без автотестов

Создай файл `manual_check.py` в корне проекта.

Пример проверки готовой функции с баллом:

```python
from procedural_version.generators import score_example

print(score_example(min_score=1, max_score=100, boundary="min"))
print(score_example(min_score=1, max_score=100, boundary="max"))
print(score_example(min_score=1, max_score=100, seed=1))
print(score_example(min_score=1, max_score=100, seed=1))
```

Запусти файл:

```bash
python manual_check.py
```

Как понять, что все нормально:

- программа не упала с ошибкой;
- `boundary="min"` напечатал `1`;
- `boundary="max"` напечатал `100`;
- два одинаковых вызова с `seed=1` напечатали одинаковые числа.

Пример проверки готовой функции с датой:

```python
from procedural_version.generators import reg_date_example

print(reg_date_example(boundary="min"))
print(reg_date_example(boundary="max"))
print(reg_date_example(seed=1))
print(reg_date_example(seed=1))
```

Как понять, что все нормально:

- первая строка должна быть `2020-01-01`;
- вторая строка должна быть `2026-12-28`;
- две строки с `seed=1` должны быть одинаковыми;
- дата должна выглядеть так: `год-месяц-день`, например `2021-10-28`.

Пример проверки своей функции после реализации:

```python
from procedural_version.generators import age

print(age(min_age=18, max_age=80, boundary="min"))
print(age(min_age=18, max_age=80, boundary="max"))
print(age(min_age=18, max_age=80, seed=1))
```

Если функция еще не реализована и внутри стоит `pass`, на экране появится `None`: значит, функцию еще нужно написать.

---

# Как подключить библиотеку к другому проекту

Самый простой учебный способ - положить папку библиотеки рядом со своим файлом Python.

Пример для процедурной версии:

```text
my_project/
  main.py
  procedural_version/
```

Пример файла `main.py`:

```python
from procedural_version.generators import score_example

result = score_example(seed=1)
print(result)
```

Пример для ООП-версии:

```text
my_project/
  main.py
  oop_version/
```

Пример файла `main.py`:

```python
from oop_version.generators.profile_generator import ProfileGenerator

generator = ProfileGenerator(seed=1)
profile = generator.user_profile(valid=True)
print(profile)
```

Если папка библиотеки лежит не рядом с `main.py`, Python может не найти импорт. Тогда проще всего запускать код из корня проекта или перенести папку библиотеки рядом с файлом, который ее использует.

---

# Процедурная версия

## Числа и границы

```python
from procedural_version.generators import age

print(age(min_age=18, max_age=80, boundary="min"))
print(age(min_age=18, max_age=80, boundary="max"))
print(age(min_age=18, max_age=80, boundary="above_max"))
```

```python
from procedural_version.generators import score_example

print(score_example(min_score=1, max_score=100, boundary="below_min"))
```

## Строки точной длины

```python
from procedural_version.generators import comment

text = comment(length=255, seed=1)
print(len(text))
```

```python
from procedural_version.generators import username

name = username(length=12, seed=1)
print(name)
print(len(name))
```

## Валидные и невалидные форматы

```python
from procedural_version.generators import email

print(email(valid=True, username_length=8, seed=1))
print(email(valid=False, username_length=8, seed=1))
```

```python
from procedural_version.generators import phone

print(phone(valid=True, seed=1))
print(phone(valid=False, seed=1))
```

## Пароль с требованиями

```python
from procedural_version.generators import password

result = password(length=16, use_digits=True, use_symbols=True, seed=1)
print(result)
print(len(result))
```

## Списки и профиль

```python
from procedural_version.generators import tags

result = tags(count=5, unique=True, seed=1)
print(result)
```

```python
from procedural_version.generators import user_profile

print(user_profile(valid=True, seed=1))
print(user_profile(valid=False, seed=1))
```

---

# ООП-версия

## Числа и границы

```python
from oop_version.generators.person_generator import PersonGenerator

person_generator = PersonGenerator(seed=1)
print(person_generator.age(min_age=18, max_age=80, boundary="min"))
```

```python
from oop_version.generators.person_generator import PersonGenerator

person_generator = PersonGenerator(seed=1)
print(person_generator.score(min_score=1, max_score=100, boundary="max"))
```

## Строки точной длины

```python
from oop_version.generators.text_generator import TextGenerator

text_generator = TextGenerator(seed=1)
comment = text_generator.comment(length=255)
print(len(comment))
```

```python
from oop_version.generators.person_generator import PersonGenerator

person_generator = PersonGenerator(seed=1)
username = person_generator.username(length=12)
print(username)
print(len(username))
```

## Валидные и невалидные форматы

```python
from oop_version.generators.contact_generator import ContactGenerator

contact_generator = ContactGenerator(seed=1)
print(contact_generator.email(valid=True, username_length=8))
print(contact_generator.email(valid=False, username_length=8))
```

## Сложный профиль

```python
from oop_version.generators.profile_generator import ProfileGenerator

profile_generator = ProfileGenerator(seed=1)
print(profile_generator.user_profile(valid=True))
print(profile_generator.user_profile(valid=False))
```

---

# Как запустить тесты

```bash
python check.py all
python check.py oop
```

Если тесты завершились со статусом `OK`, значит проверяемая часть работает правильно.
