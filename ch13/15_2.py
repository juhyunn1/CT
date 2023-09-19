from collections import deque

def bfs(connected, x, visited, distance):
  q = deque([x])
  visited[x] = True

  while q:
    now = q.popleft()

    for next in connected[now]:
      if not visited[next]:
        visited[next] = True
        distance[next] = distance[now]+1
        q.append(next)


n, m, k, x = map(int, input().split())

connected = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  connected[a].append(b)

visited = [False] * (n+1)
distance = [0] * (n+1)

bfs(connected, x, visited, distance)

print(distance)
print(visited)
if k not in distance[1:]:
  print(-1)
else:
  for idx, dis in enumerate(distance[1:]):
    if dis == k:
      print(idx+1, end=' ')
