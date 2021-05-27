lower = 100
upper = 2000
for num in range(lower, upper):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum+digit ** 3
        temp = temp//10
if sum == num:
    print(num)