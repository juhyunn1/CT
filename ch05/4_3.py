from collections import deque

def bfs(arr, sx, sy, visited):
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  q = deque([(sx, sy)])
  visited[sx][sy] = True

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
        if not visited[nx][ny]:
          arr[nx][ny] = arr[x][y]+1
          q.append((nx, ny))
          visited[nx][ny] = True


n, m = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(map(int, input())))
print(arr)

visited = [[False] * m for _ in range(n)]

bfs(arr, 0, 0, visited)

print(arr)
print(arr[n-1][m-1])
