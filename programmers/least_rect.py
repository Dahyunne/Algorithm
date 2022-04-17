def solution(sizes):
    short = []
    long = []
    for i in range(len(sizes)):
        sizes[i].sort()
        short.append(sizes[i][0])
        long.append(sizes[i][1])       
    return max(short)*max(long)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))