# 참고한 문제
def solution(priorities, location):
    array1 = [c for c in range(len(priorities))] # index 위치 저장 
    array2 = priorities.copy() # 값 저장 (출력되는 값)

    i = 0
    while True:
        if array2[i] < max(array2[i+1:]):
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
        else:
            i += 1

        if array2 == sorted(array2, reverse=True):
            break

    return array1.index(location) + 1


# 통과 (0.87ms, 10.2MB)
# 내가 푼 문제
# 맨 처음 요소가 가장 우선순위가 높다면 삭제하고 다른 리스트에 옮겼다
# 우선순위 값에 따라 값의 이동을 기억하고자 idx, pri2와 같은 인덱스를 담은 변수를 선언하였다
# 그래서 우선순위 값이 이동함에 따라 인덱스 담은 변수도 같이 이동시켰다
def solution(priorities, location):
    arr1 = priorities[:]
    idx1 = [i for i in range(len(priorities))]
    arr2 = []
    idx2 = []

    while len(arr1) != 0:
        if arr1[0] < max(arr1):
            arr1.append(arr1.pop(0))
            idx1.append(idx1.pop(0))
        else:
            arr2.append(arr1.pop(0))
            idx2.append(idx1.pop(0))
            
    return idx2.index(location) + 1
    
print(solution([2, 1, 3, 2], 2)    )















