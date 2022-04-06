import string
def solution(new_id):
    answer = ''
    answer = new_id.lower() #1단계
    
    symbols = string.punctuation.replace('-', '').replace('_', '').replace('.', '')
    for symbol in symbols:
        answer = answer.replace(symbol, "") #2단계
        
    stack = []
    for s in answer:
        if len(stack) == 0 or len(stack) == 1:
            stack.append(s)
        else:
            if s == stack[-1] and s == '.':
                stack.pop()
                stack.append('.')
            else:
                stack.append(s)
    answer = ''.join(map(str, stack))
    #3단계
    
    answer = answer.lstrip('.').rstrip('.')  #4단계
    
    if len(answer)==0:
        answer = 'a'    #5단계
        
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer.rstrip('.')  #6단계
            
    if len(answer) < 3:
        while True:
            answer = answer + answer[-1]
            if len(answer) == 3: break  #7단계
    return answer
    
print(solution("...!@BaT#*..y.abcdefghijklm",))
print(solution("z-+.^."))