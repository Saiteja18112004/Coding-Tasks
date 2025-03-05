s = input()
length = 0
temp = s
for _ in s:
    length += 1
rev = ""
for i in range(length - 1, -1, -1):
    rev += s[i]
if s == rev:
    print("True")
else:
    print("False")