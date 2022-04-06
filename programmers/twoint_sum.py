def solution(a, b):
    array = []
    if a>b:
        b, a = a, b
    for i in range(a, b+1, 1):
        array.append(i)
    return sum(array)

print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))

#특정 상황에서 시간이 엄청 오래 걸린다. 개선 방안 생각 필요할듯