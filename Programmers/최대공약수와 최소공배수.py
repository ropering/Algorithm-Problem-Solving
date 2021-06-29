def solution(y, x): 
    mul = x * y
    remainder = int()
    while True:
        if x % y == 0: return [y, mul / y]             
        remainder = x % y
        x = y
        y = remainder