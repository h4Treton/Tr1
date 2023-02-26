def list_sum_n_el(input_list):
    for i in range(len(input_list)):
        if i == 0:
            k1 = input_list[len(input_list)-1]
            k2 = input_list[i + 1]
        elif i == len(input_list) - 1:
            k1 = input_list[i - 1]
            k2 = input_list[0]
        else:
            k1 = input_list[i - 1]
            k2 = input_list[i + 1]
        print(k1 + k2)
    return None


list_sum_n_el([1, 2, 3, 8, -3, 0, 6, -8])
