def find(arr, start, end):
  while start <= end:
    mid = (start+end) // 2

    if arr[mid] > mid: # 인덱스가 더 작으면
      end = mid-1 # 왼쪽으로
    elif arr[mid] < mid:
      start = mid+1
    else: # 같으면
      return mid

  return -1 # 없으면 -1 리턴


n = int(input())
arr = list(map(int, input().split()))

print(find(arr, 0, n-1))