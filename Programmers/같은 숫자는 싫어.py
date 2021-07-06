def solution(arr):
    var = arr[0]
    li = []
    for i in range(1, len(arr)):
        if var == arr[i]:
            li.append(i) 
        else :
            var = arr[i]
    for i in li:
        arr[i] = -1
    while -1 in arr:
        arr.remove(-1)
    return arr   