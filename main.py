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

class Category:

    categories = []

    @classmethod
    def add(cls, category_name: str):
        if category_name not in cls.categories:
            cls.categories.append(category_name)
            return len(cls.categories) - 1
        else:
            raise ValueError

    @classmethod
    def get(cls, index: int):
        if index < len(cls.categories):
            return cls.categories[index]
        else:
            raise IndexError

    @classmethod
    def delete(cls, index: int):
        if index < len(cls.categories):
            del cls.categories[index]

    @classmethod
    def update(cls, index: int, new_category_name: str):
        if index >= len(cls.categories):
            if new_category_name not in cls.categories:
                cls.categories.append(new_category_name)
            else:
                raise ValueError
        else:
            cls.categories[index] = new_category_name


print(Category.categories)
Category.add('Кот')
Category.add('Пес')
Category.add('Тюлень')
print(Category.categories)
# Category.add('Кот')
print(Category.get(0))
print(Category.get(1))
Category.delete(1)
print(Category.categories)
Category.add('Слон')
print(Category.categories)
Category.update(2, 'Слониха')
print(Category.categories)
Category.update(5, 'Голубь')
print(Category.categories)
