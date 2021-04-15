# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

num=int(input("Введите время в секундах"))
minute=num//60
h: int=minute//60
n=num//60
m=minute//60
if num>60:
    num =int(num - (n * 60))
if minute>60:
    minute =int(minute - (m * 60))
print("чч:", h,"мм:", minute,"sec:", num)

