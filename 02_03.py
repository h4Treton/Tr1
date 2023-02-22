email_dictionary = {}
n = int(input('Введите количество элементов: '))
for i in range(n):
    print('Введите имя человека {}:'.format(i+1))
    name = input()
    print('Введите email человека {}:'.format(i+1))
    email = input()
    email_dictionary[i] = {}
    email_dictionary[i]['name'] = name
    email_dictionary[i]['email'] = email
print(email_dictionary)
