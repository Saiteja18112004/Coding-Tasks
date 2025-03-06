arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
common = []
for num in arr1:
    if num in arr2 and num not in common:
        common.append(num)
print(common)
