def solution(s):
    answer = []
    words = s.split(' ')
    for word in words:
        word = list(word)
        i = 1
        for i in range(len(word)):
            if i%2 == 0:
                word[i] = word[i].upper()
            else:
                word[i] = word[i].lower()
        word = ''.join(s for s in word)
        answer.append(word)
    answer = ' '.join(s for s in answer)
    return answer

print(solution("try hello world"))