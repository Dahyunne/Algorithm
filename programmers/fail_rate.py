def solution(N, stages):
    answer = []
    failrate = []
    
    for i in range(N+1):
        challenge = 0
        fail = 0
        rate = 0
        for j in stages:
            if j > i or j == i:
                challenge += 1
            if j == i:
                fail += 1
        if challenge == 0:
            rate = 0
        else:
            rate = fail/challenge
        failrate.append(rate)
        
    del(failrate[0])
        
    for i in range(N):
        for j in range(N):
            if max(failrate) == failrate[j]:
                answer.append(j+1)
                failrate[j] = -1
                break
            else:
                continue
    
    return answer[0:N]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
print(solution(5, [4, 4, 4, 4, 4]))