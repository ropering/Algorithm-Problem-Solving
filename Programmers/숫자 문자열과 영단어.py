def solution(s):
    li_ = []
    solution = ""
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    str_ = ""
    for i in range(len(s)):
        str_ += s[i]
        if str_ in words:
            solution += str(words.index(str_))
            str_ = ""
        if str_ in num:
            solution += str_
            str_ = ""
    return int(solution)