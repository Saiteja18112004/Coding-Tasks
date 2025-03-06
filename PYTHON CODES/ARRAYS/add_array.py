n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
total = 0
for num in arr:
    total += num
print(total)