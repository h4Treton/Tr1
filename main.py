# str2 = input('Введите число: ')
# while not str2.isdigit():
#     str2 = input('Введите число: ')
# print(str2)
# import string
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


# def bubble_sort (numbers):
#     k = 0
#     exit_i = False
#     while not exit_i:
#         k = 0
#         ee2 = False
#         while k < len(numbers) - 1:
#             if numbers[k] > numbers[k+1]:
#                 uu = numbers[k]
#                 numbers[k] = numbers[k+1]
#                 numbers[k+1] = uu
#                 ee2 = True
#                 break
#             else:
#                 k += 1
#         if not ee2:
#             exit_i = True
#     return numbers
#
#
# kk = [1, 5, 3, 9, 0, 8, -5, -2]
# print(bubble_sort(kk))

# class Rectangle:
#
#     def __init__(self, x1, y1, x2, y2):
#         self.width = abs(x1 - x2)
#         self.height = abs(y1 - y2)
#
#     def perimeter(self):
#         return (self.width + self.height) * 2
#
#     def area(self):
#         return self.width * self.height
#
#
# rec1 = Rectangle(2, -2, 5, 5)
# print(rec1.perimeter())
# print(rec1.area())

# class Category:
#
#     categories = []
#
#     @classmethod
#     def add(cls, category_name: str):
#         if category_name not in cls.categories:
#             cls.categories.append(category_name)
#             return len(cls.categories) - 1
#         else:
#             raise ValueError
#
#     @classmethod
#     def get(cls, index: int):
#         if index < len(cls.categories):
#             return cls.categories[index]
#         else:
#             raise IndexError
#
#     @classmethod
#     def delete(cls, index: int):
#         if index < len(cls.categories):
#             del cls.categories[index]
#
#     @classmethod
#     def update(cls, index: int, new_category_name: str):
#         if index >= len(cls.categories):
#             if new_category_name not in cls.categories:
#                 cls.categories.append(new_category_name)
#             else:
#                 raise ValueError
#         else:
#             cls.categories[index] = new_category_name
#
#
# print(Category.categories)
# Category.add('Кот')
# Category.add('Пес')
# Category.add('Тюлень')
# print(Category.categories)
# # Category.add('Кот')
# print(Category.get(0))
# print(Category.get(1))
# Category.delete(1)
# print(Category.categories)
# Category.add('Слон')
# print(Category.categories)
# Category.update(2, 'Слониха')
# print(Category.categories)
# Category.update(5, 'Голубь ')
# print(Category.categories)

# import string
#
# class RegisterForm:
#
#     def __init__(self, username: str, password: str):
#         self.username = username
#         self.password = password
#
#     def is_valid(self):
#         f_upper = False
#         f_digits = False
#         for i in range(len(self.password)):
#             if self.password[i] in string.ascii_uppercase:
#                 f_upper = True
#             if self.password[i] in string.digits:
#                 f_digits = True
#         if not isinstance(self.username, str) or not isinstance(self.password, str):
#             return False
#         elif len(self.username) < 2:
#             return False
#         elif len(self.password) < 8:
#             return False
#         elif self.password.find(self.username) != -1:
#             return False
#         elif not f_upper or not f_digits:
#             return False
#         return True
#
#
# rf1 = RegisterForm('user1', 'user1password')
# print(rf1.is_valid())

# from collections import Counter
#
#
# class Numbers:
#     def __init__(self, numbers_list: list[int]):
#         self.numbers_list = numbers_list
#
#     def average(self):
#         sum2 = 0
#         for el in self.numbers_list:
#             sum2 += el
#         return sum2/len(self.numbers_list)
#
#     def max_count(self):
#         max_count_list = Counter(self.numbers_list)
#         max_common = max_count_list.most_common(1)
#         max_common = [*filter(lambda x: self.numbers_list.count(x) == max_common, self.max_common)]
#         return sum(max_common)/len(max_common)
#
#
# num2 = Numbers([1, 2, 3, 4, 4, 3])
# print(num2.max_count())
# from io import DEFAULT_BUFFER_SIZE
#
#
# print(DEFAULT_BUFFER_SIZE)
# file = open('input.txt', 'r', encoding='utf-8')
#
# # print(file.read())
# # print(file.readline())
# # print(file.readlines())
# lines = [line.strip() for line in file if line.strip()]
# print(lines)
# text = 'Brevis, germanus mortems saepe promissio de azureus, secundus barcas.'
# file = open('output.txt', 'w', encoding='utf-8')
# file.write(text)
# file.close()

