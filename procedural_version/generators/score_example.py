# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем готовый пример функции учебного балла.
def score_example(min_score=1, max_score=100, boundary=None, seed=None):
    # Что делает функция: возвращает число-балл.
    # min_score - самый маленький балл, например 1.
    # max_score - самый большой балл, например 100.
    # boundary - это режим для специальных проверок в тестах.
    # boundary="min" значит вернуть min_score, например 1.
    # boundary="max" значит вернуть max_score, например 100.
    # boundary="below_min" значит вернуть число меньше минимума, например 0.
    # boundary="above_max" значит вернуть число больше максимума, например 101.
    # boundary=None значит выбрать случайный балл от min_score до max_score.
    # seed - число для random: с одним и тем же seed random выбирает один и тот же балл.
    # Можно вызвать score_example() и получить случайный балл от 1 до 100.
    # Можно вызвать score_example(boundary="min") и получить 1.
    # Можно вызвать score_example(min_score=10, max_score=20) и получить балл от 10 до 20.
    # Можно вызвать score_example(min_score=10, max_score=20, boundary="max") и получить 20.
    # Пример вызова: score_example(boundary="above_max") должен вернуть 101.
    # Документация: docs/function_specifications.md, раздел score.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py score_example
    # Если в конце написано OK, этот тест прошел.
    # Что вернуть: целое число.
    # Проверка тестами: python check.py score_example
    # Проверяем, что нижняя граница не больше верхней.
    if min_score > max_score:
        # Сообщаем ошибку, если диапазон написан наоборот.
        raise ValueError("min_score не должен быть больше max_score")
    # Возвращаем нижнюю границу.
    if boundary == "min":
        # Возвращаем min_score.
        return min_score
    # Возвращаем верхнюю границу.
    if boundary == "max":
        # Возвращаем max_score.
        return max_score
    # Возвращаем число ниже нижней границы.
    if boundary == "below_min":
        # Возвращаем min_score минус 1.
        return min_score - 1
    # Возвращаем число выше верхней границы.
    if boundary == "above_max":
        # Возвращаем max_score плюс 1.
        return max_score + 1
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Возвращаем случайный балл внутри диапазона.
    return randomizer.randint(min_score, max_score)
