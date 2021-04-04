import numpy
n = int(input('Введите номер члена:  '))

a = (2 ** n) - n
b = 1 / (1 - n)
c = (-1) ** n + numpy.sqrt(2 * n)
d = ((-1) ** (2 * n)) + (1 / (n ** 2))
print(a)
print(b)
print(c)
print(d)