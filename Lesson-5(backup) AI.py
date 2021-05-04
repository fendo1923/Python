# couding: utf-8
# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
'''
from math import inf
i=1
while i<inf:
    y = input("Введите построчные данные")
    x1 = list(y.split())
    with open ("text.txt",'w') as x:
        print(f"{x1[i]}\n{x1[i+1]}\n{x1[i+2]}",file=x)
    i+=1
print("Готово")
'''
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
import string

'''
x = open ("111.txt")
i=1
while i<4:
    y = x.readlines(i)
    w = x.readline()
    if len(y)==0:
        break
    else:
        print(f"{i})",y,w,len(w))
        i+=1
x.close()
'''
# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
'''
x = open("111.txt","r",encoding='utf-8')
y = x.read()
z = y.split()
print(type(z))
i=1
while i<6:
    if z[i]<'20000':
        print(f"{z[i-1 ]} получает {z[i]} ")
    i += 2
x.close()
'''
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
'''
x = open("text1.txt")
from textblob import TextBlob
blob = TextBlob(x.read())
print(blob.translate(to='ru'))
y = open("text_new.txt","w")
z = str(blob.translate(to='ru'))
y.write(z)
x.close() and y.close
'''
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
# x = open("1_2.txt","w")
# y = str(input("Введите числа через пробел"))
# x.write(y)
# z = x.read()
# print(z)
'''
y = input("Введите построчные данные")
x1 = list(y.split())
x = open ("1_2.txt",'w')
z = x.write(y)
res = [float(el) for el in x1]
print(f"Cумма чисел в файле:{sum(res)}, Среднее значение:{sum(res)/len(res)}")
x.close()
'''
# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
# x1 = {}
# x = open ("6.txt","r",encoding='utf-8')
# y = x.read()
# z = list(y.split())
# res
# print(res)
'''
subj = {}
with open('6.txt', 'r') as x:
    for line in x:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f"Общее количество часов по предмету - \n {subj}")
'''
# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
# import json
# profit = {}
# pr = {}
# prof = 0
# prof_aver = 0
# i = 0
# with open('file_7.txt', 'r') as file:
#     for line in file:
#         name, firm, earning, damage = line.split()
#         profit[name] = int(earning) - int(damage)
#         if profit.setdefault(name) >= 0:
#             prof = prof + profit.setdefault(name)
#             i += 1
#     if i != 0:
#         prof_aver = prof / i
#         print(f'Прибыль средняя - {prof_aver:.2f}')
#     else:
#         print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
#     pr = {'средняя прибыль': round(prof_aver)}
#     profit.update(pr)
#     print(f'Прибыль каждой компании - {profit}')
#
# with open('file_7.json', 'w') as write_js:
#     json.dump(profit, write_js)
#
#     js_str = json.dumps(profit)
#     print(f'Создан файл с расширением json со следующим содержимым: \n '
#           f' {js_str}')