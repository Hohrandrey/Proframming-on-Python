#1
def determinant_2x2(matrix):
    """
    Вычисляет определитель матрицы 2x2.
    """
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Матрица должна быть размером 2x2")

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    return a * d - b * c


# Пример использования:
matrix = [
    [4, 3],
    [1, 1]
]

det = determinant_2x2(matrix)
print(f"Определитель матрицы: {det}")

#2

def submatrix(A, i, j):
    """
    Возвращает подматрицу, полученную исключением i-й строки и j-го столбца из матрицы A.
    """
    n = len(A)
    m = len(A[0]) if n > 0 else 0
    new_matrix = []

    for row in range(n):
        if row == i:
            continue  # Пропускаем i-ю строку
        new_row = []
        for col in range(m):
            if col == j:
                continue  # Пропускаем j-й столбец
            new_row.append(A[row][col])
        new_matrix.append(new_row)

    return new_matrix

# Пример использования:
A = [
    [0, 2, 1],
    [1, 4, 3],
    [2, 1, 1]
]

# Тесты
print(submatrix(A, 0, 0))  # Ожидаемый результат: [[4, 3], [1, 1]]
print(submatrix(A, 1, 1))  # Ожидаемый результат: [[0, 1], [2, 1]]
print(submatrix(A, 2, 1))  # Ожидаемый результат: [[0, 1], [1, 3]]

#3

def smalldet(A):
    """
    Вычисляет определитель матрицы 2x2.
    """
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def det(A):
    """
    Рекурсивно вычисляет определитель матрицы n x n.
    """
    n = len(A)
    if n == 2:
        return smalldet(A)

    determinant = 0
    for j in range(n):
        sub_A = submatrix(A, 0, j)
        sign = (-1) ** j
        determinant += sign * A[0][j] * det(sub_A)

    return determinant


# Пример использования:
A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

# Вычисление определителя
result = det(A)
print(f"Определитель матрицы: {result}")

#4
def minor(A, i, j):
    """
    Вычисляет дополнительный минор элемента с индексами i и j.
    """
    sub_A = submatrix(A, i, j)
    return det(sub_A)


# Пример использования:
A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

# Вычисление дополнительного минора элемента a,0,1
result = minor(A, 0, 1)
print(f"Дополнительный минор элемента a,0,1: {result}")

#5
def alg(A, i, j):
    return (-1) ** (i + j) * minor(A, i, j)

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

alg_value = alg(A, 1, 1)
print("Алгебраическое дополнение элемента a_1,1:", alg_value)

#6
print("\n#6")
def algmatrix(A):
    n = len(A)
    return [[alg(A, i, j) for j in range(n)] for i in range(n)]

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

alg_mat = algmatrix(A)
print("Матрица алгебраических дополнений:")
for row in alg_mat:
    print(row)

#7
def inverse_matrix(A):
    n = len(A)
    det_A = det(A)
    if det_A == 0:
        raise ValueError("Матрица вырожденная, обратной матрицы не существует.")

    alg_mat = algmatrix(A)
    adjugate = [[alg_mat[j][i] for j in range(n)] for i in range(n)]
    inverse = [[adjugate[i][j] / det_A for j in range(n)] for i in range(n)]
    return inverse

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

inverse_A = inverse_matrix(A)
print("Обратная матрица:")
for row in inverse_A:
    print(row)


#8
def transpose_matrix(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def matrix_multiply(A, B):
    return [[sum(a * b for a, b in zip(row_A, col_B)) for col_B in zip(*B)] for row_A in A]

def more_penrose(H):
    H_T = transpose_matrix(H)
    H_T_H = matrix_multiply(H_T, H)
    H_T_H_inv = inverse_matrix(H_T_H)
    H_plus = matrix_multiply(H_T_H_inv, H_T)
    return H_plus

A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

A_plus = more_penrose(A)
print("Псевдообращение Мура-Пенроуза для матрицы A:")
for row in A_plus:
    print(row)