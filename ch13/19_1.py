def cal(a, b, op): # 계산
  if op == 0:
    return a+b
  elif op == 1:
    return a-b
  elif op == 2:
    return a*b
  else:
    if a < 0: # 앞에가 음수면
      return (a*-1//b)*-1
    return a//b


def dfs(n, nums, opCount, idx, result, temp):
  global min_answer
  global max_answer
  # global arr

  if idx == n-1: # 계산이 끝난 경우
    # if result > answer:
    #   arr = temp
    min_answer = min(min_answer, result) # 최소값 갱신
    max_answer = max(max_answer, result) # 최대값 갱신
    return

  for i in range(4): # 연산자 4개에 대해
    if opCount[i] != 0: # 사용할 수 있는 연산자이면
      opCount[i] -= 1 # 사용하고
      dfs(n, nums, opCount, idx+1, cal(result, nums[idx+1], i), temp+[i]) # 재귀적으로 다음으로, idx는 계산 횟수, temp는 연산자 순서를 보관하는 배열
      opCount[i] += 1 # 복구


n = int(input())
nums = list(map(int, input().split()))

opCount = list(map(int, input().split()))

min_answer = int(1e9)
max_answer = 0
# arr = []

dfs(n, nums, opCount, 0, nums[0], [])
print(max_answer)
print(min_answer)
# print(arr)