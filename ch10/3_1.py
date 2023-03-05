def find_parent(p, x):
  if p[x] != x:
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
paths = []
answers = []

for _ in range(m):
  a, b, cost = list(map(int, input().split()))
  paths.append((cost, a, b))
paths.sort() # 최소비용을 구해야 하니까 비용이 작은거 부터 본다

# print(paths)

for path in paths:
  cost, a, b = path
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    answers.append(path)

# print(answers)

answers.pop() # 신장트리에서 젤 긴 엣지 잘라내서 그룹 2개로 분리
sum = 0
for answer in answers:
  sum += answer[0]
print(sum)