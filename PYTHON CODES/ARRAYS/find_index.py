arr = list(map(int, input().split()))
target = int(input())
for i in range(len(arr)):
    if arr[i] == target:
        print(i)
        break
