import re
s = input()
pattern = input()
match = re.match(pattern, s)
print(bool(match))
