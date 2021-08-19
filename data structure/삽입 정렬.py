'''
삽입 정렬

정해진 위치에 삽입한다고 해서 삽입 정렬
정렬 범위가 점점 늘어난다
최소값이 발견되면 뒤->앞으로 순차적으로 비교를 하면서 swap한다
'''

import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    print(arr)

start = time.time()
insertion_sort([5,4,3,2,1])
print(f"time : {time.time() - start}")


spring 물어보기;