def solution(s):
    ss = list(s)
    ss.sort(reverse = True)
    return ''.join(i for i in ss)

print(solution("AGDgfsdaFASDGa"))