import matplotlib.pyplot as plt


#Задание 1
def main1(n, m, a):
    result = 1
    for c in range(1, a + 1):
        for j in range(1, m + 1):
            sum_term = 0
            for i in range(1, n + 1):
                term = ((28 * c**2)**6) / 5 + 16 * ((j**3 / 44) + i**2)**5
                sum_term += term
            result *= sum_term
    return result


if __name__ == "__main__":
    print(main1(4, 2, 8))

#Задание 2
def z2(y, z):
    l = len(y)
    summ = 0
    for i in range(1, l+1):
        summ += (y[i-1]-z[i-1])**2
    return summ**0.5

y1 = [1, 0.5, 1]
z1 = [0.5, 2, 1]

print(z2(y1, z1))

#Задание 3
def z3(y, z):
    l = len(y)
    summ = 0
    for i in range(1, l+1):
        summ += abs(y[i-1]-z[i-1])
    return summ

y3 = [1, 0.5, 1]
x3 = [0.5, 2, 1]

print(z3(y3, x3))

#Задание 4
def z4(y, z):
    l = len(y)
    max = -10
    for i in range(1, l + 1):
        if max < abs(y[i - 1] - z[i - 1]):
            max = abs(y[i - 1] - z[i - 1])
    return max
y4 = [1, 0.5, 1]
x4 = [0.5, 2, 1]

print(z4(y4, x4))

#Задание 5

def z5(y, z):
    l = len(y)
    summ =0
    for i in range(1, l + 1):
        summ += (y[i - 1] - z[i - 1])**2
    return summ
y5 = [1, 0.5, 1]
x5 = [0.5, 2, 1]

print(z5(y5, x5))

#Задание 6

def z6(y, z, h6):
    l = len(y)
    summ =0
    for i in range(1, l + 1):
        summ += abs(y[i - 1] - z[i - 1])**h6
    return summ**(1/h6)
y6 = [1, 0.5, 1]
x6 = [0.5, 2, 1]

h6 = 5

print(z6(y6, x6, h6))

#Задание 7


def visualize(distance_metrics, y, z, move=1.0):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = plt.subplots()
    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 1}' for i in x])
    plt.show()


list = (z2, z3, z4, z5, z6)
visualize(list, y6, z6, 1.5)

#Задание 8

words = ["language!", "programming", "Python", "the", "love", "I"]
strin = ''
count = 0
for i in range(len(words) - 1, -1, -1):
    if count == 0:
        strin += words[i]
        count+=1
    else:
        strin += ' ' + words[i]
print(strin)

#Задание 9

def count_characters(input_string):
    # Приводим строку к нижнему регистру и удаляем пробелы
    cleaned_string = input_string.lower().replace(" ", "")

    # Создаём словарь для хранения результатов
    char_count = {}

    # Подсчитываем количество вхождений каждого символа
    for char in cleaned_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


# Пример использования
input_string = strin
result = count_characters(input_string)
print(result)

#Задание 10

#Задание 11