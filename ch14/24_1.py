n = int(input())

houses = list(map(int, input().split()))

# cost = int(1e9)
# answer = 0
# for ant in houses:
#   temp = 0
#   for house in houses:
#     temp += abs(ant-house)
#   print(temp)
#
#   if cost > temp:
#     cost = temp
#     answer = ant
#
# print(answer)

houses.sort()
print(houses[(n-1)//2]) # << 짝수일 때 더 앞에 값