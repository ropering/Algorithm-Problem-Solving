def binary_search(target, array):
    left = 0
    right = len(array) - 1

    while left <= right:
        pivot = (left + right) // 2
        if target == pivot:
            print("발견")
            return pivot
        elif target < array[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
        print(1)
print(binary_search(10, [1,2,3,4,5,6,7,8,9]))
        