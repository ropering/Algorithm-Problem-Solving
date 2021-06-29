'''
소인수분해 알고리즘(파이썬)
Date : 21.06.65
'''
print("소인수분해할 숫자를 입력하세요 : ")
n = int(input())
li = []

for i in range(2, n+1):
  while n % i == 0:
    n = n / i
    li.append(i)

print(li)