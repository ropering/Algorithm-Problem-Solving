def solution(n):
    solution = set(range(2, n+1))
    for i in range(2, n+1):
        solution -= set(range(i*2, n+1, i))
    return len(solution)