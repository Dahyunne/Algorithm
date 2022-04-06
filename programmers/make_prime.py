import itertools
import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    sums = []
    comb = itertools.combinations(nums, 3)
    for i in comb:
        sums.append(sum(i))
        if is_prime(sums[-1]):
            answer += 1
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))