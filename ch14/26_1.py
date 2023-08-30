import heapq

n = int(input())

heap = []
for _ in range(n):
  heapq.heappush(heap, int(input()))

answer = 0
# print(len(heap))
while len(heap) > 1:
  a = heapq.heappop(heap)
  b = heapq.heappop(heap)

  heapq.heappush(heap, a+b)
  answer += a+b

print(answer)