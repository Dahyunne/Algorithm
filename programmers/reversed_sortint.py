def solution(n):
    ln = list(str(n))
    ln.sort(reverse = True)
    return int(''.join(n for n in ln))

print(solution(1541524))