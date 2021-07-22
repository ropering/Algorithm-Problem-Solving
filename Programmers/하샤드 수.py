def solution(x):
    str_ = str(x)
    sum_ = 0
    for i in range(len(str_)):
        sum_ += int(str_[i])
    if x % sum_ == 0:
        return True
    else:
        return False