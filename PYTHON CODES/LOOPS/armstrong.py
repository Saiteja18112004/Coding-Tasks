n = int(input())
temp = n
sum_val = 0
count = 0
temp2 = n
while temp2 > 0:
    count += 1
    temp2 //= 10
while temp > 0:
    digit = temp % 10
    power = 1
    for _ in range(count):
        power *= digit
    sum_val += power
    temp //= 10
if n == sum_val:
    print("True")
else:
    print("False")