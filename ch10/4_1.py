from collections import deque
import copy

n = int(input())

num = [0] * (n+1) # 각 과목의 선수과목 수
cost = [0] # 각 과목 수강시간
courses = [[] for _ in range(n+1)] # 해당 과목을 선수과목으로 가지는 과목의 리스트, 인덱스가 선수과목

for i in range(1, n+1):
  a = list(map(int, input().split()))
  cost.append(a[0])
  for j in a[1:-1]:
    num[i] += 1
    courses[j].append(i)


print(courses)
print(cost)
print(num)

result = copy.deepcopy(cost)
q = deque()

for i in range(1, n+1): # 선수과목 없이 들을 수 있는거 다 큐에 넣음
  if num[i] == 0:
    q.append(i)

while q:
  now = q.popleft()
  # result.append(now)

  for i in courses[now]: # now를 선수과목으로 가지는 과목 중에서
    num[i] -= 1 # 해당 과목의 선수과목 수 줄임 << now가 선수과목이었는데 사라졌기 때문
    result[i] = max(result[i], result[now] + cost[i]) # 동시에 여러개의 강의 수강이 가능하므로 더 긴걸 골라서 짧은걸 포함다도록 한다
    print('now={}, i={} : {}'.format(now, i, result))
    if num[i] == 0: # 새롭게 선수과목 없이 들을 수 있는거 큐에 넣음
      q.append(i)

print(result)