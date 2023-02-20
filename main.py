# str2 = input('Введите число: ')
# while not str2.isdigit():
#     str2 = input('Введите число: ')
# print(str2)

# n = int(input('Введите число: '))
# max_number = 0
# if n < 10:
#     max_number = n
# else:
#     while n > 10:
#         if n % 10 > max_number:
#             max_number = n % 10
#         n = n // 10
# print(max_number)

# n = int(input('Введите число: '))
# mon = (25, 10, 5, 1)
# count = 0
# for i in mon:
#     count += (n // i)
#     n %= i
# print(count)

deposit_sum = float(input('Введите сумму вклада: '))
x2_deposit_sum = deposit_sum * 2
percent = float(input('Введите процент: '))
years_count = 0
while deposit_sum < x2_deposit_sum:
    deposit_sum *= (1 + percent/100)
    years_count += 1
print(years_count)


