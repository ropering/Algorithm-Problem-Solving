# 최대공약수 알고리즘
# 유클리드 호제법 사용
# 21.06.07
'''
share : 몫
remainder : 나머지
'''

import time

def solution(x, y):
  try:
    share = 1
    count = 0
    while(share != 0):
      share = x//y
      remainder = x%y

      x = y
      y = remainder
      count += 1
  except:
    print(x)
    print(count)

start = time.time()

solution(100000000000000000000000, 94645946494949494949499)

end = time.time()
print(end - start)

