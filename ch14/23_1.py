n = int(input())

arr = []
for _ in range(n):
  name, kor, eng, math = input().split()
  arr.append((int(kor), int(eng), int(math), name))

# 국어 점수 내림차순, 영어 점수 오름차순, 수학 점수 내림차순, 이름 오름차순 정렬
arr.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for ele in arr:
  print(ele[3])