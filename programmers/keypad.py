def dist(a, b):
    distance = 0
    for i in range(2):
        distance += abs(a[i]-b[i])
    return distance

def solution(numbers, hand):
    answer = []
    keypad = {1:(1, 1), 2:(1, 2), 3:(1, 3), 4:(2, 1), 5:(2, 2), 6:(2, 3), 7:(3, 1), 8:(3, 2), 9:(3, 3), 0:(4, 2)}
    currentL = (4, 1)
    currentR = (4, 3)
    
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer.append('L')
            currentL = keypad[number]
        elif number == 3 or number == 6 or number == 9:
            answer.append('R')
            currentR = keypad[number]
        else:
            disL = dist(currentL, keypad[number])
            disR = dist(currentR, keypad[number])
            if disL == disR:
                if hand == 'right':
                    answer.append('R')
                    currentR = keypad[number]
                else:
                    answer.append('L')
                    currentL = keypad[number]
            elif disL < disR:
                answer.append('L')
                currentL = keypad[number]
            elif disL > disR:
                answer.append('R')
                currentR = keypad[number]
    
    return ''.join(s for s in answer)

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))