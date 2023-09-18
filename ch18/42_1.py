g = int(input()) # 게이트 수
gates = [1] * g
# print(gates)

p = int(input()) # 비행기 수

count = 0
for _ in range(p):
  now = int(input())-1 # 현재 들어온 비행기
  # print('now', now)

  for i in range(now, -1, -1):
    if gates[i] != 0:
      # print('i', i)
      # print(gates)
      gates[i] -= 1
      count += 1
      break
  else: # 도킹할 수 없는 비행기가 나오면 종료
    break

print(count)