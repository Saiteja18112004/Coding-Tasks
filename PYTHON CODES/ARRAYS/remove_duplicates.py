arr = list(map(int, input().split()))
unique = []
for num in arr:
    if num not in unique:
        unique.append(num)
print(unique)
