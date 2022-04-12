def solution(d, budget):
    d = sorted(d)
    buy = []
    for i in d:
        buy.append(i)
        if sum(buy) > budget:
            buy.pop()
            break
    return len(buy)

print(solution([1,3,2,5,4],9))