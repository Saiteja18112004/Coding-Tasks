arr = list(map(int, input().split()))
target = int(input())
new_arr = []
for num in arr:
    if num != target:
        new_arr.append(num)
print(new_arr)
