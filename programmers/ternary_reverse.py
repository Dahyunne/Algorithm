def solution(n):
    answer = 0
    num = []
    while(True):
        if n < 3:
            num.append(n)
            break
        num.append(n%3)
        n = n//3
    num.reverse()
    for i in range(len(num)):
        answer += num[i]*(3**i)
    return answer

print(solution(45))