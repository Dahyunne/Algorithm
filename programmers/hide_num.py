import re
def solution(phone_number):
    if len(phone_number) == 4 : return phone_number
    phone_number = re.sub('[0-9]', '*', phone_number, len(phone_number)-4)
    return phone_number

print(solution("01033334444"))
print(solution("027778888"))