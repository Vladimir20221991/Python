# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

from calendar import weekday
from datetime import datetime

week_days = ('Понедельник', 'Вторник', 'Среда', 'Четверг',
             'Пятница', 'Суббота', 'Воскресенье')
number = int(input('Введите номер дня недели: '))

def Find_day(list, num):
    if num <= 0:
        return ' Неверный день недели '
    if 0 < num < 6:
        return f' {week_days[num-1]}, Рабочий день' 
    elif 5 < num <= 7:
        return f' {week_days[num-1]}, Выходной день '

day_name = Find_day(week_days, number)
print(day_name)