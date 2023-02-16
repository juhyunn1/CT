n, m = map(int, input().split())
sx, sy, sd = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[False] * m for _ in range(n)]

x, y, i = sx, sy, sd
visited[x][y] = True
turn_time = 0
count = 1
while True:
  nx = x+dx[i]
  ny = y+dy[i]

  # if 0 > nx or nx >= n or 0 > ny or ny >= m:
  if 0 <= nx < n and 0 <= ny < m:
    if arr[nx][ny] == 0 and not visited[nx][ny]:
      visited[nx][ny] = True
      x, y = nx, ny
      turn_time = 0
      count += 1
    else:
      turn_time += 1

      if turn_time == 4:
        nx = x-dx[i]
        ny = y-dy[i]

        if arr[nx][ny] == 1:
          break
        else:
          x, y = nx, ny

        turn_time = 0
    i -= 1
    if i == -1:
      i = 3

print(count)
