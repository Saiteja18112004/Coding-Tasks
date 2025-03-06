arr = list(map(int, input().split()))
min_val = arr[0]
max_val = arr[0]
for num in arr:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
print(max_val - min_val)
