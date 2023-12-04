def check_for_asterisk(i, j, n):
  if data[i][j] == '*':
    l[i][j].append(n)

res = 0
gear_ratio_res = 0

with open('3.txt', 'r') as f:
  data = [[c for c in line.strip()] for line in f]

  size = len(data)

  l = [[[] for j in range(size) ] for i in range(size)]

  for i, row in enumerate(data):
    j = 0

    while j < size:
      start = j
      num = ''

      while j < size and row[j].isdigit():
        num += row[j]
        j += 1

      if num == '':
        j += 1
        continue

      num = int(num)

      if (0 <= i < size and 0 <= start-1 < size):
        if (data[i][start-1] != ".") and not (data[i][start-1].isdigit()):
          res += num
          check_for_asterisk(i, start-1, num)
          continue

      if (0 <= i < size and 0 <= j < size):
        if (data[i][j] != ".") and not (data[i][j].isdigit()):
          res += num
          check_for_asterisk(i, j, num)
          continue

      for k in range(start-1, j+1):
        if (0 <= i-1 < size and 0 <= k < size):
          if (data[i-1][k] != ".") and not (data[i-1][k].isdigit()):
            res += num
            check_for_asterisk(i-1, k, num)
            continue

        if (0 <= i+1 < size and 0 <= k < size):
          if (data[i+1][k] != ".") and not (data[i+1][k].isdigit()):
            res += num
            check_for_asterisk(i+1, k, num)
            continue

  for r in l:
    for c in r:
      if len(c) == 2:
        gear_ratio_res += (c[0] * c[1])

print(res)
print(gear_ratio_res)

# Credits:
# https://github.com/womogenes/AoC-2023-Solutions/
