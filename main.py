# str2 = input('Введите число: ')
# while not str2.isdigit():
#     str2 = input('Введите число: ')
# print(str2)
import random
import string
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

# deposit_sum = float(input('Введите сумму вклада: '))
# x2_deposit_sum = deposit_sum * 2
# percent = float(input('Введите процент: '))
# years_count = 0
# while deposit_sum < x2_deposit_sum:
#     deposit_sum *= (1 + percent/100)
#     years_count += 1
# print(years_count)
#
#
# from string import printable
#
#
# def sms_len(str1):
#     count_c = 0
#     for i in str1:
#         if i in string.printable:
#             count_c += 1
#         else:
#             count_c += 2
#     if count_c % 140 == 0:
#         return count_c // 140
#     else:
#         return count_c // 140 + 1
#
#
# print(sms_len(input()))


# def bernam(str1, key_string):
#     res = ''
#     for i in range(len(str1)):
#         s1 = bin(ord(str1[i]))[2:].zfill(8)
#         s2 = bin(ord(key_string[i]))[2:].zfill(8)
#         for j in range(len(s1)):
#             if s1[j] == s2[j]:
#                 res += '0'
#             else:
#                 res += '1'
#         res += ' '
#     return res
#
#
# print(bernam('LONDON', 'SYSTEM'))


def bubble_sort (numbers):
    k = 0
    exit_i = False
    while not exit_i:
        k = 0
        ee2 = False
        while k < len(numbers) - 1:
            if numbers[k] > numbers[k+1]:
                uu = numbers[k]
                numbers[k] = numbers[k+1]
                numbers[k+1] = uu
                ee2 = True
                break
            else:
                k += 1
        if not ee2:
            exit_i = True
    return numbers


kk = []
for i in range(100):
    kk.append(random.randint(-500, 500))
print(kk)
print(bubble_sort(kk))
