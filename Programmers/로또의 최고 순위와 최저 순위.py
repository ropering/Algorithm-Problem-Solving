'''
풀이 방법
- for문으로 동일한 값이 존재할 때마다 count를 증가한다 -> best 변수에 저장
- 0의 개수만큼 count를 증가한다 -> worst 변수에 저장
- 변수를 리스트에 넣어 return
'''
# == rank=[6,6,5,4,3,2,1]
def get_score(score):
    if score == 6:
        return 1
    elif score == 5:
        return 2
    elif score == 4:
        return 3
    elif score == 3:
        return 4
    elif score == 2:
        return 5
    else: return 6

def solution(lottos, win_nums):
    erased = lottos.count(0)
    result = 0

    for num in lottos:
        if num in win_nums:
            result += 1
        else:
            result += 0
    
    return [get_score(result + erased), get_score(result)]