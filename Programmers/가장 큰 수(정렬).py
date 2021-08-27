'''
해결방법
1. 전체 경우의 수를 만든 후, 최대값 반환 -> 시간 초과
2. 값을 반복한 후, 그 전체 값을 기준으로 정렬

배운 지식
1. 경우의 수(수열) : itertools 임포트, permutations 함수 사용 (https://ibit.ly/SMZo)
2. 리스트의 숫자 요소를 합치려면(문자 그대로) 반드시 문자열로 바꾸어야 한다
'''

# 테스트 케이스 성공 but,시간 초과 에러
import itertools
result = list(itertools.permutations([6, 10, 2]))
result
li_ = []
for i in result:
    first = list(map(str, i))
    first
    li_.append("".join(first))
li_

max(li_)

# 위의 에러 수정 but, 똑같이 시간 초과 에러
import itertools

li_ = []
for iter in itertools.permutations([6, 10, 2]):
    string = ""
    for element in iter:
        string += str(element)
    li_.append(string)
li_
max(li_)

# 시간 초과를 없애기 위해 수정해보았지만 똑같이 시간초과 에러
# 수열을 만드는 부분 자체가 시간이 초과 된다는 것을 알게됨
import itertools

def solution(result):
    for iter in itertools.permutations(result):
        pass
    return 0

# 통과 (1272.21ms, 27.3MB)
# 해결 https://ibit.ly/GOld
# 전체를 기준으로 정렬
# 첫번째 값을 기준으로 정렬하는 것만 구현했었다
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    # print(numbers)
    return str(int(''.join(numbers)))


numbers = [5, 76]
li = list(map(str,list(numbers)))

for i in range(len(numbers)):           # 1자리수 변형
    if len(li[i])==1:
        numbers[i]=numbers[i]*11111
numbers

email = []

email = email or ''
email
