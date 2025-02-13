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
    task = 4
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
            return (math.sin(x * 12.9898 + y * 78.233) * 43758.5453) % 1
        return noise(x, y), noise(x, y), noise(x, y)
    elif task == 5:
        pass
    else:
        pass


# Создание окна и отображение изображения
label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()