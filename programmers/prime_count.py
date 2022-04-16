a = int(input())
isprime = True
if a == 1:
    isprime = False
else:
    for i in range(2, a-1):
        if a % i == 0:
            isprime = False
print(isprime)