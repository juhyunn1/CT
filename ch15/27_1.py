def findLeft(target, arr, start, end):
  while start <= end:
    mid = (start+end) // 2

    if mid == 0 or target > arr[mid-1]: # 찾는 수가 가장 작은 수 일때는 앞에 수가 없다 >> mid == 0으로 확인
      if arr[mid] == target:
        return mid

    if arr[mid] >= target: # 같은 경우에는
      end = mid-1 # 왼쪽으로 이동 << 인덱스의 최소값을 찾는다
    else:
      start = mid+1


def findRight(target, arr, start, end):
  while start <= end:
    mid = (start+end) // 2

    if mid == len(arr)-1 or target < arr[mid+1]:
      if arr[mid] == target:
        return mid

    if arr[mid] > target:
      end = mid-1
    else: # 같은 경우에는
      start = mid+1 # 오른쪽으로 이동 << 인덱스의 최대값을 찾는다


n, x = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
if x > arr[-1]: # 찾는게 없다 << 오름차순이니깐 맨 뒤에 원소와 비교
  answer = -1
else:
  answer = findRight(x, arr, 0, n-1) - findLeft(x, arr, 0, n-1) + 1

print(answer)