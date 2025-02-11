#1 варик
import math

def main(z, x):
    numerator = ((x ** 2 / 8 + z) ** 6 - (84 * x ** 3 + x) ** 7)

    # Вычисляем знаменатель
    denominator = (z ** 8 / 13) - math.exp((x ** 2 + 2) + z / 19)

    result = numerator / denominator

    sec = (math.ceil(z)) ** 3
    last = 33 * (17 * (x ** 2)) ** 5

    f = result + sec + last
    return f


if __name__ == "__main__":
    print(main(0.03, -0.37))
    print(main(0.29, -0.23))
    print(main(-0.2, 0.66))
    print(main(-0.02, 0.04))
    print(main(0.65, -0.06))

#2 варик

def main(z, x):
    import math
    # Итоговое значение
    return (
        ((x ** 2 / 8 + z) ** 6 - (84 * x ** 3 + x) ** 7)
        / ((z ** 8 / 13) - math.exp((x ** 2 + 2) + z / 19))
        + (math.ceil(z) ** 3)
        + (33 * (17 * (x ** 2)) ** 5)
    )


if __name__ == "__main__":
    print(main(0.03, -0.37))
    print(main(0.29, -0.23))
    print(main(-0.2, 0.66))
    print(main(-0.02, 0.04))
    print(main(0.65, -0.06))

#3 варик

from math import ceil, exp


def main(z, x):
    # Итоговое значение
    return (
            ((x ** 2 / 8 + z) ** 6 - (84 * x ** 3 + x) ** 7)
            / ((z ** 8 / 13) - exp((x ** 2 + 2) + z / 19))
            + (ceil(z) ** 3)
            + (33 * (17 * (x ** 2)) ** 5)
    )


if __name__ == "__main__":
    print(main(0.03, -0.37))
    print(main(0.29, -0.23))
    print(main(-0.2, 0.66))
    print(main(-0.02, 0.04))
    print(main(0.65, -0.06))

#4 варик

def main(z, x):
    # Число Эйлера
    e = 2.718281828459045

    # Вычисляем числитель
    numerator = ((x ** 2 / 8 + z) ** 6 - (84 * x ** 3 + x) ** 7)

    # Вычисляем знаменатель
    denominator = (z ** 8 / 13) - (e ** ((x ** 2 + 2) + z / 19))

    result = numerator / denominator

    # Ручное округление вверх (замена math.ceil)
    if z > 0:
        sec = (int(z) + 1) ** 3
    else:
        sec = int(z) ** 3

    # Вычисляем last
    last = 33 * (17 * (x ** 2)) ** 5

    # Итоговое значение
    return result + sec + last


if __name__ == "__main__":
    print(main(0.03, -0.37))
    print(main(0.29, -0.23))
    print(main(-0.2, 0.66))
    print(main(-0.02, 0.04))
    print(main(0.65, -0.06))