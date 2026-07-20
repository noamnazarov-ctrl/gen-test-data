# Подсказка ученику: SUBSCRIPTION_PLANS хранит общий список планов подписки.
# План подписки - это вариант аккаунта пользователя, например "free", "basic" или "premium".
from procedural_version.data.names_data import SUBSCRIPTION_PLANS
# Подсказка ученику: create_random(seed) нужен для повторяемого выбора плана подписки в тестах.
from procedural_version.utils.random_utils import create_random

# Пример готового решения: по нему можно понять, как делать похожие генераторы.
def generate_subscription_plan_example(allowed_plans=None, seed=None):
    # Где почитать про эту функцию: открой docs/function_specifications.md и найди раздел generate_subscription_plan_example.
    # Где посмотреть задание команды: открой docs/team_tasks.md и найди generate_subscription_plan_example.
    # Где посмотреть пример использования: открой docs/usage.md и найди generate_subscription_plan_example.
    # seed помогает получать одинаковый случайный результат.
    # Например, generate_subscription_plan_example(seed=1) и еще раз generate_subscription_plan_example(seed=1) должны вернуть один и тот же план.
    # Это удобно для тестов: тест знает, какой результат должен получиться.
    # Если seed=None, результат может быть разным при каждом запуске.
    # Входные данные - это значения в скобках функции.
    # Входные данные: allowed_plans - список разрешенных планов подписки или None для общего списка.
    # Входные данные: seed - число для повторения случайного результата или None.
    # Переменные внутри функции можно называть по-своему.
    # Тесты проверяют результат функции, а не названия переменных.
    # Ниже перечислены примеры понятных названий переменных.
    # Внутренние переменные: randomizer - генератор случайности, который создается через create_random(seed).
    # Внутренние переменные: plans - список планов подписки, из которого функция будет выбирать результат.
    # Выходные данные - это значение, которое функция отдает с помощью return.
    # Выходные данные: функция должна вернуть строку с названием плана подписки.
    # Шаг 1. Создай генератор случайности через create_random(seed).
    randomizer = create_random(seed)
    # Шаг 2. Если allowed_plans передан, выбирай план подписки только из него.
    # Шаг 3. Если allowed_plans не передан, используй общий список SUBSCRIPTION_PLANS.
    plans = allowed_plans if allowed_plans is not None else SUBSCRIPTION_PLANS
    # Шаг 4. Проверь, что список планов подписки не пустой.
    if not plans:
        # Проверка тестом: при пустом списке функция должна выбросить ValueError.
        raise ValueError("Список планов подписки не должен быть пустым")
    # Шаг 5. Верни случайный план подписки из выбранного списка.
    # Проверка тестом: результат должен входить в allowed_plans или SUBSCRIPTION_PLANS.
    # Как проверить работу: запусти в терминале python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_subscription_plan_example_respects_allowed_plans
    # Если все правильно, в самом конце появится слово OK.
    # Если вместо OK появилась ошибка, проверь, что функция выбирает план подписки только из allowed_plans.
    return randomizer.choice(plans)
