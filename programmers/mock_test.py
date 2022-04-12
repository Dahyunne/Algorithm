def solution(answers):
    answer = []
    supo1 = [0, 1, 2, 3, 4, 5]
    supo2 = [0, 2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [0, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    suposcore1 = 0
    suposcore2 = 0
    suposcore3 = 0

    for i in range(len(answers)):
        #print(answers[i],supo1[i%5+1 if i%5+1 != 0 else 5], supo2[i%8+1 if i%8+1 != 0 else 8],supo3[i%9+1 if i%9+1 != 0 else 9])
        if answers[i] == supo1[i%5+1 if i%5+1 != 0 else 5]:
            suposcore1 += 1
        if answers[i] == supo2[i%8+1 if i%8+1 != 0 else 8]:
            suposcore2 += 1
        if answers[i] == supo3[i%10+1 if i%10+1 != 0 else 10]:
            suposcore3 += 1
    scores = [suposcore1, suposcore2, suposcore3]
        
    for i in range(3):
        if max(suposcore1, suposcore2, suposcore3) == scores[i]:
            answer.append(i+1)
        
    return answer

print(solution([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]))