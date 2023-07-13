def binary_search(have, start, end, target):
  while start <= end:
    mid = (start + end) // 2
    # print(mid)

    if have[mid] == target:
      return 'yes'
    elif have[mid] < target:
      start = mid + 1
    else:
      end = start + 1

  return 'no'

n = int(input())
have = list(map(int, input().split()))
have.sort()

m = int(input())
find = list(map(int, input().split()))

answer = ''
for ele in find:
  answer += binary_search(have, 0, n, ele) + ' '
print(answer)