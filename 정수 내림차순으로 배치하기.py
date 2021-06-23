def solution(n):
    n = list(str(n))
    result = ""
    for i in sorted(n, reverse=True):
        result += i
    return int(result)