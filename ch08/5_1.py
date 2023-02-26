n, m = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))

d = [1e9] * (m+1)

for ar in arr:
  if ar <= m:
    d[ar] = 1
    for i in range(ar, m+1):
      d[i] = min(d[i], d[i-ar]+1)

result = -1 if d[-1] == 1e9 else d[-1]
print(result)