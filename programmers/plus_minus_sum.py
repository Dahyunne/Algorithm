def solution(absolutes, signs):
    array = []
    for i in range(len(absolutes)):
        if not signs[i]:
            array.append(-1 * absolutes[i])
        else:
            array.append(absolutes[i])
    return sum(array)

print(solution([4,7,12],[True,False,True]))
print(solution([1,2,3],[False,False,True]))