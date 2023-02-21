n = int(input('Введите число n: '))
m = int(input('Введите число m: '))
k = int(input('Введите число k: '))
k += 1
while n > 0:
    if k % m == 0:
        print(k)
        n -= 1
    k += 1
