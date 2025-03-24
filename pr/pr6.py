"""#1
import numpy as np
import matplotlib.pyplot as plt

def generate_symmetric_sprite(size=5):
    sprite = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range((size + 1) // 2):
            sprite[i, j] = np.random.randint(0, 2)
    for i in range(size):
        for j in range((size + 1) // 2, size):
            sprite[i, j] = sprite[i, size - 1 - j]
    return sprite

def plot_sprite(sprite):
    plt.imshow(sprite, cmap='gray')
    plt.axis('off')
    plt.show()

sprite = generate_symmetric_sprite()
plot_sprite(sprite)

#2

import numpy as np
import matplotlib.pyplot as plt

def generate_symmetric_sprite(size=5):
    sprite = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range((size + 1) // 2):
            sprite[i, j] = np.random.randint(0, 2)
    for i in range(size):
        for j in range((size + 1) // 2, size):
            sprite[i, j] = sprite[i, size - 1 - j]
    return sprite

def generate_sprite_map(rows, cols, sprite_size=5, padding=1, side_padding=2, top_bottom_padding=2):
    map_height = rows * sprite_size + (rows - 1) * padding + 2 * top_bottom_padding
    map_width = cols * sprite_size + (cols - 1) * padding + 2 * side_padding
    sprite_map = np.zeros((map_height, map_width), dtype=int)
    for i in range(rows):
        for j in range(cols):
            sprite = generate_symmetric_sprite(sprite_size)
            y_start = top_bottom_padding + i * (sprite_size + padding)
            y_end = y_start + sprite_size
            x_start = side_padding + j * (sprite_size + padding)
            x_end = x_start + sprite_size
            sprite_map[y_start:y_end, x_start:x_end] = sprite
    return sprite_map

def plot_sprite_map(sprite_map):
    plt.imshow(sprite_map, cmap='gray')
    plt.axis('off')
    plt.show()

rows = 10
cols = 20
sprite_size = 5
padding = 1
side_padding = 2
top_bottom_padding = 2

sprite_map = generate_sprite_map(rows, cols, sprite_size, padding, side_padding, top_bottom_padding)
plot_sprite_map(sprite_map)


#3
import numpy as np
import matplotlib.pyplot as plt

PICO_8_PALETTE = [
    (29, 43, 83), (126, 37, 83), (0, 135, 81), (171, 82, 54),
    (95, 87, 79), (194, 195, 199), (255, 241, 232), (255, 0, 77),
    (255, 163, 0), (255, 236, 39), (0, 228, 54), (41, 173, 255),
    (131, 118, 156), (255, 119, 168), (255, 204, 170), (0, 0, 0)
]

def generate_symmetric_sprite(n, m):
    sprite = np.zeros((n, m, 3), dtype=int)
    color_indices = np.random.choice(len(PICO_8_PALETTE) - 1, 2, replace=False)
    color1 = PICO_8_PALETTE[color_indices[0]]
    color2 = PICO_8_PALETTE[color_indices[1]]
    black_color = PICO_8_PALETTE[-1]
    for i in range(n):
        for j in range((m + 1) // 2):
            random_value = np.random.randint(0, 3)
            if random_value == 0:
                sprite[i, j] = color1
            elif random_value == 1:
                sprite[i, j] = color2
            else:
                sprite[i, j] = black_color
    for i in range(n):
        for j in range((m + 1) // 2, m):
            sprite[i, j] = sprite[i, m - 1 - j]
    return sprite

def generate_sprite_map(rows, cols, n, m, padding=1, side_padding=2, top_bottom_padding=2):
    map_height = rows * n + (rows - 1) * padding + 2 * top_bottom_padding
    map_width = cols * m + (cols - 1) * padding + 2 * side_padding
    sprite_map = np.zeros((map_height, map_width, 3), dtype=int)
    for i in range(rows):
        for j in range(cols):
            sprite = generate_symmetric_sprite(n, m)
            y_start = top_bottom_padding + i * (n + padding)
            y_end = y_start + n
            x_start = side_padding + j * (m + padding)
            x_end = x_start + m
            sprite_map[y_start:y_end, x_start:x_end] = sprite
    return sprite_map

def plot_sprite_map(sprite_map):
    plt.imshow(sprite_map)
    plt.axis('off')
    plt.show()

try:
    n = int(input("Введите высоту спрайта (n): "))
    m = int(input("Введите ширину спрайта (m): "))
    if n <= 0 or m <= 0:
        raise ValueError("Размеры спрайта должны быть положительными числами.")
except ValueError as e:
    print(f"Ошибка ввода: {e}")
    exit()

rows = 10
cols = 20
padding = 1
side_padding = 2
top_bottom_padding = 2

sprite_map = generate_sprite_map(rows, cols, n, m, padding, side_padding, top_bottom_padding)
plot_sprite_map(sprite_map)"""

