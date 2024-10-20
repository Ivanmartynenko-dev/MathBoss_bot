import random



#Дописать функцию, чтобы она генерировал пример, в котором
# складываются или вычитаются числа(без отрицательных ответов)
# функция возвращает список следующего вида [число1 знак число2 ответ]
# добавлять в список при помощи append

def level_1():
    a = random.randint(1, 100)
    b = random.randint(1,100)
    c=0
    signs = ['+', '-']
    sign = signs[random.randint(0, 1)]
    if a >= b:
        return[a, sign, b, eval(str(a)+sign+str(b))]
    else:
        return[b, sign, a, eval(str(b)+sign+str(a))]

print(level_1())