# (готово)
# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def delete(arg1, arg2):
    return arg1 / arg2
i = 1
while i < 9999:
    x = float(input("Input first number:"))
    y = float(input("Input second number:"))
    if y==0:
        print(f"Attention you devide on {y}!!!!!!")
    else:
        z = delete(x, y)
        print(i, f") {x} / {y} = ", round(z, 2))
    i= i + 1
'''
# готово
# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
import math

'''
i = 1
while i < 9999:
    a = input("Input you name:")
    b = input("Input your surname:")
    c = input("Input your birth year:")
    d = input("Input your city:")
    e = input("Input your email:")
    f = input("Input your phone:")
    def enter (name, surname, birth_year, city, email, phone):
        print(i,f")",f"name: {a.title()}; surname: {b.title()}; birth year: {c}; city: {d.title()}, email: {e}; phone: {f}")
    enter(name=a, surname=b, birth_year=c, city=d, email=e, phone=f)
    i=i+1
'''
# (готово)
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''
i=1
while i<9999:
    a = float(input("Input first number:"))
    b = float(input("Input second number:"))
    c = float(input("Input third number:"))
    def delete(arg1, arg2, arg3):
        return arg1+arg2+arg3-min(arg1, arg2, arg3)
    print(i,")","Cумма наибольших двух аргументов =", delete(a, b, c))
    i=i+1
'''
# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
#Var1
'''
i=1
while i<9999:
    x = float(input("Input first number:"))
    y = float(input("enter the degree of the number:"))
    def degr1e (arg1,arg2):
        return arg1**arg2
    print(f"the result {x} of exponentiation {y} :",degr1e(x,y))
    i=i+1
'''
#Var2 Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''
x = float(input("Input first number:"))
y = float(input("enter the degree of the number:"))
def degr1e(arg1, arg2):
    return arg1 ** arg2
i=0
while i<=y:
    i=i+1
print(f"the result {x} of exponentiation {y} :",degr1e(x,y))
'''
#Var3
'''
i=1
while i<9999:
    x = float(input("Input first number:"))
    y = float(input("enter the degree of the number:"))
    def degr1e (arg1,arg2):
        return pow(arg1,arg2)
    print(f"the result {x} of exponentiation {y} :",degr1e(x,y))
'''
# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''
print("stop app- you must enter-000!!!".upper())
x=input("Введите строку чисел, разделенных пробелом")
y=(x.split())
y_int=[float(x) for x in y]
z=sum(y_int)
print(z)
n=1
while n<math.inf:
    if x=='000':
        print(f"Сумма равна:{z}.The end!")
        break
    n = z
    x = input("Введите строку чисел, разделенных пробелом")
    y = (x.split())
    y_int = [float(x) for x in y]
    z = sum(y_int) + n
    print(z)
'''
# (готово)
# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
'''
print("stop app- you must enter-stop!!!".upper())
i=1
while i<99999:
    x=input("Введите слово")
    if x=="STOP":
        input("STOP app!")
        break
    print(f"{i}) Было:",x.lower())
    def int_func (arg):
        return arg.title()
    print(f"{i}) Стало:",int_func(x))
    i=i+1
'''
