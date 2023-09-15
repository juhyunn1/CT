n, m = map(int, input().split())

arr = [[int(1e9)] * (n+1) for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  arr[a][b] = 1

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i == j: # 자기자신인 경우
        arr[i][j] = int(1e9) # 제외
        continue
      arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

count = [0]
for k in range(1, n+1):
  count.append(n - arr[k][1:].count(int(1e9))) # k에서 출발 = k보다 성적 높다

for i in range(1, n+1):
  for j in range(1, n+1):
    if arr[i][j] != int(1e9): # j로 도착 = j보다 성적 낮다
      count[j] += 1

answer = count.count(n-1) # 값이 n-1인 경우가 자기보다 성적 높고 낮은 경우 모두 아는 경우

print(count)
print(answer)