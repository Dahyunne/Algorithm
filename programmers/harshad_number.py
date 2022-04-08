def solution(x):
    num = []
    for i in str(x):
        num.append(int(i))
    return x % sum(num) == 0

print(solution(10))
print(solution(12))
print(solution(11))