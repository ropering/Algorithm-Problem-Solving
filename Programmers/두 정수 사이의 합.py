def solution(a, b):
    sum_ : int = 0
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        sum_ += i
    return sum_