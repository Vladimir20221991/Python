# Задача 1: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = int(input("Введите число:"))
def  Sumnumber(num):
    tot = 0
    while(num > 0):
        dig = num % 10
        tot = tot + dig
        num = num//10
    return tot
print(Sumnumber(n))