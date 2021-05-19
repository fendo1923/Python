
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
#//////////////////////////////////////////////////////////////////////////////#////////////////////////////////
"""import  time
#Version 2
# Создаём класс:
class Data:

    def __init__(self, data):
        self.data = data
    @classmethod
    def INT(self, data):
        self.data = data
        return int(data)
    @staticmethod
    def validation(data):
        try:
            valid_date = time.strptime(data, '%m/%d/%Y')
        except ValueError:
            print("Ошибка значений!!!Попробуйте снова")
        finally:
            print("Готово")
x = Data (12/1/12)
x.validation(data= input("Введите дату в фомате  «месяц/день/год»"))"""
#beta_ver1
    # def __init__(self, day, month, year):
    #     self.day = day
    #     self.month = month
    #     self.year = year
    # @classmethod
    # def INT(self, day, month, year):
    #     self.day = day
    #     self.month = month
    #     self.year = year
    #     return int(day), int(month), int(year)

# month = int(input("Введите меяц от 1 до 12"))
# res1 = "Месяц принят" if 0 < month < 13 else "Введены неверные данные по месяцам. Выбран 1 месяц"
# if 0 < month < 13:
#     month = month
# else:
#     month = 1
# day = int(input("Введите день от 1 до 31"))
# res2 = "День принят" if 0 < month < 32 else "Введены неверные данные по дням.Выбрано 1 число"
# if 0 < day < 31:
#     day = day
# else:
#     day = 1
# year = int(input("Введите год"))
# res3 = "Год принят" if 0 < year else "Введены неверные данные по годам.Выбран 1975 год"
# if 0 < year:
#     # if year < 10:
#     #     year = "0"+"0"+"0"+year
#     # elif year < 100:
#     #     year = "0" + "0" + year
#     # elif year < 1000:
#     #     year = "0" + year
#     # else:
#         year = year
# else:
#     year = 1975
# x = Data(day,month,year)
# print(res1+"\n"+res2+"\n"+res3)
# print("Дата:","«", x.day,"-",x.month,"-",x.year,"»")
#//////////////////////////////////////////////////////////////////////////////#////////////////////////////////
# 2. Создайте собственный класс-исклюычение, обрабатывающий ситуацию деления на нуль.
# # Проверьте его работу на данных, вводимх пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""class Noproblems:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @staticmethod
    def mm (a, b):
        try:
           a / b
           print(a / b)
        except ZeroDivisionError:
            print("<<Не надо так делать. Вы делите на 0!!!!>>")
        finally:
            print("Конец")
x = Noproblems(777 ,0)
x.mm(x.a, x.b)"""
# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.
# class Ex3:
#     y = input("Введите данные через запятую")
#     def __init__(self):
#         self.i = 0
#     def xxaxa (self, i = 0, y):
#         self.y = input("Введите данные через запятую")
#         self.i = i
# x = input("Введите данные через запятую")
#
# def check(x):
#     for i in x:
#         if not isinstance(i, int):
#             raise ValueError("Value Error")
# print(check(x))
'''class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        # self.my_list = [int(i) for i in input('Введите значения через пробел ').split()]
        # val = int(input('Введите значения и нажимайте Enter - '))
        # self.my_list.append(val)
        while True:
            try:
                val = int(input('Введите значения - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булевое значение")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'вСё'
                else:
                    return f'Всё'
try_except = Error(1)
print(try_except.my_input())'''
# 4&5&6 Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием.
# # Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''class Warehouse:
    info = "<<Склад оргтехники>>"
    def __init__(self, years, numbers, position):
        self.years = years
        self.numbers = numbers
        self.position = position

class office_equipment(Warehouse):
    def oe(self, printer, xerox, scaner, place,position):
        self.scaner = scaner
        self.printer = printer
        self.xerox = xerox
        self.place = place
        self.position = position
    def printer(self, years = 2021, numbers = 10, place = "Warehouse", color = "сolour"):
        self.numbers = numbers
        self.color = color
        self.place = place
        return years, numbers, place, color

    def xerox (self, years=2020, numbers=5, place = "Warehouse", mass = "heavi"):
        self.years = years
        self.numbers = numbers
        self.mass = mass
        self.place = place
        return  years, numbers, place, mass

    def scaner (self, years= 2021, numbers=15, place = "Warehouse", portative = "portative"):
        self.years = years
        self.numbers = int(numbers)
        self.place = place
        self.portative = portative
        return years, numbers, portative, place
    def replace (self):
        if y.numbers==0:
            y.numbers = "Товар временно отсутствует"

        return {y.position:(y.place,y.numbers)}

x = Warehouse(2021,30,"xerox")
y = office_equipment("printer", "xerox", "scaner")
print(x.info)
print(y.scaner())
y.position = "printer" or "xerox"
y.place =  "Office" or "Stadium"
y.numbers = 1
print(y.replace())
print(y.replace())
'''
# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
'''class Complex:

    def __init__(self, a, b):
        self.a = complex(1, 4)
        self.b = complex(1, 2)

    def sum (self):
        return self.a + self.b
    def umn (self):
        return self.a * self.b

y = Complex(1,2)
print(y.a)
print(y.b)
print(f"Умножение комплексных чисел: {y.a} * {y.b} = {y.umn()}")
print(f"Сложение комплексных чисел:  {y.a} + {y.b} = {y.sum()}")'''