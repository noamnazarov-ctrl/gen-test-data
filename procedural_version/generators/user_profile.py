# Импортируем список имен.
from procedural_version.data.names_data import FIRST_NAMES
# Импортируем список фамилий.
from procedural_version.data.names_data import LAST_NAMES
# Импортируем список городов.
from procedural_version.data.names_data import CITY_NAMES
# Импортируем список планов подписки.
from procedural_version.data.names_data import SUBSCRIPTION_PLANS
# Импортируем пример готовой функции даты регистрации.
from procedural_version.generators.reg_date_example import reg_date_example
# Импортируем функцию email.
from procedural_version.generators.email import email
# Импортируем функцию пароля.
from procedural_version.generators.password import password
# Импортируем функцию тегов.
from procedural_version.generators.tags import tags
# Импортируем функцию username.
from procedural_version.generators.username import username
# Импортируем функцию ID.
from procedural_version.generators.user_id import user_id
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random
# Импортируем помощник для выбора случайного элемента.
from procedural_version.utils.random_utils import choose_item

# Объявляем функцию, которая должна вернуть полный профиль пользователя.
def user_profile(valid=True, seed=None):
    # Что делает функция: собирает один большой словарь с данными пользователя.
    # valid=True значит email внутри профиля должен быть правильным и содержать @.
    # valid=False значит email внутри профиля должен быть специально неправильным.
    # seed - число для random: с одним и тем же seed random собирает один и тот же профиль.
    # В словаре должны быть ключи: user_id, first_name, last_name, age, city, is_active.
    # В словаре также должны быть ключи: username, email, password, tags, registration_date, subscription_plan.
    # user_id должен быть строкой длиной 6.
    # username должен быть строкой длиной 10.
    # password должен быть строкой длиной 12.
    # tags должен быть списком из 3 уникальных тегов.
    # subscription_plan - это план подписки, например "free" или "premium".
    # Можно вызвать user_profile() и получить профиль с правильным email.
    # Можно вызвать user_profile(valid=False) и получить профиль с неправильным email.
    # Можно вызвать user_profile(seed=1) два раза и получить одинаковые профили.
    # Пример вызова: user_profile(valid=False, seed=1) должен вернуть словарь с email без @.
    # Документация: docs/function_specifications.md, раздел user_profile.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py user_profile
    # Если в конце написано OK, этот тест прошел.
    # Что вернуть: словарь dict.
    # Тесты: test_user_profile_fields, test_user_profile_invalid_email.
    pass
