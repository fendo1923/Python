# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
# ///////////////////////////////////////////////# ///////////////////////////////////////////////
'''# Создаём класс:
class Matrix:
    info = "Матрица"
# Создаём атрибут:
    def __init__(self, list1, list2, list3):
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3
        self.matrix = [list1, list2, list3]
# Создаём методы:
    def __str__(self):
        super().__init__()
        print(f"Матрица #1: {self.matrix}")

    def __add__(self, other):
        return f" Сумма #1: {[(self.list1[0] + x1.list1[0],self.list1[1] + x1.list1[1]), (self.list2[0] + x1.list2[0],self.list2[1] + x1.list2[1]), (self.list3[0] + x1.list3[0],self.list3[1] + x1.list3[1])]}"
# Создаём класс:
class Matrix2(Matrix):
# Создаём атрибут:
    def daat (self, matrix, list1, list2, list3):
        Matrix.__init__(matrix, list1, list2, list3)
# Создаём методы:
    def __str__(self):
        print(f"Матрица #2: {self.matrix}")

    def __add__(self, other):
        return f" Сумма #2 : {[(self.list1[0] + other.list1[0],self.list1[1] + other.list1[1]), (self.list2[0] + other.list2[0],self.list2[1] + other.list2[1]), (self.list3[0] + other.list3[0],self.list3[1] + other.list3[1])]}"

x = Matrix((1, 12), (7, 11), (3, 12))
x2 = Matrix2((1, 130), (0, 44), (32, 23))
x1 = Matrix2((7, 670), (5, 11), (3, 12))
x.__str__()
x1.__str__()
print(x + x1)
print(x1 + x2)'''


# ///////////////////////////////////////////////# ///////////////////////////////////////////////
# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
# ///////////////////////////////////////////////# ///////////////////////////////////////////////
'''#Создаём класс:
class Clothes:
    info = "<<Программа для подсчёта расхода ткани на одежду>>"

    # Создаём атрибут:

    def __init__(self, size=52, height=184):
        self.size = size
        self.height = height


# Создаём дочерний класс:
class Suit(Clothes):

    def sd(self, height):
        self.height = height
        return (2 * height + 0.3)


class Coat(Clothes):
    def cd(self, size):
        self.size = size
        return (size / 6.5) + 0.5


class Time:
    def __init__(self, days = 5):
        self.days = days
# Создаём свойство
    @property
    def days(self):
        return self.days * 8
# Создаём сеттер
    @days.setter
    def days (self, days):
        if days < 1:
            self.days = "малый расход"
        elif days < 9:
            self.days = "средний расход"
        else:
            self.days = "максимальный расход"

    def info(self):
        print(f"{x3.days} часов- {str(self.days)}")

x = Clothes()
x1 = Suit(x.height)
x2 = Coat(x.size)
x3 = Time()
print(x.info)
print(x1.sd(x.height))
print(round(x2.cd(x.height)))'''


# ///////////////////////////////////////////////# ///////////////////////////////////////////////
# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# # Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
'''class Cage:
    info = "<<Клетка>>"
    def __init__(self, numb1 ):
        self.numb1 = numb1

    # Сложение
    def __add__(self, other):
        return Cage(self.numb1 + other.numb1)
    # Вычитание
    def __sub__(self, other):
       return self.numb1 - other.numb1 if self.numb1 - other.numb1 > 0 else "Неверные значения!!!"

    # Умножение
    def __mul__(self, other):
        return Cage(self.numb1 * other.numb1)
    # Деление
    def __truediv__(self, other):
        return Cage(self.numb1 // other.numb1)

    def make_order(self, row):
        res = " "
        for i in range(int(self.numb1/row)):
            res += "*" * row + "\n"
        res += "*" * (self.numb1 % row) + "\n"
        return res
    
x = Cage(10)
x1 = Cage(5)
print(Cage.info)
print(x + x1)
print(x - x1)
print(x * x1)
print(x / x1)
print(x.make_order(2))'''