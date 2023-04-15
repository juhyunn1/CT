s = input()

sum = 0
result = []
for c in s:
  if c >= 'A' and c <= 'Z':
    result.append(c)
  else:
    sum += int(c)

result.sort()
for r in result:
  print(r, end='')
if sum != 0:
  print(sum)