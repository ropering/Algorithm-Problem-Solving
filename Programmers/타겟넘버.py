def solution(numbers, target):
    answer_list = [0]
    for i in numbers:
        temp = []
        for j in answer_list:
            temp.append(j+i)
            temp.append(j-i)
        answer_list=temp
        print(answer_list)
    return answer_list.count(target)

solution([1, 1, 1, 1, 1], 3)