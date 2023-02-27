def dec_to_bin(dec_number: int):
    binary_str = ''
    max_bite = 0
    while 2 ** max_bite <= dec_number:
        max_bite += 1
    for i in range(max_bite - 1, -1, -1):
        if 2 ** i > dec_number:
            binary_str += '0'
        else:
            binary_str += '1'
            dec_number -= 2 ** i
    if binary_str == '':
        binary_str = '0'
    return binary_str


print(dec_to_bin(2))
