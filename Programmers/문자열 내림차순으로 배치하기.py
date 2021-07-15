def solution(s):
    arr = list(s)
    for i in range(len(arr)):
        for j in range(len(arr) -1 -i): # bubble sort
            if ord(arr[j]) < ord(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return "".join(arr)