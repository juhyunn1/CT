def rotate(before):
  n = len(before)
  m = len(before[0])
  after = [[0] * n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      after[j][n - i - 1] = before[i][j]

  return after


def check(extended, n, m):
  for i in range(n, 2 * n):
    for j in range(m, 2 * m):
      if extended[i][j] != 1:
        return False
  else:
    return True


def solution(key, lock):
  n = len(lock)
  m = len(lock[0])

  extended = [[1] * (3 * m) for _ in range(3 * n)]
  for i in range(n):
    for j in range(m):
      extended[n + i][m + j] = lock[i][j]  # 가운데 lock 대입

  for i in range(1, 2 * n):
    for j in range(1, 2 * m):
      for k in range(4):
        key = rotate(key)
        for r in range(len(key)):
          for c in range(len(key[0])):
            extended[i + r][j + c] += key[r][c]

        if check(extended, n, m):  # 열쇠가 맞으면
          return True

        for r in range(len(key)):
          for c in range(len(key[0])):
            extended[i + r][j + c] -= key[r][c]  # 원상복구

  return False