from itertools import combinations as cb

n = int(input())
coins = list(map(int, input().split()))

# possible = []
# for i in range(1, n+1):
#   for a in cb(coins, i):
#     if sum(a) not in possible:
#       possible.append(sum(a))
#
# for i in range(1, sum(coins)):
#   if i not in possible:
#     print(i)
#     break

coins.sort()

target = 1 # target - 1까지 다 만들 수 있다고 가정, 동전의 금액은 자연수이기에 나올 수 없는 금액의 최소는 1
for coin in coins:
  if target < coin: # target - 1까지 다 만들 수 있다, target == coin이면 단독으로 target 만들 수 있다
    print(target)
    break
  target += coin