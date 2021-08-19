# https://www.daleseo.com/sort-selection/

'''
선택 정렬

최소값의 인덱스 변수 생성
내부 for문을 마칠 때마다 위치 swap
'''

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    print(arr)

selection_sort([5,2,6,4,3,4,6,7,8,9,3])
