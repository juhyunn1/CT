n = int(input())

a = list(map(int, input().split()))
a.sort()

count = 0
result = 0
for i in a:
  count += 1 # 현재 그룹의 인원
  if i <= count:
    result += 1
    count = 0

print(result)