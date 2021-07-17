def solution(nums, n):
    result = ""
    for i in nums:
        if i == " ":
            result += " "
        if ord(i) > 96: #소문자 
            if ord(i) + n > 122:
                result += chr(ord(i) + n - 26)
            else:
                result += chr(ord(i) + n)
        elif ord(i) > 64: # 대문자
            if ord(i) + n > 90:
                result += chr(ord(i) + n - 26)
            else:
                result += chr(ord(i) + n)
    return result