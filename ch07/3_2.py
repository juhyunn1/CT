def bin_find(start, end, arr, target):
  result = 0

  while end >= start:
    temp = 0
    mid = (end + start) // 2
    # print(f"mid: #{mid}")

    for ele in arr:
      temp += ele - mid if ele >= mid else 0
    else:
      if temp >= target:
        result = max(result, mid)
        start = mid + 1 # mid는 처리한 상태이므로 mid를 제외한 나머지에서 찾는다
      else: # 더 많이 짤라야 한다
        end = mid - 1
    # print(f"start: #{start}, end: #{end}")

  print(result)


n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

bin_find(arr[0], arr[-1], arr, m)