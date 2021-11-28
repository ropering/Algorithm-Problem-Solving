
def solution(x, l=[]):
    for i in range(x):
        l.append(i)
        print(l)
    print('=====')
    return None
# 원인은 모르겠지만 해결책
# def solution(x, l=None):
#     if l is None:
#         l = []
#     for i in range(x):
#         l.append(i)
#         print(l)
#     print('=====')

solution(2)        
solution(2, [])
solution(2)
solution(3)
