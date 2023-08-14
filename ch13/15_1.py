from collections import deque

n, m, k, x = map(int, input().split())

visited = [False] * (n+1)  # 방문여부
# print(visited)

connected = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  connected[a].append(b)

q = deque([(x, 0)]) # 출발점 큐에 넣고
visited[x] = True # 방문처리

answer = []
while q:
  now, cost = q.popleft()
  if cost == k: # 거리가 k와 같으면
    answer.append(now) # 정답에 넣는다

  for next in connected[now]: # 연결된 것 중에
    if not visited[next]: # 방문하지 않았으면
      q.append((next, cost+1)) # 큐에 넣고
      visited[next] = True # 방문처리

if answer: # answer이 존재하면
  answer.sort() # 정렬해서
  for ele in answer: # 하나씩
    print(ele, end=' ') # 출력
else:
  print(-1)