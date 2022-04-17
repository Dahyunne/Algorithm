def solution(s):
    answer = True
    pnum = 0
    ynum = 0
    for i in s:
        if i == 'p' or i == 'P':
            pnum += 1
        if i == 'y' or i == 'Y':
            ynum += 1
    return pnum == ynum

print(solution("pyyyyppypp"))