def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_of_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    total_days = 0

    for i in range(a):
        total_days += days[i]
    total_days -= (total_days - b)
    return days_of_week[total_days % 7]

