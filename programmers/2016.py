def solution(a, b):
    answer = ''
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    if a == 1 or a == 4 or a == 7: #1일이 금요일
        answer = day[(b%7)-4]
    elif a == 2 or a == 8: #1일이 월요일
        answer = day [(b%7)-1]
    elif a == 3 or a == 11: #1일이 화요일
        answer = day [(b%7)]
    elif a == 5: #1일이 일요일
        answer = day [(b%7)-2]
    elif a == 6: #1일이 수요일
        answer = day [(b%7)-6]
    elif a == 9 or a == 12: #1일이 목요일
        answer = day [(b%7)-5]
    elif a == 10: #1일이 토요일
        answer = day [(b%7)-3]
        
        
    return answer

print(solution(5, 24))