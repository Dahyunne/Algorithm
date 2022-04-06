def solution(s):
    answer = 0
    num_dict = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    for i in range(10):
        if num_dict[i] in s:
            s = s.replace(num_dict[i],str(i))
    return int(s)

print(solution("one4seveneight"))
print(solution("23four5six7"))