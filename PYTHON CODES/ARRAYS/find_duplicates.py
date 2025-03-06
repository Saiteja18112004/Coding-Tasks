arr = list(map(int, input().split()))
seen = []
duplicates = []
for num in arr:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    else:
        seen.append(num)
print(duplicates)
