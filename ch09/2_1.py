n, m = map(int, input().split())
arr = [[1e9] * (n+1) for _ in range(n+1)]

for i in range(1, n+1): # 자기 자신으로 가는거 0으로
  for j in range(1, n+1):
    if i == j:
      arr[i][j] = 0

for _ in range(m): # 연결된 도로 비용 설정
  a, b = map(int, input().split())
  arr[a][b] = 1
  arr[b][a] = 1

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      arr[i][j] = min(arr[i][k]+arr[k][j], arr[i][j])

x, k = map(int, input().split())

result = arr[1][k] + arr[k][x]
print(result if result <= 1e9 else -1)