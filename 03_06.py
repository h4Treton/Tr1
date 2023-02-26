def list_even_sort(input_list):
    return_list = []
    return_list2 = []
    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            return_list.append(input_list[i])
        else:
            return_list2.append(input_list[i])
    return_list.extend(return_list2)
    return return_list


print(list_even_sort([1, 2, 3, 8, -3, 0, 6, -8]))
