def find_parent(parent, x):
  if parent[x] != x: # 루트될 때 까지
    parent[x] = find_parent(parent, parent[x]) # 부모를 찾는다
  return parent[x] # 루트까지 가면 parent[x] == x이므로 루트 반환


def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a > b:
    parent[a] = b
  else:
    parent[b] = a


n, m = map(int, input().split())

parent = [0]
for i in range(1, n+1):
  parent.append(i) # 자기 자신으로 부모 초기화

for _ in range(m):
  op, a, b = map(int, input().split())
  if op == 0:
    union(parent, a, b) # 합친다
  elif op == 1:
    if find_parent(parent, a) == find_parent(parent, b): # 부모가 같다 = 사이클이 존재
      print('YES')
    else:
      print('NO')