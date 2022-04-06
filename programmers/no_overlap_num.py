def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr:
        answer.append(i)
        if answer[-1] == answer[-2]:
            del answer[-1]
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))