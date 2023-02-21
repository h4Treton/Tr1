n = int(input('Введите n: '))
for i in range(2, n + 1, 2):
    print(i, end=' ')
    if i % 5 == 0:
        print('')
