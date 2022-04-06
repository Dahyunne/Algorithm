def solution(array, commands):
    answer = []
    slice = []
    slicedarray = []
    
    for i in range(len(commands)):
        slice = commands[i]
        slicedarray = array[slice[0]-1:slice[1]]
        k = slice[2] - 1
        slicedarray = sorted(slicedarray)
        answer.append(slicedarray[k])
    
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))