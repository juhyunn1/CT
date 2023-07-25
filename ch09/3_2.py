import heapq

n, m, c = map(int, input().split())

connected = [[] for _ in range(n)]
for _ in range(m):
  x, y, z = map(int, input().split())
  connected[x-1].append((y-1, z)) # 각 노드에 연결된 노드와 비용을 저장

distance = [int(1e9)] * n # 각 노드까지의 최소 거리 저장
visited = [False] * n # 각 노드의 방문 여부

q = []
heapq.heappush(q, (0, c-1)) # 시작 노드 우선순위 큐에 넣는다
distance[c-1] = 0 # 시작 노드까지의 거리는 0
while q:
  cost, now = heapq.heappop(q)
  visited[now] = True # 방문 처리

  for next, next_cost in connected[now]: # 지금 노드와 연결된 노드 중에서
    distance[next] = min(distance[now]+next_cost, distance[next]) # 비용 갱신

    if not visited[next]: # 방문하지 않은 노드라면
      heapq.heappush(q, (next_cost, next)) # 우선순위 큐에 넣는다


print(distance)

count = 0
time = 0
for ele in distance:
  if ele != 0 and ele != int(1e9):
    count += 1
    time = max(time, ele)

print(f'{count} {time}')