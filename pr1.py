import tkinter as tk
import math

def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr

# Функция, возвращающая черный цвет для всех пикселей
def func(x, y):
    task = 2
    #1 (Малевич)
    if task == 1:
        if x < 0.1 or x > 0.9 or y < 0.1 or y > 0.9:
            return 1, 1, 1  # Белый цвет для рамки
        else:
            return 0, 0, 0  # Черный цвет для внутренней части
    # 2 Градиент
    elif task == 2:
        # Функция smoothstep выполняет плавный переход между двумя значениями edge0 и edge1
        def smoothstep(edge0, edge1, x):
            # Нормализуем x в диапазоне [0, 1] относительно edge0 и edge1
            t = max(0.0, min(1.0, (x - edge0) / (edge1 - edge0)))
            # Возвращаем значение, которое плавно изменяется от 0 до 1
            return t * t * (3.0 - 2.0 * t)

        # Радиусы для красного и зеленого кругов
        radius_red = 0.3
        radius_green = 0.3

        # Размер размытия для плавного перехода
        blur_size = 0.25

        # Вычисляем расстояние от точки (x, y) до центра красного круга
        distance_red = math.hypot(x - 0.52, y - 0.52)

        # Вычисляем расстояние от точки (x, y) до центра зеленого круга
        distance_green = math.hypot(x - 0.48, y - 0.48)

        # Вычисляем значение для красного цвета с учетом плавного перехода
        # Если расстояние меньше (radius_red - blur_size), то значение будет 1
        # Если расстояние больше radius_red, то значение будет 0
        # В промежутке значение плавно изменяется от 1 до 0
        t_red = 1.0 - smoothstep(radius_red - blur_size, radius_red, distance_red)

        # Аналогично вычисляем значение для зеленого цвета
        t_green = 1.0 - smoothstep(radius_green - blur_size, radius_green, distance_green)

        # Возвращаем значения для красного и зеленого цветов, а также 0 для синего
        return t_red, t_green, 0
    # 3 пакмен
    elif task == 3:
        # Центр желтого круга
        center_x, center_y = 0.5, 0.5
        # Радиус желтого круга
        radius = 0.3
        # Расстояние от текущего пикселя до центра желтого круга
        distance_yellow = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)

        # Центр черного круга (смещен вправо и вверх относительно центра желтого круга)
        black_center_x, black_center_y = center_x + 0.15, center_y - 0.15
        # Радиус черного круга
        black_radius = 0.07
        # Расстояние от текущего пикселя до центра черного круга
        distance_black = math.sqrt((x - black_center_x) ** 2 + (y - black_center_y) ** 2)

        # Если пиксель внутри черного круга, возвращаем черный цвет
        if distance_black <= black_radius:
            return 0, 0, 0  # Черный цвет
        # Если пиксель внутри желтого круга, возвращаем желтый цвет
        elif distance_yellow <= radius:
            return 1, 1, 0  # Желтый цвет

        else:
            return 0, 0, 0  # Черный цвет для фона
    elif task == 4:
        def noise(x, y):
            return (math.sin(x * 12.9898 + y * 78.233) * 43758.5453) % 1 #псевдослучайное значение в диапазоне от 0 до 1
        return noise(x, y), noise(x, y), noise(x, y)
    elif task == 5:
        def noise(x, y):
            return (math.sin(x * 12.9898 + y * 78.233) * 43758.5453) % 1 #псевдослучайное значение в диапазоне от 0 до 1

        def val_noise(x, y):
            # Определяем целочисленные координаты (округляем вниз)
            x0 = int(x)  # Ближайшая меньшая целая координата по x
            x1 = x0 + 1  # Следующая целая координата по x
            y0 = int(y)  # Ближайшая меньшая целая координата по y
            y1 = y0 + 1  # Следующая целая координата по y

            # Вычисляем дробные части координат (расстояние до x0 и y0)
            s = x - x0  # Дробная часть по x
            t = y - y0  # Дробная часть по y

            # Применяем smoothstep-функцию для сглаживания интерполяции
            s = s * s * (3.0 - 2.0 * s)  # Сглаживание по x
            t = t * t * (3.0 - 2.0 * t)  # Сглаживание по y

            # Вычисляем значения шума в четырех углах квадрата
            n00 = noise(x0, y0)  # Шум в (x0, y0)
            n01 = noise(x0, y1)  # Шум в (x0, y1)
            n10 = noise(x1, y0)  # Шум в (x1, y0)
            n11 = noise(x1, y1)  # Шум в (x1, y1)

            # Интерполяция по x (между x0 и x1)
            ix0 = n00 + (n10 - n00) * s  # Интерполяция между n00 и n10
            ix1 = n01 + (n11 - n01) * s  # Интерполяция между n01 и n11

            # Интерполяция по y (между y0 и y1)
            value = ix0 + (ix1 - ix0) * t  # Интерполяция между ix0 и ix1

            return value

        # Масштабируем координаты для получения более детализированного шума
        scale = 15.0
        # Вычисляем значение шума в точке (x * scale, y * scale)
        v = val_noise(x * scale, y * scale)
        # Возвращаем одно и то же значение три раза (например, для RGB-цвета)
        return v, v, v

    elif task == 6:
        def noise(x, y):
            return (math.sin(x * 12.9898 + y * 78.233) * 43758.5453) % 1 #псевдослучайное значение в диапазоне от 0 до 1

        def calculate_noise(coord_x, coord_y):
            # Преобразование координат в целые числа
            int_x = int(coord_x)
            int_y = int(coord_y)
            # Следующие целые координаты
            next_x = int_x + 1
            next_y = int_y + 1
            # Дробные части координат
            frac_x = coord_x - int_x
            frac_y = coord_y - int_y
            # Кубическая интерполяция для плавных переходов
            frac_x = frac_x * frac_x * (3.0 - 2.0 * frac_x)
            frac_y = frac_y * frac_y * (3.0 - 2.0 * frac_y)
            # Получение шумовых значений в углах ячейки
            noise_00 = noise(int_x, int_y)
            noise_01 = noise(int_x, next_y)
            noise_10 = noise(next_x, int_y)
            noise_11 = noise(next_x, next_y)
            # Линейная интерполяция вдоль оси X
            interp_x0 = noise_00 + (noise_10 - noise_00) * frac_x
            interp_x1 = noise_01 + (noise_11 - noise_01) * frac_x
            # Линейная интерполяция вдоль оси Y
            return interp_x0 + (interp_x1 - interp_x0) * frac_y

        # Параметры генерации шума
        num_octaves = 5  # Количество октав шума
        decay_rate = 0.5  # Коэффициент затухания амплитуды
        noise_scale = 5.0  # Масштабирование координат
        # Инициализация переменных
        noise_sum = 0.0  # Общая сумма шума
        current_amplitude = 1.0  # Начальная амплитуда
        current_frequency = 1.0  # Начальная частота
        max_amplitude = 0.0  # Максимальная возможная амплитуда
        # Цикл по октавам
        for _ in range(num_octaves):
            # Масштабирование координат для текущей октавы
            scaled_x = x * noise_scale * current_frequency
            scaled_y = y * noise_scale * current_frequency
            # Добавление шума с учетом амплитуды
            noise_sum += calculate_noise(scaled_x, scaled_y) * current_amplitude
            # Обновление максимальной амплитуды
            max_amplitude += current_amplitude
            # Уменьшение амплитуды и увеличение частоты для следующей октавы
            current_amplitude *= decay_rate
            current_frequency *= 2.0
            # Нормализация шума
        noise_sum /= max_amplitude
        # Применение квадратичной функции для плавных переходов
        noise_sum = noise_sum ** 2
        # Возвращение результата
        return noise_sum, noise_sum, 255

    else:
        print("Такого нет")


# Создание окна и отображение изображения
label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()