"""
#2.5

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def generate_attraction_points(n, width, height):
    return np.random.rand(n, 2) * [width, height]

def absorb_points(nodes, points, dk):
    to_remove = []
    for i, point in enumerate(points):
        if np.min(np.linalg.norm(nodes - point, axis=1)) < dk:
            to_remove.append(i)
    return np.delete(points, to_remove, axis=0)

def find_influence_sets(nodes, points, di):
    influence_sets = {i: [] for i in range(len(nodes))}
    for point in points:
        distances = np.linalg.norm(nodes - point, axis=1)
        closest_idx = np.argmin(distances)
        if distances[closest_idx] <= di:
            influence_sets[closest_idx].append(point)
    return influence_sets

def grow_tree(attraction_points, initial_node, dk, di, D, steps):
    nodes = np.array([initial_node])
    segments = []
    points = np.copy(attraction_points)

    for _ in range(steps):
        # Шаг 2: Поглощение точек
        points = absorb_points(nodes, points, dk)
        if len(points) == 0:
            break

        # Шаг 3: Поиск множеств влияния
        influence_sets = find_influence_sets(nodes, points, di)

        # Шаг 4: Рост новых узлов
        new_nodes = []
        for idx, S_v in influence_sets.items():
            if S_v:
                vectors = [(s - nodes[idx])/np.linalg.norm(s - nodes[idx]) for s in S_v]
                n_vec = np.sum(vectors, axis=0)
                if np.linalg.norm(n_vec) > 1e-6:
                    n_hat = n_vec / np.linalg.norm(n_vec)
                    new_node = nodes[idx] + n_hat * D
                    new_nodes.append(new_node)
                    segments.append([nodes[idx], new_node])

        if new_nodes:
            nodes = np.vstack([nodes, new_nodes])
        else:
            break

    return nodes, segments

def plot_trees(trees):
    fig, ax = plt.subplots(figsize=(10, 6))
    for tree in trees:
        segments = tree['segments']
        lc = LineCollection(segments, colors='green', linewidths=1)
        ax.add_collection(lc)
    ax.autoscale()
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

def generate_initial_positions(num_trees, width, height, min_distance):
    positions = []
    zone_width = width / num_trees
    for i in range(num_trees):
        x = i * zone_width + zone_width / 2
        y = np.random.uniform(0, height / 4)
        positions.append([x, y])
    return positions

# Параметры
width, height = 400, 250
n_points = 500
num_trees = 1  # Количество деревьев
min_distance = 20  # Минимальное расстояние между деревьями
dk = 5
di = 40
D = 10
steps = 100

# Начальные позиции с учетом минимального расстояния
initial_positions = generate_initial_positions(num_trees, width, height, min_distance)

# Генерация
trees = []
for i in range(num_trees):
    # Определяем зону для каждого дерева
    zone_width = width / num_trees
    left = i * zone_width
    right = (i + 1) * zone_width
    zone_points = generate_attraction_points(n_points // num_trees, zone_width - min_distance, height)
    zone_points[:, 0] += left + min_distance / 2  # Сдвигаем точки в свою зону

    # Генерация дерева
    nodes, segments = grow_tree(zone_points, initial_positions[i], dk, di, D, steps)
    trees.append({'nodes': nodes, 'segments': segments})

# Визуализация
plot_trees(trees)
"""

#2.6
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Circle


def generate_attraction_points(n, width, height, min_y):
    """Генерация точек притяжения выше min_y"""
    points = np.random.rand(n, 2) * [width, height - min_y]  # Генерация точек выше min_y
    points[:, 1] += min_y  # Сдвигаем точки вверх
    return points


def absorb_points(nodes, points, dk):
    """Удалить точки, находящиеся ближе dk к любому узлу дерева"""
    to_remove = []
    for i, point in enumerate(points):
        if np.min(np.linalg.norm(nodes - point, axis=1)) < dk:
            to_remove.append(i)
    return np.delete(points, to_remove, axis=0)


def find_influence_sets(nodes, points, di):
    """Найти множества S(v) для узлов конкретного дерева"""
    influence_sets = {i: [] for i in range(len(nodes))}
    for point in points:
        distances = np.linalg.norm(nodes - point, axis=1)
        closest_idx = np.argmin(distances)
        if distances[closest_idx] <= di:
            influence_sets[closest_idx].append(point)
    return influence_sets


