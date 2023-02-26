def list_reverse(input_list):
    for i in range(len(input_list) // 2):
        input_list[i], input_list[len(input_list)-i-1] = input_list[len(input_list)-i-1], input_list[i]
    return input_list


print(list_reverse([1, 2, 3, 8, -3, 0, 6]))
