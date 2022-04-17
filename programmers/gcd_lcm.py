import math
def solution(n, m):
    return [math.gcd(n, m), n*m//math.gcd(n,m)]

print(solution(3, 12))