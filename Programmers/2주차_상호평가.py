'''
한단계 풀어갈 때마다 결과를 출력하면서 해나가는게 결국 더 빠른 것 같다

행-열 바꾸는 방법 
    1. scores = list(map(list, zip(*scores)))
    2. score=[ [i[j] for i in scores] for j in range(len(scores))]



'''

def getGrade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else: return 'F'

def solution(scores):
    result = ""
    for row in range(len(scores)):
        li = []
        for column in range(len(scores)):
            li.append(scores[column][row])
        # 유일한 최댓값 or 유일한 최솟값 이면 제거
        if li.count(li[row]) == 1 and (li[row] == max(li) or li[row] == min(li)):
            li.remove(li[row])
        result += getGrade(sum(li) / len(li))
    return result

# 다른 사람 풀이
def solution(scores):
    avgs = []
    score = [ [i[j]] for i in scores] for j in range(len(scores))]
    for idx, i in enumerate(score):
        avg = sum(i); length = len(i)

        if i[idx] == max(i) or i[idx] == min(i):
            if i.count(i[idx]) == 1:
                avg -= i[idx]; length -= 1
        avgs.append(avg/length)
    return "".join([avg >= 90 and "A" or avg >= 80 and "B" or avg >= 70 and "C" or avg>=50 and "D" or "F" for avg in avgs])
                
