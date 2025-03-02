"""from itertools import groupby
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
"""

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
def task5_3():
    from ctypes import c_uint32

    def decrypt(v, k):
        v0, v1 = c_uint32(v[0]), c_uint32(v[1])
        delta = 0x9e3779b9
        k0, k1, k2, k3 = k[0], k[1], k[2], k[3]
        total = c_uint32(delta * 32)
        for i in range(32):
            v1.value -= ((v0.value << 4) + k2) ^ (v0.value + total.value) ^ ((v0.value >> 5) + k3)
            v0.value -= ((v1.value << 4) + k0) ^ (v1.value + total.value) ^ ((v1.value >> 5) + k1)
            total.value -= delta
        return v0.value, v1.value

    def hex_to_uint32(hex_str):
        return int(hex_str, 16)

    e_message = [
        "E3238557", "6204A1F8", "E6537611", "174E5747",
        "5D954DA8", "8C2DFE97", "2911CB4C", "2CB7C66B",
        "E7F185A0", "C7E3FA40", "42419867", "374044DF",
        "2519F07D", "5A0C24D4", "F4A960C5", "31159418",
        "F2768EC7", "AEAF14CF", "071B2C95", "C9F22699",
        "FFB06F41", "2AC90051", "A53F035D", "830601A7",
        "EB475702", "183BAA6F", "12626744", "9B75A72F",
        "8DBFBFEC", "73C1A46E", "FFB06F41", "2AC90051",
        "97C5E4E9", "B1C26A21", "DD4A3463", "6B71162F",
        "8C075668", "7975D565", "6D95A700", "7272E637"
    ]
    key = [0, 4, 5, 1]
    e_data = [hex_to_uint32(i) for i in e_message]
    d_data = []
    for i in range(0, len(e_data), 2):
        e_block = [e_data[i], e_data[i + 1]]
        d_block = decrypt(e_block, key)
        d_data.append(d_block)
    for v0, v1 in d_data:
        print(f"{chr(v0)}{chr(v1)}", end='')

task5_3()

#7.1
def task7_1():
    rooms = {
        'room1': {
            'name': 'Комната №1',
            'description': 'Вы в начале лабиринта. Сможете ли из него выбраться?',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы углубляетесь в недры лабиринта...',
                    'next_label': 'room2'
                }
            ]
        },
        'room2': {
            'name': 'Комната №2',
            'description': 'Квадратная комната с красными стенами.',
            'actions': [
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте в светлый проход...',
                    'next_label': 'room3'
                },
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы поднимаетесь к светлой стартовой комнате...',
                    'next_label': 'room1'
                },
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы идёте в тёмный проход...',
                    'next_label': 'room4'
                }
            ]
        },
        'room3': {
            'name': 'Комната №3',
            'description': 'Круглая комната с синими стенами.',
            'actions': [
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы идёте по коридору, придающему уверенности в выборе...',
                    'next_label': 'room5'
                },
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы идёте в комнату цвета мака...',
                    'next_label': 'room2'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы поднимаетесь по очень длинной лестнице...',
                    'next_label': 'room6'
                }
            ]
        },
        'room4': {
            'name': 'Комната №4',
            'description': 'Квадратная комната с белыми стенами.',
            'actions': [
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы поднимаетесь по не очень длинной лестнице...',
                    'next_label': 'room7'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте по тёмному проходу...',
                    'next_label': 'room2'
                }
            ]
        },
        'room5': {
            'name': 'Комната №5',
            'description': 'Тупиковая комната',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы с грустью на душе возвращаетесь обратно',
                    'next_label': 'room3'
                }
            ]
        },
        'room6': {
            'name': 'Комната №6',
            'description': 'Комната с лифтом и числом "-5" на стене.',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы поднимаетесь вверх с помощью лифта...',
                    'next_label': 'room8'
                },
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы спускаетесь по очень длинной лестнице...',
                    'next_label': 'room3'
                }
            ]
        },
        'room7': {
            'name': 'Комната №7',
            'description': 'Круглая комната с красным полом и рисунком в виде белого кирпича',
            'actions': [
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы спускаетесь по не очень длинной лестнице...',
                    'next_label': 'room4'
                }
            ]
        },
        'room8': {
            'name': 'Комната №8',
            'description': 'Комната с лифтом и числом "1" на стене.',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы идёте в тёмную комнату...',
                    'next_label': 'room9'
                },
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы спускаетесь вниз с помощью лифта...',
                    'next_label': 'room6'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте в светлую комнату...',
                    'next_label': 'room10'
                }
            ]
        },
        'room9': {
            'name': 'Комната №9',
            'description': 'Тёмная комната.',
            'actions': [
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы идёте в комнату с лифтом...',
                    'next_label': 'room8'
                },
                {
                    'text': 'Идти на юго-запад.',
                    'message': 'Вы идёте в светлую комнату',
                    'next_label': 'room10'
                }
            ]
        },
        'room10': {
            'name': 'Комната №10',
            'description': 'Светлая комната с двумя выходами.',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы возвращаетесь в тёмную комнату...',
                    'next_label': 'room9'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте в новую комнату...',
                    'next_label': 'room11'
                }
            ]
        },
        'room11': {
            'name': 'Комната №11',
            'description': 'Комната с загадочными символами на стенах.',
            'actions': [
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы возвращаетесь в светлую комнату...',
                    'next_label': 'room10'
                },
                {
                    'text': 'Идти на север.',
                    'message': 'Вы идёте в последнюю комнату...',
                    'next_label': 'room12'
                }
            ]
        },
        'room12': {
            'name': 'Выход',
            'description': 'Вы нашли выход! Поздравляем!',
            'actions': []
        }
    }

    def play_game():
        current_label = 'room1'
        while True:
            current_room = rooms.get(current_label)
            if not current_room:
                print("Ошибка: комната не найдена.")
                break

            print("\n" + current_room['name'])
            print(current_room['description'])

            actions = current_room.get('actions', [])
            if not actions:
                print("\nКонец игры.")
                break

            for index, action in enumerate(actions, 1):
                print(f"{index}. {action['text']}")

            while True:
                choice = input("> ")
                try:
                    choice_index = int(choice) - 1
                    if 0 <= choice_index < len(actions):
                        selected_action = actions[choice_index]
                        break
                    else:
                        print("Неверный выбор. Попробуйте снова.")
                except ValueError:
                    print("Пожалуйста, введите номер.")

            if selected_action['message']:
                print(selected_action['message'])

            current_label = selected_action['next_label']

    play_game()

