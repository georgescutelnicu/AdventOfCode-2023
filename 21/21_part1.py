from collections import deque

with open('21.txt', 'r') as f:
  grid = f.read().splitlines()

coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
STEPS = 64  
q = deque()

for r, row in enumerate(range(len(grid))):
  for c, col in enumerate(range(len(grid[0]))):
    if grid[r][c] == 'S':
      q.append((r, c))

for s in range(STEPS):

  for _ in range(len(q)):
    row, col = q.popleft()
    
    for coord in coords:
      _row = row + coord[0]
      _col = col + coord[1]

      if 0 <= _row < len(grid) and 0 <= _col < len(grid[0]) and grid[_row][_col] != '#' and (_row, _col) not in q:
        q.append((_row, _col))

print(len(q))
