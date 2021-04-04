import sympy
n = int(input('Введите номер члена:  '))
a = sympy.limit(n / (n ** (1 / n)), n, sympy.oo)
print(a)