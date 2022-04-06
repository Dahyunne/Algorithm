def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    win_nums.sort()
    correct = 0
    zero = 0
    result = []
    for i in lottos:
        if i == 0:
            zero += 1
        else:
            for j in win_nums:
                if i == j:
                    correct += 1
    result.append(correct + zero)
    result.append(correct)
    
    answer.append(7 - result[0])
    answer.append(7 - result[1])
    if answer[0] >= 6:
        answer[0] = 6
    if answer[1] >= 6:
        answer[1] = 6
    
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))