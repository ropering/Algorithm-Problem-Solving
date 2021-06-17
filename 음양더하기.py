

def solution(absolutes, signs):
    list_ = []
    sum = 0
    for i in range(len(absolutes)):
        list_.append(absolutes[i]) if signs[i] == True else list_.append(-absolutes[i])
        sum += list_[i]
    return sum
        
def solution(absolutes, signs):
    list_ = []
    sum = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            list_.append(absolutes[i])
        else:
            list_.append(-absolutes[i])
        sum += list_[i]
    return sum