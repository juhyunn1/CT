import heapq

def search(arr, costs, visited):
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  q = []
  heapq.heappush(q, (costs[0][0], 0, 0))

  while q:
    cost, x, y = heapq.heappop(q) # 꺼낸다

    if visited[x][y]: # 현재 노드가 방문한 노드면
      continue # 넘어간다

    visited[x][y] = True # 방문 안했으면 방문처리

    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0 <= nx < n and 0 <= ny < n:
        temp = costs[x][y]+arr[nx][ny]

        if costs[nx][ny] > temp: # 갱신될 값이 더 작은 경우에만
          heapq.heappush(q, (temp, nx, ny)) # 큐에 넣고
          costs[nx][ny] = temp # 갱신
          print(costs)


n = int(input())

arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

costs = [[int(1e9)] * n for _ in range(n)]
costs[0][0] = arr[0][0]

visited = [[False] * n for _ in range(n)]

search(arr, costs, visited)

print(costs[n-1][n-1])