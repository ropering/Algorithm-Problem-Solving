def solution(nums):
    to_select = len(nums) / 2
    kinds = len(set(nums))
    return to_select if to_select < kinds else kinds