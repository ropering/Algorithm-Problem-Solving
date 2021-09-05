def solution(n, lost, reserve):
    _lost = []
    _reserve = []

    for i in lost:
        if i not in reserve:
            _lost.append(i)
    for i in reserve:
        if i not in lost:
            _reserve.append(i)
    
    for i in _reserve: # reserve 대신 lost를 넣으면 문제가 생길 수 있다 (없애지 않았기 때문)
        f = i - 1
        b = i + 1

        if f in _lost:
            _lost.remove(f)
        if b in _lost:
            _lost.remove(b)
    return n - len(_lost)


print(solution(5, [2, 3, 4], [1, 2, 3]))

'''나의 풀이'''
def solution(n, lost, reserve):
    result = n - len(lost)
    
    for i in lost: # 도난 당한 사람 == 여분 가지고 있는 사람 경우 / 12번 해결
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            result += 1
            
    lost.sort() # 13, 18 해결, 5 실패 추가 / 배열이 오름차순이 아닐 때
    reserve.sort() # 5번 해결 -> 중복 제거 후 정렬하니 해결
            
    for i in lost:
        for j in reserve:
            if i == j:
                reserve.remove(j)
                result += 1
                break
            if i - 1 == j:
                reserve.remove(j)
                result += 1
                break
            if i + 1 == j:
                reserve.remove(j)
                result += 1
                break
    return result