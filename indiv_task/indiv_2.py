#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Создать абстрактный базовый класс Triangle для представления треугольника с
виртуальными функциями вычисления площади и периметра.
Поля данных должны включать две стороны и угол между ними.
Определить классы-наследники: прямоугольный треугольник,
равнобедренный треугольник, равносторонний треугольник со своими
функциями вычисления площади и периметра.

Вызывающая программа должна продемонстрировать все варианты вызова
переопределенных абстрактных методов. Написать функцию вывода, получающую
параметры базового класса по ссылке и демонстрирующую виртуальный вызов.
"""


from math import pi, sqrt, cos, sin
from abc import ABC, abstractmethod


# Базовый абстрактный класс "Треугольник"
class Triangle(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    # Функция вывода
    def print_info(self):
        print(f"Площадь треугольника = {self.square()}")
        print(f"Периметр треугольника = {self.perimeter()}")


# Класс-наследник "Прямоугольный треугольник"
class RightTriangle(Triangle):
    def __init__(self, side1, side2, angle):
        self.__side1 = side1
        self.__side2 = side2
        self.__angle = angle * pi

    def square(self):
        return 0.5 * self.__side1 * self.__side2

    def perimeter(self):
        return (
            self.__side1
            + self.__side2
            + sqrt(
                self.__side1**2
                + self.__side2**2
                - 2 * self.__side1 * self.__side2 * cos(self.__angle)
            )
        )


class IsoscelesTriangle(Triangle):
    def __init__(self, side1, side2, angle):
        self.__side1 = side1
        self.__side2 = side2
        self.__angle = angle * pi

    def square(self):
        return 0.5 * self.__side1 * self.__side2 * sin(self.__angle)

    def perimeter(self):
        return (
            self.__side1
            + self.__side2
            + sqrt(
                self.__side1**2
                + self.__side2**2
                - 2 * self.__side1 * self.__side2 * cos(self.__angle)
            )
        )


# Класс-наследник "Равнобедренный треугольник"
class EquilateralTriangle(Triangle):
    def __init__(self, side1, side2, angle):
        # Если неверно заданы стороны или угол -> ошибка
        if side1 != side2 or angle != 60:
            raise ValueError("Не равнобедренный треугольник!")
        else:
            self.__side1 = side1
            self.__side2 = side2
            self.__angle = angle * pi

    def square(self):
        return (sqrt(3.0) / 4) * self.__side1**2

    def perimeter(self):
        return 3 * self.__side1


if __name__ == "__main__":
    # Проверка классов, задание значений, расчет
    tr1 = RightTriangle(3, 4, 30)
    print(f"Площадь прямоугольного треугольника: {tr1.square()}")
    print(f"Периметр прямоугольного треугольника: {tr1.perimeter()}")
    tr2 = IsoscelesTriangle(2, 2, 45)
    print(f"Площадь равнобедренного треугольника: {tr2.square()}")
    print(f"Периметр равнобедренного треугольника: {tr2.perimeter()}")
    tr3 = EquilateralTriangle(5, 5, 60)
    print(f"Площадь равностороннего треугольника: {tr3.square()}")
    print(f"Периметр равностороннего треугольника: {tr3.perimeter()}")
    print("-" * 20)
    # Проверка функции вывода посчитанных значений
    tr1.print_info()
    tr2.print_info()
    tr3.print_info()
