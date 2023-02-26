def list_string_filter(input_list):
    return_list = []
    for i in range(len(input_list)):
        if isinstance(input_list[i], str):
            return_list.append(input_list[i])
    return return_list


lst = [1, 'sdf', -9.08, [1, 2], 'sdf hd', '']
print(list_string_filter(lst))
