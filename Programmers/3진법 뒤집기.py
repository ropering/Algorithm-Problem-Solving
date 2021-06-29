def solution(n):
    li_one = []
    sum_ = 0
    index = 0
    while True:
        li_one.append(n % 3)
        n = n // 3
        if n == 0:
            break
    for i in range(len(li_one)-1, -1, -1):
        sum_ += li_one[index] * (3 ** i)
        index += 1
    return sum_