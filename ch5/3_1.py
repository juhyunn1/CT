def dfs(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    # if 0 > nx or nx >= n or 0 > ny or ny >= m or arr[nx][ny] == '1':
    #     return
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '0':  # 다음 좌표가 범위 안에 있고 얼음일 때
      arr[nx][ny] = '1'  # 방문처리
      dfs(nx, ny)
    else:  # 다음 좌표가 범위 밖에 있거나 틀일 때
      continue  # 넘어감
  return  # 다 네 방향 다 보고 return


n, m = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(input()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[False] * m for _ in range(n)]
# print(arr)
count = 0
for i in range(n):
  for j in range(m):
    if arr[i][j] == '0':
      arr[i][j] = '1'
      dfs(i, j)
      # print(i, j, arr)
      count += 1

print(count)

