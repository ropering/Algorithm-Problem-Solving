'''
그리디 알고리즘
- 현재 상황에서 가장 좋은 선택을 하는 것
- 나중을 고려하지 않음
'''

# 백준 - 설탕 배달

sugar = int(input())
sugar_bags = [3, 5]

while (True):
    if sugar % 5 == 0:
        count += sugar // 5
        print(count)
        break
    
    sugar -= 3
    count += 1

    if sugar < 0:
        print(-1)
        break


for i in sugar_bags[::-1]:
    print(i)
