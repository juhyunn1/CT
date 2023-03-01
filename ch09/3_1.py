n, m, c = map(int, input().split())

connected = [[] for _ in range(n+1)]
canReach = [False] * (n+1)
time = [1e9] * (n+1)

for _ in range(m): # 연결된 도로 비용 설정
  x, y, z = map(int, input().split()) # x에서 y까지 z만큼의 시간 든다
  connected[x].append([y, z])

result = 0
q = [c]
time[c] = 0
while q:
  now = q.pop(0)
  canReach[now] = True # 방문 처리

  for next, next_time in connected[now]:
    time[next] = min(time[now] + next_time, time[next])
    q.append(next)

print(canReach.count(True)-1, max(time), time)