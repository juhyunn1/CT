def binary(target):
  global result

  start = 0
  end = max(arr)

  while end >= start:
    mid = (start + end) // 2

    temp = 0
    for ele in arr:
      if ele >= mid:
        temp += ele - mid

    if temp >= target:
      result = mid
      start = mid + 1
    else:
      end = mid - 1


n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
binary(m)
print(result)