from collections import deque

def bfs():
  while q:
    x, y = q.popleft() # 꺼내서
    visited[x][y] = True # 방문처리

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # if 0 > nx or nx >= n or 0 > ny or ny >= m or arr[nx][ny] == '1':
      #   return
      if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != '0' and not visited[nx][ny]: # 다음 좌표가 범위 안에 있고 길일 때
        arr[nx][ny] = str(int(arr[x][y]) + 1)
        q.append((nx, ny)) # 큐에 넣는다
      else: # 다음 좌표가 범위 밖에 있거나 벽일 때
        continue # 넘어감


n, m = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(input()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visited = [[False] * m for _ in range(n)]
# print(arr)

q = deque()
q.append((0, 0))
bfs()

print(arr, arr[n-1][m-1])

