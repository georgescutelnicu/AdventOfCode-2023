import heapq

with open('17.txt', 'r') as f:
  grid = f.read().splitlines()
  grid = [[int(char) for char in string] for string in grid]

seen = set()
start = (0, 0, 0, 0, 0, 0)
q = [start]
res = 0

while q:
  heat, row, col, _row, _col, steps = heapq.heappop(q)

  if row == len(grid) - 1 and col == len(grid[0]) - 1 and steps > 3:
    res = heat
    break

  if (row, col, _row, _col, steps) not in seen:
    seen.add((row, col, _row, _col, steps))

    next_row = row + _row
    next_col = col + _col

    if (steps < 10) and (0 <= next_row < len(grid)) and (0 <= next_col < len(grid[0])):
      heapq.heappush(q, (heat + grid[next_row][next_col], next_row, next_col, _row, _col, steps + 1))

    if steps > 3 or (_row, _col) == start[3:5]:
      for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if abs(i) != abs(_row) or abs(j) != abs(_col):
          if (0 <= row + i < len(grid)) and (0 <= col + j < len(grid[0])):
            next_row = row + i
            next_col = col + j
            heapq.heappush(q, (heat + grid[next_row][next_col], next_row, next_col, i, j, 1))

print(res)

# In the first attempt i used only a simple list,
# but the code ran very slowly, and also looked pretty ugly.
# This solution is kinda similar to HyperNeutrino's solution since
# i followed his code structure and explanations.