"""task7_1()"""

#7.2
"""
digraph G {
    rankdir="LR"; // Ориентация графа слева направо
    node [shape=box, style=rounded]; // Стиль узлов

    // Комнаты
    room1 [label="Комната №1\nВы в начале лабиринта. Сможете ли из него выбраться?"];
    room2 [label="Комната №2\nКвадратная комната с красными стенами."];
    room3 [label="Комната №3\nКруглая комната с синими стенами."];
    room4 [label="Комната №4\nКвадратная комната с белыми стенами."];
    room5 [label="Комната №5\nТупиковая комната"];
    room6 [label="Комната №6\nКомната с лифтом и числом \"-5\" на стене."];
    room7 [label="Комната №7\nКруглая комната с красным полом и рисунком в виде белого кирпича"];
    room8 [label="Комната №8\nКомната с лифтом и числом \"1\" на стене."];
    room9 [label="Комната №9\nТёмная комната."];
    room10 [label="Комната №10\nСветлая комната с двумя выходами."];
    room11 [label="Комната №11\nКомната с загадочными символами на стенах."];
    room12 [label="Комната №12\nВыход\nВы нашли выход! Поздравляем!"];

    // Связи между комнатами
    room1 -> room2 [label="Идти на север"];
    room2 -> room1 [label="Идти на юг"];
    room2 -> room3 [label="Идти на запад"];
    room2 -> room4 [label="Идти на восток"];
    room3 -> room2 [label="Идти на восток"];
    room3 -> room5 [label="Идти на юг"];
    room3 -> room6 [label="Идти на запад"];
    room4 -> room2 [label="Идти на запад"];
    room4 -> room7 [label="Идти на восток"];
    room5 -> room3 [label="Идти на север"];
    room6 -> room3 [label="Идти на восток"];
    room6 -> room8 [label="Идти на север"];
    room7 -> room4 [label="Идти на запад"];
    room8 -> room6 [label="Идти на юг"];
    room8 -> room9 [label="Идти на север"];
    room8 -> room10 [label="Идти на запад"];
    room9 -> room8 [label="Идти на юг"];
    room9 -> room10 [label="Идти на юго-запад"];
    room10 -> room9 [label="Идти на север"];
    room10 -> room11 [label="Идти на запад"];
    room11 -> room10 [label="Идти на восток"];
    room11 -> room12 [label="Идти на север"];
}
"""
#7.3

