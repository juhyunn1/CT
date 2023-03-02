def find_parent(p, x):
  if p[x] != x: # 루트노드가 아니면
    p[x] = find_parent(p, p[x])
  return p[x]


def union_parent(p, a, b):
  a = find_parent(p, a)
  b = find_parent(p, b)
  if a < b:
    p[b] = a
  else:
    p[a] = b


n, m = map(int, input().split())
parent = []
for i in range(n + 1): # 부모를 자기로 초기화
  parent.append(i)
answers = []

for _ in range(m):
  op, a, b = list(map(int, input().split()))

  if op == 0:
    union_parent(parent, a, b)
  elif op == 1:
    if find_parent(parent, a) == find_parent(parent, b):
      answers.append('YES')
    else:
      answers.append('NO')

for answer in answers:
  print(answer)