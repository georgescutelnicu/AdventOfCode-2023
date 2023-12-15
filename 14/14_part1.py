char_mapping = {'O': 0, '#': 1, '.': -1}

with open('14.txt', 'r') as f:
  grid = f.read().splitlines()
  grid_integers = [[char_mapping[char] for char in row] for row in grid]

for i in range(1, len(grid_integers)):
  for j in range(len(grid_integers[0])):
    if grid_integers[i][j] == 0:
      idx = i
      while idx != 0 and grid_integers[idx-1][j] == -1:
        grid_integers[idx][j], grid_integers[idx-1][j] = grid_integers[idx-1][j], grid_integers[idx][j]
        idx -= 1

res = 0
count = len(grid_integers)

for row in grid_integers:
  s = sum(1 for r in row if r == 0)
  res += count * s
  count -= 1
  
print(res)
