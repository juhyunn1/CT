from itertools import combinations
import copy

def dfs(arr, sx, sy):
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  for i in range(4): # 4방향 보면서
    nx = sx + dx[i]
    ny = sy + dy[i]

    if 0 <= nx < n and 0 <= ny < m: # arr 안에 있으면서
      if arr[nx][ny] == 0: # 빈 공간이면
        arr[nx][ny] = 2 # 전염시키고
        dfs(arr, nx, ny) # 탐색 다시 실행

  return # 더 할꺼 없으면 함수 종료

n, m = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))
# print(arr)

empty = []
for i in range(n):
  for j in range(m):
    if arr[i][j] == 0:
      empty.append((i, j))

combis = list(combinations(empty, 3))
# print(combis)

answer = 0
for combi in combis: # 하나의 조합에 대해
  temp = copy.deepcopy(arr) # 배열 복사 >> 2차원 배열의 복사는 copy.deepcopy 사용

  for x, y in combi:
    temp[x][y] = 1 # 벽 설치

  for i in range(n):
    for j in range(m):
      if temp[i][j] == 2:
        dfs(temp, i, j)
  # print(temp)

  safe = 0
  for t in temp:
    safe += t.count(0)
  else:
    answer = max(answer, safe)

print(answer)