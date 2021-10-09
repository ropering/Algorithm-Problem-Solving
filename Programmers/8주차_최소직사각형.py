'''
스스로 풀지 못하였음
'''


# 상현이가 푼 문제
def solution(sizes):
    hor = []
    vert = []
    for size in sizes:
        hor.append(size[0])
        vert.append(size[1])
    for i in range(len(sizes)):
        if hor[i] > vert[i]:
            hor[i], vert[i] = vert[i], hor[i]
            
    return max(hor) * max(vert)