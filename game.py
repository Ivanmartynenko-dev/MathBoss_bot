import random



#Дописать функцию, чтобы она генерировал пример, в котором
# складываются или вычитаются числа(без отрицательных ответов)
# функция возвращает список следующего вида [число1 знак число2 ответ]
# добавлять в список при помощи append

def level_1():
    a = str(random.randint(1, 100))
    b = str(random.randint(1,100))
    signs = ['+', '-']
    sign = signs[random.randint(0, 1)]
    if a >= b:
        return[a, sign, b, eval(a+sign+b)]
    else:
        return[b, sign, a, eval(b+sign+a)]

print(level_1())