import math
def solution(left, right):
    #약수의 개수가 홀수인 경우 = 어떤 정수의 제곱근
    num_list = []
    for i in range(left, right+1):
        if math.sqrt(i).is_integer():
            num_list.append(-i)
        else:
            num_list.append(i)
    return sum(num_list)

print(solution(13, 17))