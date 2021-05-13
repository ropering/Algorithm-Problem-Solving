#역 삼각형 그리기
#직접 한 것!
#20/09/19

def star(num):
    for i in range(num):
        print( ' ' * ( (num-1)-i) + '*' * (i+1))  
        
star(5) 