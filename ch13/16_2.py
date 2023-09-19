from collections import deque
import copy

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

      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 0:
        arr[nx][ny] = 2
        q.append((nx, ny))
        visited[nx][ny] = True


def makeWall(arr, count):
  global answer

  if count == 3:
    # print(arr)
    lab = copy.deepcopy(arr)

    visited = [[False] * m for _ in range(n)]

    for a in range(n):
      for b in range(m):
        if lab[a][b] == 2:
          bfs(lab, a, b, visited)

    temp = 0
    for row in lab:
      temp += row.count(0)
    # print(temp)
    answer = max(answer, temp)
    return

  for i in range(n):
    for j in range(m):
      if arr[i][j] == 0: # 빈공간이면
        arr[i][j] = 1 # 벽으로
        makeWall(arr, count+1)
        arr[i][j] = 0

n, m = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))
print(arr)

answer = 0

makeWall(arr, 0)

print(answer)