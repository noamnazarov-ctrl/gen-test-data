# Подключаем модуль random, чтобы создавать случайные значения.
import random

# Объявляем функцию, которая создает отдельный генератор случайности.
def create_random(seed=None):
    # Возвращаем генератор случайных чисел с переданным seed или без него.
    return random.Random(seed)

# Объявляем функцию, которая выбирает один случайный элемент из списка.
def choose_item(items, seed=None, randomizer=None):
    # Создаем генератор случайности, если его не передали снаружи.
    current_randomizer = randomizer or create_random(seed)
    # Возвращаем случайный элемент из переданного списка.
    return current_randomizer.choice(items)
