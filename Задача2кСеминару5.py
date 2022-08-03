'''Задача 2: Дан список чисел. Создайте список, в который попадают числа, 
описываемые возрастающую последовательность.
Порядок элементов менять нельзя.
Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
[1, 5, 2, 3, 4, 1, 7] => [1, 5]'''

nums = [ 1, 5, 2, 3, 4, 6, 1, 7]

def get_up(nums):
    ups = []
    for i in range(len(nums)):
        if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
            ups.append(nums[i])
    return ups

print(nums)
print(get_up(nums))
