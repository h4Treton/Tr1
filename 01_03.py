input_name = input('Введите имя: ')
input_age = int(input('Введите возраст: '))
input_city = input('Введите город: ')
print('Приветствуем, ' + input_name + ' ' + str(input_age) + ' лет из ' + input_city)
print("Приветствуем, %s %d лет из %s" % (input_name, input_age, input_city))
print("Приветствуем, {} {} лет из {}".format(input_name, input_age, input_city))
