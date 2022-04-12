def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    answer = ''
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    if answer == '':
        answer = participant[-1]
    return answer

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]	))