def solution(n):
    result = ""        
    for i in range(1, n+1):
        if i % 2 == 1:
            result += "수"
        else:
            result += "박"
    return result

# join() : 리스트의 요소를 합친다 (문자열로 반환)
# 한 줄에 여러 개의 변수 선언 : 세미콜론(;) 사용
# a, b = "수","박" 도 가능!!!!!!!!!