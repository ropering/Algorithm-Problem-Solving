def combine(one, two):
    return (one + (two * 2))

def solution(scoville, K):
    count = 0
    comparison = [K]*len(scoville)
    scoville.sort()
    while (scoville[0] < K):
        fir_idx = scoville[0]
        if scoville[0] == scoville[1]:
            sec_idx = scoville[2]
        else:
            sec_idx = scoville[1]
        scoville[:2] = []
        scoville.insert(0, combine(fir_idx, sec_idx))
        
        scoville.sort()
        count += 1
        
        if count > 950: # 테스트 케이스 : 900 - 950번 섞는 케이스도 있음
            return -1
    return count


a = [5,6,7,8]
b = [5,7,1,1]
a+1 >= b
a = [1.1,0.9]
a <= [1,1]
[a[0], a[1]]

import numpy as np
a = np.array([6,7,8,9])
a += 1
a >= 6


c = [5,76,78]
[7]*4


정렬
while 반복문 ㅡ 첫번째 값이 x 미만인 동안
첫번째, 두번째 값 변수에 저장 - 리스트에서 삭제 - 섞은 값 인덱스 0에 추가
카운트 증가
정렬
if 카운트가 일정 이상이면 -1 반환

a = hq.heapify(c)
type(a)

a[:2] = []
a


import heapq as hq

h = []
a = heapify([])
heappush(h, [1])
type(h)
def solution(scoville, k):
    mix_cnt = 0
    while min(scoville) < k:
        scoville.sort()
        try:
            scoville.append(scoville.pop(0) + (scoville.pop(0) * 2))
        except IndexError:
            return -1
        mix_cnt += 1

    return mix_cnt


import heapq

def solution(scoville, k):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    
    count = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except:
            return -1
        count += 1
    return count