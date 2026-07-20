# Импортируем короткие учебные имена всех процедурных генераторов.
from procedural_version.generators import active_example, age, birth_year, city, comment, email, full_name, password, phone, plan_example, reg_date_example, score_example, tags, user_id, user_profile, username

# Проверяем, что файл запущен напрямую, а не импортирован как модуль.
if __name__ == "__main__":
    # Печатаем пример цифрового ID пользователя.
    print(user_id(seed=1))
    # Печатаем пример возраста пользователя.
    print(age(seed=1))
    # Печатаем пример года рождения пользователя.
    print(birth_year(seed=1))
    # Печатаем пример длинного комментария.
    print(comment(seed=1))
    # Печатаем пример адреса электронной почты.
    print(email(seed=1))
    # Печатаем пример номера телефона.
    print(phone(seed=1))
    # Печатаем пример учебного пароля.
    print(password(seed=1))
    # Печатаем пример города.
    print(city(seed=1))
    # Печатаем пример даты регистрации пользователя.
    print(reg_date_example(seed=1))
    # Печатаем пример учебного балла.
    print(score_example(seed=1))
    # Печатаем пример признака активности.
    print(active_example(seed=1))
    # Печатаем пример плана подписки пользователя.
    print(plan_example(seed=1))
    # Печатаем пример списка тегов.
    print(tags(seed=1))
    # Печатаем пример username пользователя.
    print(username(seed=1))
    # Печатаем пример профиля пользователя.
    print(user_profile(seed=1))
    # Печатаем пример полного имени.
    print(full_name(seed=1))
