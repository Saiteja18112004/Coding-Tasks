n = int(input())
if n < 2:
    print("False")
else:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("True")
    else:
        print("False")