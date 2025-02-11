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
