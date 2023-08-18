from collections import deque

def bfs(n, k, target):
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  q = deque()

  for i in range(1, k+1): # 바이러스 번호 순으로 큐에 넣는다 << 한 싸이클에 바이러스 번호가 1~k인 거 다 1칸씩 확장 한다
    for r in range(n):
      for c in range(n):
        if arr[r][c] == i:
          q.append((r, c, i, 0)) # x좌표, y좌표, 바이러스 번호, 싸아클 인덱스
  print(q)

  while q:
    x, y, num, idx = q.popleft()
    print(f'now: {x, y} num: {num}')

    if idx == target: # 한 싸이클이 끝났으면
      break # 종료

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n: # 범위 안에 있고
        print(f'next: {nx, ny} value: {arr[nx][ny]}')
        if arr[nx][ny] == 0: # 바이러스가 없는 칸이면
          arr[nx][ny] = num # 현재 번호로 전염시키고
          q.append((nx, ny, num, idx+1)) # 큐에 추가, 싸이클 인덱스는 +1

    print(f'{q}')
    print(arr)


n, k = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

bfs(n, k, s)
print(arr[x-1][y-1])
