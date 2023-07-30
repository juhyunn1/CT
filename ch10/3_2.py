def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
    # print(parent[x])
  return parent[x]


def union(x, y):
  x = find_parent(parent, x)
  y = find_parent(parent, y)

  if x > y:
    parent[x] = y
  else:
    parent[y] = x


n, m = map(int, input().split())

parent = []
for i in range(n+1):
  parent.append(i) # 부모 자기 자신으로 초기화

edges = []
for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((c, a, b))

edges.sort() # 작은 비용부터 본다
print(edges)

rode = []
for edge in edges:
  cost, node1, node2 = edge

  if find_parent(parent, node1) != find_parent(parent, node2): # 싸이클이 없으면
    rode.append(cost) # 추가하고
    union(node1, node2) # 합친다
  # print(parent)

rode.pop(-1) # 젤 큰 거 짤라내서 마을을 두개로 나눈다

# print(parent)
# print(rode)
print(sum(rode))