def grow_tree(attraction_points, initial_node, dk, di, D, steps, trunk_length):
    # Преобразуем initial_node в массив NumPy
    initial_node = np.array(initial_node, dtype=float)

    # Создаем ствол
    trunk_end = initial_node + np.array([0, trunk_length])  # Вершина ствола
    nodes = np.array([initial_node, trunk_end])  # Начальные узлы: основание и вершина ствола
    segments = [[initial_node, trunk_end]]  # Сегмент ствола
    points = np.copy(attraction_points)

    for _ in range(steps):
        # Шаг 2: Поглощение точек
        points = absorb_points(nodes, points, dk)
        if len(points) == 0:
            break

        # Шаг 3: Поиск множеств влияния
        influence_sets = find_influence_sets(nodes, points, di)

        # Шаг 4: Рост новых узлов
        new_nodes = []
        for idx, S_v in influence_sets.items():
            if S_v:
                vectors = [(s - nodes[idx]) / np.linalg.norm(s - nodes[idx]) for s in S_v]
                n_vec = np.sum(vectors, axis=0)
                if np.linalg.norm(n_vec) > 1e-6:
                    n_hat = n_vec / np.linalg.norm(n_vec)
                    new_node = nodes[idx] + n_hat * D
                    new_nodes.append(new_node)
                    segments.append([nodes[idx], new_node])

        if new_nodes:
            nodes = np.vstack([nodes, new_nodes])
        else:
            break

    return nodes, segments


def add_leaves(ax, segments, leaf_radius, leaf_probability, max_leaves_per_segment, min_distance_between_leaves):
    """Добавляет листья на ветки дерева"""
    leaves = []  # Список для хранения позиций листьев
    for segment in segments:
        # Добавляем листья только с вероятностью leaf_probability
        if np.random.rand() < leaf_probability:
            # Количество листьев на текущем сегменте
            num_leaves = np.random.randint(1, max_leaves_per_segment + 1)
            for _ in range(num_leaves):
                t = np.random.uniform(0, 1)  # Случайная позиция вдоль сегмента
                x = segment[0][0] + t * (segment[1][0] - segment[0][0])
                y = segment[0][1] + t * (segment[1][1] - segment[0][1])
                # Проверяем расстояние до других листьев
                if all(np.linalg.norm(np.array([x, y]) - np.array(leaf)) >= min_distance_between_leaves for leaf in
                       leaves):
                    leaves.append((x, y))
                    # Добавление круга (листа)
                    leaf_circle = Circle((x, y), leaf_radius, color='green', alpha=0.5)  # Полупрозрачный зеленый круг
                    ax.add_patch(leaf_circle)


def plot_trees(trees, leaf_radius=4, leaf_probability=0.3, max_leaves_per_segment=3, min_distance_between_leaves=10):
    fig, ax = plt.subplots(figsize=(10, 6))
    for tree in trees:
        segments = tree['segments']
        lc = LineCollection(segments, colors='brown', linewidths=2)  # Коричневые ветки
        ax.add_collection(lc)
        # Добавляем листья
        add_leaves(ax, segments, leaf_radius, leaf_probability, max_leaves_per_segment, min_distance_between_leaves)
    ax.autoscale()
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()


def generate_initial_positions(num_trees, width, height, min_distance, trunk_base_y):
    positions = []
    zone_width = width / num_trees
    for i in range(num_trees):
        x = i * zone_width + zone_width / 2
        y = trunk_base_y  # Основание ствола на высоте trunk_base_y
        positions.append([x, y])
    return positions


# Параметры
width, height = 400, 250
n_points = 500
num_trees = 3  # Количество деревьев
min_distance = 50  # Минимальное расстояние между деревьями
dk = 5
di = 40
D = 10
steps = 100
trunk_length = 45  # Длина ствола
trunk_base_y = 35  # Высота основания ствола
leaf_radius = 7  # Радиус листьев (увеличен в 2 раза)
leaf_probability = 0.4  # Вероятность появления листьев на сегменте
max_leaves_per_segment = 3  # Максимальное количество листьев на сегмент
min_distance_between_leaves = 20  # Минимальное расстояние между листьями

# Начальные позиции с учетом минимального расстояния
initial_positions = generate_initial_positions(num_trees, width, height, min_distance, trunk_base_y)

# Генерация
trees = []
for i in range(num_trees):
    # Определяем зону для каждого дерева
    zone_width = width / num_trees
    left = i * zone_width
    right = (i + 1) * zone_width
    zone_points = generate_attraction_points(n_points // num_trees, zone_width - min_distance, height,
                                             trunk_base_y + trunk_length)
    zone_points[:, 0] += left + min_distance / 2  # Сдвигаем точки в свою зону

    # Генерация дерева
    nodes, segments = grow_tree(zone_points, initial_positions[i], dk, di, D, steps, trunk_length)
    trees.append({'nodes': nodes, 'segments': segments})

# Визуализация
plot_trees(trees, leaf_radius, leaf_probability, max_leaves_per_segment, min_distance_between_leaves)