def task7_3():
    rooms = {
        'room1': {
            'name': 'Комната №1',
            'description': 'Вы в начале лабиринта. Сможете ли из него выбраться?',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы углубляетесь в недры лабиринта...',
                    'next_label': 'room2'
                }
            ]
        },
        'room2': {
            'name': 'Комната №2',
            'description': 'Квадратная комната с красными стенами.',
            'actions': [
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте в светлый проход...',
                    'next_label': 'room3'
                },
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы поднимаетесь к светлой стартовой комнате...',
                    'next_label': 'room1'
                },
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы идёте в тёмный проход...',
                    'next_label': 'room4'
                }
            ]
        },
        'room3': {
            'name': 'Комната №3',
            'description': 'Круглая комната с синими стенами.',
            'actions': [
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы идёте по коридору, придающему уверенности в выборе...',
                    'next_label': 'room5'
                },
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы идёте в комнату цвета мака...',
                    'next_label': 'room2'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы поднимаетесь по очень длинной лестнице...',
                    'next_label': 'room6'
                }
            ]
        },
        'room4': {
            'name': 'Комната №4',
            'description': 'Квадратная комната с белыми стенами.',
            'actions': [
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы поднимаетесь по не очень длинной лестнице...',
                    'next_label': 'room7'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте по тёмному проходу...',
                    'next_label': 'room2'
                }
            ]
        },
        'room5': {
            'name': 'Комната №5',
            'description': 'Тупиковая комната',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы с грустью на душе возвращаетесь обратно',
                    'next_label': 'room3'
                }
            ]
        },
        'room6': {
            'name': 'Комната №6',
            'description': 'Комната с лифтом и числом "-5" на стене.',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы поднимаетесь вверх с помощью лифта...',
                    'next_label': 'room8'
                },
                {
                    'text': 'Идти на восток.',
                    'message': 'Вы спускаетесь по очень длинной лестнице...',
                    'next_label': 'room3'
                }
            ]
        },
        'room7': {
            'name': 'Комната №7',
            'description': 'Круглая комната с красным полом и рисунком в виде белого кирпича',
            'actions': [
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы спускаетесь по не очень длинной лестнице...',
                    'next_label': 'room4'
                }
            ]
        },
        'room8': {
            'name': 'Комната №8',
            'description': 'Комната с лифтом и числом "1" на стене.',
            'actions': [
                {
                    'text': 'Идти на север.',
                    'message': 'Вы идёте в тёмную комнату...',
                    'next_label': 'room9'
                },
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы спускаетесь вниз с помощью лифта...',
                    'next_label': 'room6'
                },
                {
                    'text': 'Идти на запад.',
                    'message': 'Вы идёте в светлую комнату...',
                    'next_label': 'room10'
                }
            ]
        },
        'room9': {
            'name': 'Комната №9',
            'description': 'Тёмная комната.',
            'actions': [
                {
                    'text': 'Идти на юг.',
                    'message': 'Вы идёте в комнату с лифтом...',
                    'next_label': 'room8'
                },
                {
                    'text': 'Идти на юго-запад.',
                    'message': 'Вы идёте в светлую комнату',
                    'next_label': 'room10'
                }
            ]
        },
        'room10': {
            'name': 'Выход',
            'description': 'Вы нашли выход! Поздравляем!',
            'actions': []
        }
    }

    from collections import deque, defaultdict

    def find_dead_ends(rooms):
        """
        Находит тупиковые комнаты в игровом мире.
        :param rooms: Словарь комнат.
        :return: Список тупиковых комнат.
        """
        # Построение обратного графа
        reverse_graph = defaultdict(list)
        for room_label, room_info in rooms.items():
            for action in room_info['actions']:
                next_label = action['next_label']
                reverse_graph[next_label].append(room_label)

        # Поиск всех комнат, из которых можно добраться до выхода
        visited = set()
        queue = deque()
        start_label = 'room10'  # Выходная комната
        if start_label in rooms:
            visited.add(start_label)
            queue.append(start_label)

        while queue:
            current_label = queue.popleft()
            for neighbor in reverse_graph.get(current_label, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        # Находим комнаты, которые недостижимы из выхода
        all_rooms = set(rooms.keys())
        unreachable = all_rooms - visited

        # Находим комнаты с одним выходом (тупики)
        single_exit = [label for label in rooms if len(rooms[label]['actions']) == 1]

        # Объединяем недостижимые комнаты и комнаты с одним выходом
        dead_ends = unreachable.union(set(single_exit))

        # Убираем входную комнату из списка тупиков
        dead_ends.discard('room1')

        return sorted(dead_ends)

    # Находим тупиковые комнаты
    dead_ends = find_dead_ends(rooms)
    print("\nНайдены тупиковые комнаты:", dead_ends)

# Запуск функции
task7_3()