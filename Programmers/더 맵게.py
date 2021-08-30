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