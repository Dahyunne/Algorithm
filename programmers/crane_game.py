def solution(board, moves):
    answer = 0
    get = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] == 0:
                continue
            else:
                get.append(board[i][m-1])
                board[i][m-1] = 0
                if len(get)>=2 and get[-1] == get[-2]:
                    get.pop()
                    get.pop()
                    answer += 2
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))