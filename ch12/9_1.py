def solution(s):
  answer = len(s)
  compressed = ''

  for unit in range(1, len(s) // 2 + 1):
    count = 1
    prev = s[0:unit]

    for i in range(unit, len(s), unit):
      if prev == s[i:i + unit]:
        count += 1
      else:
        if count > 1:
          compressed += str(count)
        compressed += prev
        count = 1
        prev = s[i:i + unit]
    else:  # 뒤에 남았을 때
      if count > 1:
        compressed += str(count)
      compressed += prev
    # print(unit, compressed)
    answer = min(len(compressed), answer)
    compressed = ''  # 압축 결과 초기화

  return answer