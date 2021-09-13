'''
https://ibit.ly/dSFN
https://ibit.ly/5pJE
'''

# def solution(numbers, target):
#     answer_list = [0]
#     for i in numbers:
#         temp = []
#         for j in answer_list:
#             temp.append(j+i)
#             temp.append(j-i)
#         answer_list=temp
#         print(answer_list)
#     return answer_list.count(target)

# solution([1, 1, 1, 1, 1], 3)


def solution(numbers, target):
    print(numbers)
    print(target)
    if numbers == []:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return solution(numbers[1:], target+numbers[0]) + solution(numbers[1:], target-numbers[0])

solution([1, 1, 1, 1, 1], 3)