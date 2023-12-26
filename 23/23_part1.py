with open('23.txt', 'r') as f:
  grid = f.read().splitlines()

seen = set()
q = [(0, 1, 0)] # row, col, steps
res = []

symbols = {
    '.': [(1, 0), (-1, 0), (0, 1), (0, -1)],
    '<': [(0, -1)],
    '>': [(0, 1)],
    'v': [(1, 0)],
    '^': [(-1, 0)]
}

while q:

  row, col, steps = q.pop()

  if row == (len(grid) - 1):
    res.append(steps)
    continue

  seen.add((row, col, steps))
  
  symb = grid[row][col]

  for coord in symbols[symb]:
    r, c = coord
    _row, _col = row + r, col + c

    if (grid[_row][_col] != '#') and (0 <= _row < len(grid)) and (0 <= _col < len(grid[0])):
      if (_row, _col, steps-1) not in seen: # Prevent it to go immediately back
        q.append((_row, _col, steps+1))

print(sorted(res)[-1])

# Worked on my input file(ran in 1 sec) since i didn't have any weirdo loops in
# the grid but i don't expect this to work on every input since this code can 
# step onto the same tile twice, i just prevented it to go immediately back
