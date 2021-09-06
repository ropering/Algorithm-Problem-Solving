# https://ibit.ly/XakK
'''
배열이 정렬이 안되어 있다 -> 13, 18번 해결
- 4, [2, 4], [1, 3] => 1 이 뒷번호 2에 빌려주고, 3이 뒷번호 4에 빌려주므로 4명 (O)
- 4, [2, 4], [3, 1] => 3 이 앞번호 2에 빌려주고, 1은 뒷번호 2가 이미 있으므로 3명 (X)
- 정렬에서 오류발생할 수 있지 않을까?

잃어버린 사람 == 여분이 있는사람인 경우가 있다
정렬 후 중복제거 / 중복제거 후 정렬 : 결과 차이가 있다 -> 5번 해결
'''
def solution(n, lost, reserve):    
    _lost = [i for i in lost if i not in reserve]
    _reserve = [j for j in reserve if j not in lost]
    _lost.sort()
    _reserve.sort()
    
    for i in _reserve: # reserve 대신 lost를 넣으면 문제가 생길 수 있다 (없애지 않았기 때문)
        f = i - 1
        b = i + 1

        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


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