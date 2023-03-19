s = input()

s = s + '1' if s[-1] == '0' else s + '0' # 뒤에 반대되는거 하나 추가

print(min(s.count('01'), s.count('10')))