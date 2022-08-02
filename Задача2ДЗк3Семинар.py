#Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#Пример:

# список: ["qwe", "asd", "zxc", "qwerty", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5 если я не ошибаюсь то здесь допущена ошибка.
# правилный ответ 4, потому что индексы считаются с 0, а не с 1.
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1



text1 = "qwe asd zxc rtyqwe ertqwe" #где мы ищем

text2 = "qwe" # что мы ищем

def position_second_occurrence(text1, text2):
    temp_list = text1.split()
    count = 0
    index = 0
    answer = ''
    for i in range(len(temp_list)):
        if count != 2:
            if text2 in temp_list[i]:
                index = i
                count += 1
        else: break
    if count == 0: answer = f'строки {text2} в списке нет'
    elif count == 1: answer = f'Строка {text2} имеется только в одном варианте'
    else: answer = f'второго вхождения строки {text2} находится на позиции {index}' 
    return answer

print(position_second_occurrence(text1, text2))
