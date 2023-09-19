from collections import deque

def bfs(arr):
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  q = deque()

  for i in range(1, k+1):
    for r in range(n):
      for c in range(n):
        if arr[r][c] == i:
          q.append((r, c, i, 0)) # 처음에 큐에 넣어준다

  while q:
    x, y, num, count = q.popleft()

    if count == s:
      break

    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0 <= nx < n and 0 <= ny < n:
        if arr[nx][ny] == 0:
          arr[nx][ny] = num
          q.append((nx, ny, num, count+1))


n, k = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

bfs(arr)

print(arr[x-1][y-1])

