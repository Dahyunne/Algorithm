def solution(x, n):
    answer = []
    num = x
    for _ in range(n):
        answer.append(num)
        num += x
    return answer

print(solution(2,5))