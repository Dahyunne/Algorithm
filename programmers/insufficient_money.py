def solution(price, money, count):
    sum = 0
    for i in range(count+1):
        sum = sum + (price * i)
    if (money - sum) < 0:
        answer = abs(money - sum)
    else:
        answer = 0
    return answer

print(solution(3, 20, 4))