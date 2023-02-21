input_string = input('Введите строку: ')
char_dictionary = {}
for i in range(len(input_string)):
    col = 0
    for j in range(len(input_string)):
        if input_string[j] == input_string[i]:
            col += 1
    char_dictionary[input_string[i]] = col
print(char_dictionary)
