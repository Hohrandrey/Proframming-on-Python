import math


def main(n):
    if n == 0:
        return 0.75
    elif n == 1:
        return -0.96

    # Инициализация значений для n = 0 и n = 1
    fn_minus_2 = 0.75  # f(0)
    fn_minus_1 = -0.96  # f(1)

    # Итеративное вычисление для n >= 2
    for i in range(2, n + 1):
        fn = 24 * (fn_minus_2 + 0.03) + math.cos(fn_minus_1) ** 2
        # Обновляем значения для следующей итерации
        fn_minus_2 = fn_minus_1
        fn_minus_1 = fn

    return fn
