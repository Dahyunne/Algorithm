def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        anstr = ''
        a1 = list(format(arr1[i],'b').zfill(n))
        a2 = list(format(arr2[i],'b').zfill(n))
        for j in range(n):
            if a1[j] == '1' or a2[j] == '1':
                anstr += '#'
            else:
                anstr += ' '
        answer.append(anstr)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))