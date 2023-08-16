def dfs(x, y):
  arr[x][y] = 1 # 방문처리
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= n or ny < 0 or ny >= m: # 다음이 범위 벗어나면
      continue # 넘어간다
    else: # 다음이 범위 안이고
      if arr[nx][ny] == 0: # 0이면
        dfs(nx, ny) # 다음으로

  return # 종료


n, m = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(map(int, input())))

print(arr)

count = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
  for j in range(m):
    if arr[i][j] == 0: # 0이면
      dfs(i, j) # dfs 탐색시작
      count += 1 # 탐색 끝나면 +1

print(arr)
print(count)