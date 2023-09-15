n = int(input())
m = int(input())

city = [[int(1e9)] * (n+1) for _ in range(n+1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  city[a][b] = min(city[a][b], c) # 작은 값으로 비용 갱신

print(city)

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i == j: # 출발지와 목적지가 같은 경우는
        city[i][j] = 0 # 없다
        continue
      city[i][j] = min(city[i][j], city[i][k]+city[k][j])

for temp in city[1:]:
  print(*temp[1:])