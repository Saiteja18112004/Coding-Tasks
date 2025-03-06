arr = list(map(int, input().split()))
rev_arr = []
for i in range(len(arr) - 1, -1, -1):
    rev_arr.append(arr[i])
print(rev_arr)
