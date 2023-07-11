from collections import deque

def bfs(sx, sy):
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  q = deque([(sx, sy)])
  visited[sx][sy] = True # 방문처리

  print(q)

  while q:
    px, py = q.popleft() # 현재 좌표

    for i in range(4):
      nx = px + dx[i]
      ny = py + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] == '0':
        continue
      else: # 범위 안이고 1이며
        if not visited[nx][ny]: # 방문안했으면
          visited[nx][ny] = True # 방문처리
          arr[nx][ny] = int(arr[px][py]) + 1
          q.append((nx, ny))


n, m = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(input()))

visited = [[False] * m for _ in range(n)]

print(arr)
print(visited)

bfs(0, 0)

print(arr)
print(visited)
print(arr[n-1][m-1])