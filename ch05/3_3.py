def dfs(arr, sx, sy):
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  for i in range(4):
    nx = sx+dx[i]
    ny = sy+dy[i]

    if 0 <= nx < n and 0 <= ny < m: # 범위 안에 있고
      if arr[nx][ny] == '0': # 얼음인 경우
        arr[nx][ny] = '1' # 채우고
        dfs(arr, nx, ny) # 다음에서 다시 실행


n, m = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(input()))
# print(arr)

answer = 0

for i in range(n):
  for j in range(m):
    if arr[i][j] == '0': # 얼음이면
      arr[i][j] = '1' # 채우고
      dfs(arr, i, j) # 확인
      # print(arr)
      answer += 1 # 다 변환한 후 카운트 +1

print(answer)