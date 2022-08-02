# Задача 1: Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

from random import  randint
import itertools

n = int(input(('Введите число: ')))
    
mylist = ['Road', 'Maria', 'Shop', '2', '345', '7']

def find_number(n, lst):
    return str(n) in lst

print(mylist)

print(find_number(n, mylist))
