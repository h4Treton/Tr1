def list_offset(input_list, offset: int):
    result_list = input_list.copy()
    for i in range(len(input_list)):
        result_list[(i + offset) % len(input_list)] = input_list[i]
    return result_list


print(list_offset([1, 2, 3, 8, -3, 6], 3))
print(list_offset([1, 2, 3, 4, 5, 6, 7], 3))
