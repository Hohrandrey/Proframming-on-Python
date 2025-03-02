from itertools import groupby
s = ["3", '1', '2', '3', "4567"]

#3.1
print([int(i) for i in s])
#3.2
print([len(set(s))])
#3.3
print([s[::-1]])
#3.4
x = "3"
print([i for i, val in enumerate(s) if val == x])
#3.5
print(sum([int(s[i]) for i in range(0, len(s), 2)]))
#3.6
print(max(s, key=len))
#3.7
n = 110
print(n % sum(map(int, str(n))) == 0)
#3.8
x = 'ABBCCCDEF'
print([(k, len(list(g))) for k, g in groupby(x)])


#4.1
A = [[0, 2], [3, 0]]
B = [[1, 4], [2, 0]]
def multiply(A, B):
    C = []
    for j in range(len(A)):
        new = []
        for i in range(len(A[j])):
            new.append(A[j][i]*B[j][i])
        C.append(new)
    return C

print(multiply(A, B))
#4.2
A = [[0, 2, 1], [1, 0, 3], [0, 1, 1]]
def transpose(A):
    res = []
    for j in range(len(A)):
        new = []
        for i in range(len(A[j])):
            new.append(A[i][j])
        res.append(new)
    return res

print(transpose(A))

#4.3
A = [[1, 2], [3, 4], [5, 6]]
B = [[1, 2, 3], [4, 5, 6]]
def dot(A, B):
    result = []
    for i in range(len(A)):
        new = []
        for j in range(len(B[0])):
            summ =0
            for k in range(len(B)):
                summ += A[i][k] * B[k][j]
            new.append(summ)
        result.append(new)
    return result
print(dot(A, B))


#5.1
def task5_1():
    def generate_groups():
        array = []
        groups = ["ИВБО", "ИКБО", "ИМБО", "ИНБО"]
        for group in groups:
            if group == "ИВБО":
                append = []
                numbers = [10, 11, 12, 13, 20, 21, 22]
                for number in numbers:
                    append.append(group + '-' + str(number) + "-23")
                array.append((group, append))

            elif group == "ИКБО":
                append = []
                numbers = [10, 10, 11, 12, 13, 14, 15, 20, 21, 22, 24,
                           34, 40, 41, 42, 43, 50, 51, 52, 60, 61, 62,
                           63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76]
                flag = 1
                for number in numbers:
                    if number == 10 and flag == 1 or number == 24 or number == 34:
                        append.append(group + '-' + str(number) + "-22")
                        flag = 0
                    else:
                        append.append(group + '-' + str(number) + "-23")
                array.append((group, append))

            elif group == "ИМБО":
                append = []
                numbers = [10, 11]
                for number in numbers:
                    append.append(group + '-' + str(number) + "-23")
                array.append((group, append))

            elif group == "ИНБО":
                append = []
                numbers = [10, 11, 12, 13, 20, 21, 22, 23, 30, 31, 32, 33]
                for number in numbers:
                    append.append(group + '-' + str(number) + "-23")
                array.append((group, append))

        return array

    list_of_groups = generate_groups()

    for group_name, groups in list_of_groups:
        print(group_name)  # Вывод названия раздела
        for i in range(0, len(groups), 9):  # Разбиваем на строки по 9 групп
            print(" ".join(groups[i:i + 9]))  # Вывод групп в строку
        print()  # Пустая строка между разделами

task5_1()
#5.2
import sys

def my_print(*args, sep=' ', end='\n', file=sys.stdout):
    out = sep.join(map(str, args))
    out += end
    file.write(out)

# Пример использования
my_print("Hello,", "world!", sep=" ", end="!\n")
my_print("This is a custom print function.")
my_print("This", "is", "a", "custom", "print", "function.", sep=" ", end="\n")

file = open("123yt64ryfheiuowsuy.txt", 'w')
my_print(123, file=file)
file.close()

#5.3
def hex_to_char(hex_value):
    return chr(hex_value)  # Прямое преобразование без int()

def main():
    hex_pairs = [
        (0x41f, 0x43e),
        (0x437, 0x434),
        (0x440, 0x430),
        (0x432, 0x43b),
        (0x44f, 0x44e),
        (0x21, 0x20),
        (0x412, 0x44b),
        (0x20, 0x43d),
        (0x430, 0x448),
        (0x43b, 0x438),
        (0x20, 0x441),
        (0x435, 0x43a),
        (0x440, 0x435),
        (0x442, 0x43d),
        (0x43e, 0x435),
        (0x20, 0x441),
        (0x43e, 0x43e),
        (0x431, 0x449),
        (0x435, 0x43d),
        (0x438, 0x435)
    ]

    # Конвертация в текст
    result = ""
    for pair in hex_pairs:
        for hex_value in pair:
            result += hex_to_char(hex_value)

    print(result)

if __name__ == "__main__":
    main()