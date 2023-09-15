import heapq

n, m = map(int, input().split())

connected = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  connected[a].append(b)
  connected[b].append(a)

costs = [int(1e9)] * (n+1)
costs[1] = 0 # 출발점은 거리 0

visited = [False] * (n+1)

q = []
heapq.heappush(q, (0, 1))

while q:
  cost, now = heapq.heappop(q)

  if visited[now]: # 방문 했던 노드면
    continue # 넘어간다

  visited[now] = True # 방문처리

  for next in connected[now]:
    temp = costs[now]+1 # 현재 노드까지 거리 + 다음 노드까지 비용

    if temp < costs[next]: # 새로운 값이 기존 값보다 작으면
      costs[next] = temp # 갱신하고
      heapq.heappush(q, (temp, next)) # 큐에 넣는다

print(costs.index(max(costs[1:])), max(costs[1:]), costs.count(max(costs[1:])))