def solve(start):

  def energize(row, col, _row, _col):
    p = (row, col, _row, _col)

    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
      s = grid[row][col]

      if s == '.':
        if (p[:2], directions[p[2:]]) not in seen:
          q.append(p)
          seen.add((p[:2], directions[p[2:]]))

      elif (s == '-' and _row == 0):
        if (p[:2], directions[p[2:]]) not in seen:
          q.append(p)
          seen.add((p[:2], directions[p[2:]]))

      elif (s == '|' and _col == 0):
        if (p[:2], directions[p[2:]]) not in seen:
          q.append(p)
          seen.add((p[:2], directions[p[2:]]))

      elif s == '/':
        p = (row, col, -_col, -_row)
        if (p[:2], directions[p[2:]]) not in seen:
          q.append(p)
          seen.add((p[:2], directions[p[2:]]))

      elif s == '\\':
        p = (row, col, _col, _row)
        if (p[:2], directions[p[2:]]) not in seen:
          q.append(p)
          seen.add((p[:2], directions[p[2:]]))
      
      elif s == '-':
        for i in [(0, 1), (0, -1)]:
          p = (row, col, i[0], i[1])
          if (p[:2], directions[p[2:]]) not in seen:
            q.append(p)
            seen.add((p[:2], directions[p[2:]]))

      elif s == '|':
        for i in [(1, 0), (-1, 0)]:
          p = (row, col, i[0], i[1])
          if (p[:2], directions[p[2:]]) not in seen:
            q.append(p)
            seen.add((p[:2], directions[p[2:]]))
  
  directions = {(-1, 0): 'UP', (1, 0): 'DOWN', (0, -1): 'LEFT', (0, 1): 'RIGHT'}
  q = [start] # start_row, start_col, moving_by_n_rows, moving_by_n_cols
  seen = set()

  while q:
    row, col, _row, _col = q.pop()
    row += _row
    col += _col
    energize(row, col, _row, _col)

  return len(set([coord for coord, direction in seen]))


with open('16.txt', 'r') as f:
  grid = f.read().splitlines()

res = 0

for row in range(len(grid)):
  val1 = solve((row, -1, 0, 1))
  val2 = solve((row, len(grid), 0, -1))
  if res < max(val1, val2):
    res = max(val1, val2)

for col in range(len(grid[0])):
  val1 = solve((-1, col, 1, 0))
  val2 = solve((len(grid[0]), col, -1, 0))
  if res < max(val1, val2):
    res = max(val1, val2)

print(res)
