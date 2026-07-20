# Импортируем общий список планов подписки.
from procedural_version.data.names_data import SUBSCRIPTION_PLANS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем готовый пример функции плана подписки.
def plan_example(allowed_plans=None, seed=None):
    # Что делает функция: выбирает один план подписки.
    # План подписки - это вариант аккаунта пользователя.
    # Примеры планов подписки: "free", "basic", "premium".
    # allowed_plans=None значит выбрать из общего списка SUBSCRIPTION_PLANS.
    # allowed_plans=["free", "premium"] значит выбрать только "free" или "premium".
    # allowed_plans=[] значит выбирать не из чего, поэтому нужна ошибка ValueError.
    # seed - число для random: с одним и тем же seed random выбирает один и тот же план.
    # Можно вызвать plan_example() и выбрать план из общего списка.
    # Можно вызвать plan_example(allowed_plans=["free", "premium"]) и выбрать только из двух планов.
    # Можно вызвать plan_example(allowed_plans=["free"], seed=1) и получить "free".
    # Пример вызова: plan_example(allowed_plans=["free", "premium"], seed=1).
    # Документация: docs/function_specifications.md, раздел plan.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py plan_example
    # Если в конце написано OK, этот тест прошел.
    # Что вернуть: строку с одним планом подписки.
    # Проверка тестами: python check.py plan_example
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Выбираем список: переданный allowed_plans или общий SUBSCRIPTION_PLANS.
    plans = allowed_plans if allowed_plans is not None else SUBSCRIPTION_PLANS
    # Проверяем, что список планов не пустой.
    if not plans:
        # Сообщаем ошибку, если выбирать не из чего.
        raise ValueError("Список планов подписки не должен быть пустым")
    # Возвращаем случайный план из выбранного списка.
    return randomizer.choice(plans)
