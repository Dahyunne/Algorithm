def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer = s[int(len(s)//2 -1)] + s[int(len(s)//2)]
    else:
        answer = s[len(s)//2]
    return answer
#
#    def solution(s):
#    return s[int(len(s)//2 -1)] + s[int(len(s)//2)] if len(s) % 2 == 0 else s[len(s)//2]
#    삼항 연산자로 한줄로 해결