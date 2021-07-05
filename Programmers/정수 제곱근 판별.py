def solution(n):
    return -1 if n % (n**0.5) != 0 else ((n**0.5) + 1) ** 2