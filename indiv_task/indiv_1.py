#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Man (человек), с полями: имя, возраст, пол и вес.
Определить методы переназначения имени, изменения возраста и изменения веса.
Создать производный класс Student, имеющий поле года обучения.
Определить методы переназначения и увеличения года обучения.
"""


class Man:
    # Инициализация класса "Человек"
    def __init__(self, name, age, sex, weight):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def sex(self):
        return self.__sex

    @property
    def weight(self):
        return self.__weight

    @name.setter
    def name(self, value):
        self.__name = value

    @age.setter
    def age(self, value):
        self.__age = value

    @sex.setter
    def sex(self, value):
        self.__sex = value

    @weight.setter
    def weight(self, value):
        self.__weight = value

    def set_name(self, name):
        self.name = name

    def set_weight(self, weight):
        self.weight = weight

    def set_age(self, age):
        self.age = age

    # Функция вывода
    def display(self):
        print()
        print(f"Имя: {self.name}")
        print(f"Пол: {self.sex}")
        print(f"Возраст: {self.age}")
        print(f"Вес: {self.weight}")


# Производный класс "Человек" -> "Студент"
class Student(Man):
    def __init__(self, name, age, sex, weight, study_year):
        # Доступ к наследуемым элементам
        super().__init__(name, age, sex, weight)
        # Поле "Год обучения"
        self.study_year = study_year

    @property
    def study_year(self):
        return self.__study_year

    @study_year.setter
    def study_year(self, value):
        self.__study_year = value

    def set_study_year(self, value):
        self.study_year = value

    def increase_study_year(self):
        self.study_year += 1

    def display(self):
        super(Student, self).display()
        print(f"Год обучения: {self.study_year}")


if __name__ == "__main__":
    m1 = Man(name="Andrey", age=18, sex="Male", weight=50)
    m1.display()
    m1.set_age(20)
    m1.set_weight(43)
    m1.display()

    m2 = Student(name="Test", age=23, sex="Female", weight=100, study_year=2)
    m2.display()
    m2.increase_study_year()
    m2.set_name("Jean")
    m2.set_age(22)
    m2.display()
