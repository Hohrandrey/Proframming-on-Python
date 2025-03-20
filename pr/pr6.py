#1
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
plot_sprite_map(sprite_map)