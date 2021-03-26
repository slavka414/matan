a = int(input('Введите бит а:  '))
b = int(input('Введите бит b:  '))
c = int(input('Введите бит c:  '))

def implication(a, b, c):
    if a == 0 and b == 0 and c == 0:
        i = 1
    elif c == 1:
        i = 1
    else:
        i = 0
    return i

def ecvivalent(a, b, c):
    if a == 0 and b == 0 and c == 0:
        e = 1
    elif a == 1 and b == 1 and c == 1:
        e = 1
    else:
        e = 0
    return e

if a == 0 or a == 1:
    if b == 0 or b == 1:
        if c == 0 or c == 1:
            print('Сложение')
            print(a & b & c)
            print('Умножение')
            print(a | b | c)
            print('Импликация')
            print(implication(a, b, c))
            print('Эквивалентность')
            print(ecvivalent(a, b, c))


