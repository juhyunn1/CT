def binary(target):
  start = 0
  end = n - 1

  while end >= start:
    mid = (start + end) // 2

    if target > have[mid]:
      start = mid + 1
    elif target < have[mid]:
      end = mid - 1
    else:
      return 'yes'
  return 'no'


n = int(input())
have = list(map(int, input().split()))

m = int(input())
want = list(map(int, input().split()))

for w in want:
  print(binary(w))