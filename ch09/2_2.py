n, m = map(int, input().split())

arr = [[int(1e9)] * n for _ in range(n)]
# print(arr)

# 초기 세팅
for i in range(n):
  arr[i][i] = 0

for _ in range(m): # 연결된 거 비용 1로
  tx, ty = map(int, input().split())
  arr[tx-1][ty-1] = 1
  arr[ty-1][tx-1] = 1

x, k = map(int, input().split())

for t in range(n):
  for i in range(n):
    for j in range(n):
      arr[i][j] = min(arr[i][t] + arr[t][j], arr[i][j])

print(arr[0][k-1] + arr[k-1][x-1] if arr[0][k-1] + arr[k-1][x-1] <= int(1e9) else -1) # 앞, 뒤 중 하나가 0인 경우는 X >> arr[0][k-1] == 0, arr[k-1][x-1] == 0은 안따져도 됨
