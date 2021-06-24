'''첫번째(오류)'''
def solution(left, right):
    count = 0
    sum_ = 0
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
                if count % 2 == 0:
                    sum_ += i
    return sum_

'''두번째(해결)'''
# 소수 % 소수의 제곱근 == 0이다!!
def solution(left, right):
    sum_ = 0
    for i in range(left, right+1):
        if i % (i**0.5) == 0:
            sum_ -= i
        else:
            sum_ += i
    return sum_

'''세번째(업그레이드)'''
def solution(left, right):
    sum_ = 0
    for i in range(left, right+1):
        sum_ = (sum_ - i) if (i % (i**0.5) == 0) else (sum_ + i)
    return sum_