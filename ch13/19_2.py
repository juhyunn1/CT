def cal(a, b, op):
  if op == 0:
    return a+b
  elif op == 1:
    return a-b
  elif op == 2:
    return a*b
  else:
    if a < 0:
      return (a*-1//b)*-1
    else:
      return a//b


def dfs(nums, ops, result, now):
  global max_answer
  global min_answer

  if now == len(nums):
    # print(result)
    # print(ops)
    max_answer = max(max_answer, result)
    min_answer = min(min_answer, result)
    return

  # for ni in range(now, len(nums)): # 이게 들어가면 두번째 부터 숫자의 순서도 랜덤인 경우
  for oi, op in enumerate(ops):
    if op != 0:
      ops[oi] -= 1 # 연산자 사용하고
      # print(result)
      dfs(nums, ops, cal(result, nums[now], oi), now+1) # 계산
      ops[oi] += 1 # 복구


n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split())) # +, -, *, /

max_answer = 0
min_answer = int(1e9)
dfs(nums, ops, nums[0], 1)

print(max_answer)
print(min_answer)
