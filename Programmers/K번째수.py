def solution(array, commands):
    sub_list = []
    main_list = []
    for i in commands:
        sub_list = array[i[0]-1 : i[1]]
        sub_list.sort()
        main_list.append(sub_list[i[2]-1])
    return main_list