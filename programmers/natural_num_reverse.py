def solution(n):
    answer = []
    a = list(str(n)[::-1])
    for i in a:
        answer.append(int(i))
    return answer

print(solution(123456789))