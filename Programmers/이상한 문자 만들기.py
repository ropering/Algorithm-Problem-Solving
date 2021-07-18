def solution(s):
    solution = ""
    count = 0
    for i in range(len(s)):
        if ord(s[i]) == 32:
            solution += " "
            count = 0
        else:
            if count % 2 == 0:
                solution += s[i].upper()
                count += 1
            else:
                solution += s[i].lower()
                count += 1
    return solution