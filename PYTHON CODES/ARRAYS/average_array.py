arr = list(map(int, input().split()))
total = 0
for num in arr:
    total += num
print(total / len(arr))
