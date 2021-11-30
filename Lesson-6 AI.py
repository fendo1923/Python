# couding=<utf-8>
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
# ///////////////////////////////////////////////# ///////////////////////////////////////////////
'''import time
from idlelib.multicall import r
# Создаём класс светофор:
class TrafficLight:
    info = "<<Программа служит для отображения работы светофора>> \nПереключение осуществляться только в указанном порядке (красный, желтый, зеленый):"
    # Создаём атрибут цвет:
    def __init__(self):
        self.__red = "Красный сигнал - <СТОЙ>!"
        self.__yellow = "Жёлтый сигнал - <ПРИГОТОВИТЬСЯ>!"
        self.__green = "Зелёный сигнал - <НАЧИНАЙТЕ ДВИЖЕНИЕ>!"
        self.__green1 = "Мигающий зелёный сигнал - <ВНИМАНИЕ БУДЕТ ВКЛЮЧЕН ЗАПРЕЩАЮЩИЙ СИГНАЛ СВЕТОФОРА>!"
    #  Создаём метод работы: можем обойтись без него
    # def running(self, r,y,g):
    #     print("Загорелся сигнал светофора ")
    #     self.r = 7
    #     self.y = 2
    #     self.g = 15
# Присваиваем переменную для класса, с целью дальнейшей работы с ней
x = TrafficLight()
print(x.info)
# Проверяем работу отображения сигналов посекундно (в реальном режиме работы с заданным условием)
i = 1
while i < 25:
    time.sleep(1)
    if i < 8:
        print(f"{i}c. {x._TrafficLight__red}")
    elif i < 10:
        print(f"{i}c {x._TrafficLight__yellow}")
    elif i < 22:
        print(f"{i}c {x._TrafficLight__green}")
    else:
        print(f"{i}c {x._TrafficLight__green1}")
    i+=1
# В случае, если необходимо сделать постоянную работу светофора необходимо добавить к циклу 2 следующих строки:
#     if i == 25:
#         i = 1'''
# ///////////////////////////////////////////////# ///////////////////////////////////////////////
# from tkinter import Tk
# x = Tk()
# x.mainloop()
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
# ///////////////////////////////////////////////# ///////////////////////////////////////////////
'''# Создаём класс Road
lass Road:
    info = "Программа для расчета массы асфальта, необходимого для покрытия всего дорожного полотна"
#Создаём атрибуты
    def __init__(self,lenght,width):
        self._lenght = lenght
        self._width = width
#Создаём функцию для подсчёта массы асФАЛЬТА
    def massa(self, lenght, width, m1m,thickness):
        self.lenght = x._lenght
        self.width = x._width
        self.m1m = m1m
        self.thickness = thickness
        return lenght * width * m1m * thickness
# Создаём функцию для отображения информации
    def DisplayInfo(self):
        print("Длина:", self._lenght , ", Ширина:", self._width, ", Масса асфальта в 1 см :", self.m1m," Толщина полотна :", self.thickness)
#Присваиваем переменную для нашего класса
x = Road(3000, 5)
#Печатаем итоговую информацию
print(x.info)
print(f"Масса афальта будет равна: {x.massa(3000, 5, 0.4, 400)} кг")
x.DisplayInfo()'''
# ///////////////////////////////////////////////# ///////////////////////////////////////////////
# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
# ///////////////////////////////////////////////# ///////////////////////////////////////////////
'''#Создаём класс работник:
import self as self
class Worker:
    workcount = 0
    info = "Программа отображает персональные данные в компании "
#Присваиваем атрибуты:
    def __init__(self, name, surname,position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        Worker.workcount +=1
#Создаём для подсчета рабочий в компании:
    def DispCount(self):
        print("Количество сотрудников в базе %d:" % Worker.workcount)
# Создаём для отображения полной информации о работнике:
    def DisplayInfo(self):
        print("Name:", self.name, ", Surname:", self.surname, ", Position:", self.position, ", Income:", self._income)
# Создаём класс должность:
class Position(Worker):
# Присваиваем атрибуты:
    def FullInfo(self, get_full_name, get_total_income):
        self.get_full_name = f"name:{x.name} \nsurname: {x.surname} \nposition: {x.position}"
        self.get_total_income = int(x._income["wage"]) + int(x._income["bonus"])
        return get_full_name, get_total_income
    def DisplayInfo2(self):
        print("Полное наименование сотрудника:\n", y.get_full_name, ", доход с учётом премии:", y.get_total_income)
# Присваиваем переменные для наших классов:
x = Worker("Morty", "Smith", "Morty", 1, 1)
y = Position(x.name,x.surname,x.position,x._income["wage"],x._income["bonus"])
# Добавим ещё трех сотрудников:
p1 = Worker("Ivan", "Ivanov", "IvanInFirm", 1001, 500)
p2 = Worker("Fedor", "Fedorov", "FedorInFirm", 1000, 500)
p3 = Worker("Rick", "Sanchez", "The greatest scientist", 999999999, 999999999)
# Выводим данные сотрудников на экран:
x.DisplayInfo()
p1.DisplayInfo()
p2.DisplayInfo()
p3.DisplayInfo()
# Выводим количество сотрудников в выведенной на экран базе
print("Количество сотрудников в базе %d:" % (Worker.workcount-1))
# Добавляем атрибуты к классу Position и выводим доход с учетом премии:
print(y.FullInfo((x.name,x.surname,x.position),(x._income["wage"],x._income["bonus"])))
y.DisplayInfo2()'''
# ///////////////////////////////////////////////# ///////////////////////////////////////////////
# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# ///////////////////////////////////////////////# ///////////////////////////////////////////////
'''# Создаём класс Car:
class Car:
# Создадим атрибуты:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
# Создадим методы:
    def GO (self):
        print("Машина поехала")
    def STOP (self):
        print("Машина остановилась")
    def TURN (self):
        print("Машина повернула")
    def show_speed(self):
        if c2.speed > 60:
            print("Превышение скорости у TownCar")
        if c4.speed > 40:
            print("Превышение скорости у WorkCar")
        print(f"{self.speed} км/ч")
# Создадим дочерние классы с атрибутами
class TownCar(Car):

    def infoT(self):
        self.speed = 60
        self.color = "Black"
        self.name = "Priora"
        self.is_police = "None"

class SportCar(Car):

    def infoS(self):
        self.speed = "black"
        self.color = "VeryBlack"
        self.name = "VaZ-2170 на валах"
        self.is_police = "ACAB"

class WorkCar(Car):

    def infoW(self):
        self.speed = 90
        self.color = "Grey"
        self.name = "Logan"
        self.is_police = "None"

class PoliceCar(Car):

    def infoP(self):
        self.speed = 220
        self.color = "black&white"
        self.name = "Dodge Viper"
        self.is_police = "is_police"
# Добавим данные для работы:
c1 = Car(520, "Red", "Toyota Supra 2JZ-GTE", "NoNE")
c2 = TownCar(60, "grey", "Dodge Viper","None")
c3 = SportCar(999, "black", "VAZ-2170","None")
c4 = WorkCar (90, "white", "Logan","None")
c5 = PoliceCar (220, "black&white", "Dodge Viper","is_police")
# Проверим работоспособность:
print(c1.name)
c1.show_speed() 
c1.GO()
c1.TURN()
c1.GO()
c1.STOP()
print(c2.name)
c2.show_speed()
c2.GO()
c2.STOP()'''
# ///////////////////////////////////////////////# ///////////////////////////////////////////////
# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
# ///////////////////////////////////////////////# ///////////////////////////////////////////////
'''# Создадим класс
class Stationery:
# Создадим атрибут:
    def __init__(self, name):
        self.name = name
# Создадим метод:
    def draw(self):
        print("“Запуск отрисовки.”")
# Создим три дочерних класса:
class Pen(Stationery):

    def infoPen (self, name):
        self.name = name
    def draw(self):
        print("отрисовка РУЧЧЧККОЙ ")

class Pencil(Stationery):

    def infoPencil (self, name):
        self.name = name
    def draw(self):
        print("отрисовка КАРАНДАШОМ ")

class Handle(Stationery):

    def infoHandle(self, name):
        self.name = name
    def draw(self):
        print("отрисовка МАРКЕРОМ")

x = Stationery("Stationery")
x1 = Pen("Pen")
x2 = Pencil("Pencil")
x3 = Handle("Handle")
print(x2.name)
x2.draw()
print(x3.name)
x3.draw()
print(x1.name)
x1.draw()
print(x.name)
x.draw()'''
# ///////////////////////////////////////////////# ///////////////////////////////////////////////