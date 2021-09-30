'''
1. lower(). 사용
2. 아스키코드 값으로 해당 값 아닐 시, 
'''
import re

def solution(data):
    # 1
    data = data.lower()
    # 2
    asc = list(range(97, 123)) + [45, 46, 95] + list(range(48, 58))
    data = ''.join(x for x in data if ord(x) in asc)
    # 3
    data = re.sub('\.\.+', '.', data)
    # 4
    if data[0] == '.':
        data = data[1:]
    if len(data) >= 1 :
        if data[-1] == '.':
            data = data[:-1]
    # 5
    if data == "":
        data += "a"
    # 6
    if len(data) >= 16:
        data = data[:15]
        if data[-1] == '.':
            data = data[:-1]
    # 7
    if len(data) <= 2:
        while len(data) <= 2:
            data += data[-1]
    return data

solution("...!@BaT#*..y.abcdefghijklm")
print("=" * 20)
solution("z-+.^."	)
print("=" * 20)
solution("=.="	)
print("=" * 20)
solution("123_.def"	)
print("=" * 20)
solution("abcdefghijklmn.p"	)

