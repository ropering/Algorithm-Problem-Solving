def solution(n):
    n = list(str(n))
    for i in range(len(n)):
        n[i] = int(n[i])
    n.reverse()
    return(n)