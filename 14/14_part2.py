def north(grid):
  for i in range(1, len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 0:
        idx = i
        while idx != 0 and grid[idx-1][j] == -1:
          grid[idx][j], grid[idx-1][j] = grid[idx-1][j], grid[idx][j]
          idx -= 1

def south(grid):
  for i in range(len(grid)-2, -1, -1):
    for j in range(len(grid[0])):
      if grid[i][j] == 0:
        idx = i
        while idx != len(grid)-1 and grid[idx+1][j] == -1:
          grid[idx][j], grid[idx+1][j] = grid[idx+1][j], grid[idx][j]
          idx += 1

def east(grid):
  for i in range(len(grid)):
    for j in range(len(grid[0])-2, -1, -1):
      if grid[i][j] == 0:
        idx = j
        while idx != len(grid[0])-1 and grid[i][idx+1] == -1:
          grid[i][idx], grid[i][idx+1] = grid[i][idx+1], grid[i][idx]
          idx += 1

def west(grid):
  for i in range(len(grid)):
    for j in range(1, len(grid[0])):
      if grid[i][j] == 0:
        idx = j
        while idx != 0 and grid[i][idx-1] == -1:
          grid[i][idx], grid[i][idx-1] = grid[i][idx-1], grid[i][idx]
          idx -= 1


char_mapping = {'O': 0, '#': 1, '.': -1}

with open('14.txt', 'r') as f:
  grid = f.read().splitlines()
  grid_integers = [[char_mapping[char] for char in row] for row in grid]

cycles = 1000000000
grid_offset = set()
cycle_offset = 0
grid_cycle = set()
cycle_len = 0

while True:
  cycle_offset += 1
  north(grid_integers)
  west(grid_integers)
  south(grid_integers)
  east(grid_integers)
  if tuple(map(tuple, grid_integers)) in grid_offset:
    break
  grid_offset.add(tuple(map(tuple, grid_integers)))

while True:
  cycle_len += 1
  north(grid_integers)
  west(grid_integers)
  south(grid_integers)
  east(grid_integers)
  if tuple(map(tuple, grid_integers)) in grid_cycle:
    break
  grid_cycle.add(tuple(map(tuple, grid_integers)))


where_is_the_cycle = (cycles - cycle_offset-1) % (cycle_len-1)

for cycle in range(where_is_the_cycle):
  north(grid_integers)
  west(grid_integers)
  south(grid_integers)
  east(grid_integers)

res = 0
count = len(grid_integers)

for row in grid_integers:
  s = sum(1 for r in row if r == 0)
  res += count * s
  count -= 1

print(res)
