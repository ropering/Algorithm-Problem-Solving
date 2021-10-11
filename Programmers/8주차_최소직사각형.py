'''
스스로 풀지 못하였음

규칙성을 파악하면 정말 쉽게 문제를 해결가능하다
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


# 다른 사람 풀이를 보고 만든 나만의 코드
def solution(sizes):
    maxList = []
    minList = []
    for size in sizes:
        maxList.append(max(size))
        minList.append(min(size))
    return max(maxList) * max(minList)
        