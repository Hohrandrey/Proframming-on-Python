import sys

def task_1_1():
    print("Задание 1.1")
    print(42, 42 == 42)
    print(0b101010, 0b101010 == 42)
    print(0o52, 0o52 == 42)
    print(0x2A, 0x2A == 42)
    print(0x2a, 0x2a == 42)
    print(42.0, 42.0 == 42)
    print([42][0], [42][0] == 42)
    print(420e-1, 420e-1 == 42)
    print({'key': 42}['key'], {'key': 42}['key'] == 42)
    print(4_2, 4_2 == 42)

def task_1_2():
    print("Задание 1.2")
    max_float = sys.float_info.max
    print(max_float)

def task_1_3():
    print("Задание 1.3")
    result = divmod(7, 3)
    print(result)  # Выведет (2, 1), где 2 — это частное, а 1 — остаток

def task_1_4():
    print("Задание 1.4")
    a = 10
    while a != 0:
        a -= 0.1 # исправление - a = 100 и a -= 1 (по сути домножить на 10)
        # 0.1 - не точное число для ПК, вычитается приблизительное число и ошибки округления суммируются

def task_1_5():
    print("Задание 1.5")
    z = 1
    z <<= 40 # == 2^40
    print(2 ** z) # 2^(2^40)

def task_1_6():
    print("Задание 1.6")
    i = 0
    while i < 10:
        print(i)
        i+=1 # заменили ++i на i+=1


def task_1_7():
    print("Задание 1.7")
    print((True * 2 + False) * -True) #True можно интерпретировать как 1

def task_1_8():
    print("Задание 1.8")
    x = 5
    print(1 < x < 10) #(1 < x) and (x < 10)

    x = 5
    print(1 < (x < 10)) # 1 < True(True можно интерпретировать как 1)


#task_1_1()
#task_1_2()
#task_1_3()
#task_1_4()
#task_1_5()
#task_1_6()
#task_1_7()
#task_1_8()