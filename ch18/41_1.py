def find_parent(parent, x):
  if parent[x] != x: # 루트될 때 까지
    parent[x] = find_parent(parent, parent[x]) # 부모를 찾는다
  return parent[x] # 루트까지 가면 parent[x] == x이므로 루트 반환


def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = parent[a]
  else:
    parent[a] = parent[b]


n, m = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

parent = []
for i in range(n):
  parent.append(i)

for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      union(parent, i, j)

print(parent)

temp = set()
path = list(map(int, input().split()))
for i in range(len(path)-1):
  if parent[path[i]-1] != parent[path[i+1]-1]:
    print("No")
    break
else:
  print("Yes")