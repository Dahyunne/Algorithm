def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] != ' ':
            number = ord(s[i])
            if number < 91:      #대문자인경우
                number += n
                if number >= 91:
                    number -= 26
            elif number < 123:       #소문자인경우
                number += n
                if number >= 123:
                    number -= 26
            new = chr(number)
            answer += new
        else:
            answer += ' '
    return answer

print(solution("AB",1))