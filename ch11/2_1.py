s = input()

result = 0
for i in s:
    i = int(i)
    if i == 0 or i == 1 or result == 0 or result == 1:
        result += i
    else:
        result *= i

print(result)