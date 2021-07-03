def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_of_week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    total_days = 0

    for i in range(a):
        total_days += days[i]
    total_days -= (days[a-1] - b)
    return days_of_week[total_days % 7]