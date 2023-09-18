def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b


n, m = map(int, input().split())

parent = []
for i in range(n+1):
  parent.append(i)

costs = []
ori_cost = 0 # 전체 비용
for _ in range(m):
  x, y, z = map(int, input().split())
  costs.append((z, x, y))
  ori_cost += z
# print(costs)

costs.sort() # 비용 작은거 부터 처리
# print(costs)

min_cost = 0 # 최소 비용
for cost, x, y in costs:
  if find_parent(parent, x) != find_parent(parent, y): # 연결되어 있지 않으면
    min_cost += cost # 비용 더해주고
    union(parent, x, y) # 연결 시킨다

print(ori_cost-min_cost)