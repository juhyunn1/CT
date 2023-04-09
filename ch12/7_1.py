n = int(input())
s = str(n)

l, r = 0, 0
for c in s[:len(s)//2]:
    l += int(c)
for c in s[len(s)//2:]:
    r += int(c)

if l == r:
    print("LUCKY")
else:
    print("READY")