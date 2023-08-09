from collections import deque

n = int(input())

cost = [0] # 각 과목을 듣기 위해 필요한 최대시간
pre_course = [[] for _ in range(n+1)] # 특정 과목(인덱스)에 대한 선수과목 목록
visited = [False for _ in range(n+1)] # 방문 여부

for i in range(1, n+1):
  arr = list(map(int, input().split()))
  # print(arr)

  cost.append(arr[0]) # 비용
  for sub in arr[1:-1]: # 선수과목
    pre_course[i].append(sub)

# print(pre)

q = deque()
for i in range(1, n+1):
  if not pre_course[i]: # 선수과목 없으면
    q.append(i) # 큐에 넣고
    visited[i] = True # 방문처리

while q:
  now = q.popleft() # 큐에서 꺼내서

  for i in range(1, n+1):
    if not visited[i]: # 방문하지 않은 과목 중에
      if now in pre_course[i]: # 선수과목 중 now가 있으면
        pre_course[i].remove(now) # 선수과목 목록에서 삭제

      if not pre_course[i]: # 선수과목 없으면
        q.append(i) # 큐에 넣고
        cost[i] = max(cost[now] + cost[i], cost[i]) # 비용 갱신
        visited[i] = True # 방문처리

print(cost[1:])