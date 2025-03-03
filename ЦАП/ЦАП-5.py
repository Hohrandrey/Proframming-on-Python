from math import ceil

def main(z, y, x):
    total_sum = 0
    n = len(z)
    for i in range(1, n):
        idx = n + 1 - ceil(i / 4)
        print(i)
        print(idx)
        f = 5 * ((z[idx - 1]) ** 2)
        s = 96 * y[idx - 1]
        t = 40 * ((x[n + 1 - i - 1]) ** 3)
        total_sum += (f + s + t) ** 2
    return total_sum


print(main([0.64, 0.91, 0.46, -0.0, 0.57],
           [0.69, -0.06, 0.21, 0.87, -0.48],
           [0.65, -0.01, 0.49, -0.19, 0.41]))  # ≈ 1.62e+04

print(main([0.81, 0.29, 0.68, -0.61, 0.28],
           [-0.28, -0.75, -0.77, -0.87, 0.6],
           [0.1, 0.7, 0.39, 0.35, -0.33]))  # ≈ 2.22e+04

print(main([-0.0, -0.05, -0.1, -0.12, 0.08],
           [-0.41, -0.97, 0.18, 0.04, -0.44],
           [-0.21, -0.28, -0.43, 0.21, -0.41]))  # ≈ 7.70e+03

print(main([0.09, -0.53, -0.97, 0.84, -0.71],
           [0.52, -0.15, -0.13, 0.3, 0.12],
           [0.87, 0.49, -0.86, -0.29, 0.9]))  # ≈ 5.96e+03

print(main([0.17, -0.79, 0.72, -0.44, -0.09],
           [-0.1, -0.2, 0.86, 0.68, -0.73],
           [0.43, 0.82, 0.6, 0.48, -0.63]))  # ≈ 2.16e+04
