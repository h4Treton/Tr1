a1 = float(input('Введите первое число: '))
oper = input('Введите операцию: ')
a2 = float(input('Введите второе число: '))
if oper == '+':
    print('Результат: {}'.format(a1+a2))
elif oper == '-':
    print('Результат: {}'.format(a1-a2))
elif oper == '*':
    print('Результат: {}'.format(a1*a2))
elif oper == '/':
    print('Результат: {}'.format(a1/a2))
else:
    print('Неверная операция!')
