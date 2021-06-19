def solution(word):
    length = len(word)
    if length % 2 == 1:
        return word[length // 2]
    else:
        return word[length//2 - 1 : length//2 + 1]