def dfs(arr, routers, count, idx):
  global answer

  if count == c:
    for i in range(1, n):
      answer = min(routers[i]-routers[i-1], answer) # 인접한 최소값 갱신
      return

  if idx == n:
    return

  dfs(arr, routers+[arr[idx]], count+1, idx+1)
  dfs(arr, routers, count, idx+1)


n, c = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(int(input()))

arr.sort() # 정렬

answer = int(1e9)

dfs(arr, [], 0, 0)

print(answer)