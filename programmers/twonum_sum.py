import itertools

def solution(numbers):
    answer = []
    comb = itertools.combinations(numbers, 2)
    for i in comb:
        answer.append(sum(i))
        answer = set(answer)
        answer = sorted(list(answer))
    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))