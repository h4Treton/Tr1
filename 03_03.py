def list_reverse(input_list):
    work_list = input_list
    for i in range(len(work_list) // 2):
        print(work_list[i])
        print(work_list[len(work_list)-i-1])
        work_list[i], work_list[len(work_list)-i-1] = work_list[len(work_list)-i-1], work_list[i]
    return work_list


print(list_reverse([1, 2, 3]))
