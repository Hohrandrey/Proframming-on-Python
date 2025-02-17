import math


def main(a, b, y):
    total = 0
    for j in range(1, b + 1):
        for c in range(1, a + 1):
            term = 72 * math.log2(90 * y + j**2 + 45 * c**3) + 1 + j**4
            total += term
    return total


if __name__ == "__main__":
    print(main(5, 2, 0.43))
    print(main(7, 8, 0.57))
    print(main(7, 6, 0.83))
    print(main(2, 6, -0.41))
    print(main(4, 8, 0.32))
