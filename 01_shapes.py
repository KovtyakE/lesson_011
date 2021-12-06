# -*- coding: utf-8 -*-

import simple_draw as sd
sd.set_screen_size(1200, 600)

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_polygon(point, angle=0):
        length = 400 / n
        every_angle = 360 / n
        start_point = point
        for iteration in range(n):
            line = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
            line.draw()
            start_point = line.end_point
            angle += every_angle
            # sd.sleep(0.1)
    return draw_polygon


draw_triangle = get_polygon(n=4)
draw_triangle(point=sd.get_point(600, 100), angle=15)
sd.pause()
