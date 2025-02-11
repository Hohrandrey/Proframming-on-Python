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
    task = 3
    #1 (Малевич)
    if task == 1:
        if x < 0.1 or x > 0.9 or y < 0.1 or y > 0.9:
            return 1, 1, 1  # Белый цвет для рамки
        else:
            return 0, 0, 0  # Черный цвет для внутренней части
    # 2 Градиент
    if task == 2:
        pass
    # 3 пакмен
    if task == 3:
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


# Создание окна и отображение изображения
label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()