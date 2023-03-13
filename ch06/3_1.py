n = int(input())

dic = {}
for _ in range(n):
  a, b = input().split()
  dic[int(b)] = a

dic = sorted(dic.items())
for k, v in dic:
  print(v, end=' ')