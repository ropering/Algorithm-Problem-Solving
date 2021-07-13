def solution(numbers):
    set_ = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if j == len(numbers):
                pass
            set_.add(numbers[i] + numbers[j])
    return sorted(list(set_))