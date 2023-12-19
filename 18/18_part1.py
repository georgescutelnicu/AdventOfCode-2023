def visualise_grid_and_get_coords(directions, steps):
  min_height = 0
  max_height = 0
  min_width = 0
  max_width = 0

  width = 0
  height = 0

  for d, s in zip(directions, steps):
    if d == 'L':
      width -= int(s)
    elif d == 'R':
      width += int(s)
    elif d == 'U':
      height -= int(s)
    elif d == 'D':
      height += int(s)

    min_height = min(min_height, height)
    max_height = max(max_height, height)
    min_width = min(min_width, width)
    max_width = max(max_width, width)


  total_height = abs(min_height) + max_height
  total_width = abs(min_width) + max_width

  grid = [['.' for row in range(total_width+1)] for row in range(total_height+1)]

  current_row, current_col = 0 - min_height, 0 - min_width
  coords = [(current_row, current_col)]
  grid[current_row][current_col] = '#'

  for d, s in zip(directions, steps):
    for i in range(1, int(s)+1):

      if d == 'L':
        current_col -= 1

      elif d == 'R':
        current_col += 1

      elif d == 'U':
        current_row -= 1

      elif d == 'D':
        current_row += 1

      grid[current_row][current_col]= '#'

    coords.append((current_row, current_col))

  for row in grid:
    print(row)

  return grid, coords


def shoelace_formula(coords):
  l = len(coords)
  area_sum = sum(coords[i][0] * (coords[i - 1][1] - coords[i + 1][1] if i + 1 < l else coords[0][1]) for i in range(l))
  A = abs(area_sum) // 2

  return A


def picks_theorem(shoelace_A, boundary):
  A = shoelace_A + boundary  // 2 + 1

  return A


with open('18.txt', 'r') as f:
  directions, steps, colors = [list(x) for x in zip(*(line.split() for line in f.read().splitlines()))]

grid, coords = visualise_grid_and_get_coords(directions, steps)
boundary = sum(1 for row in grid for col in row if col == '#')
res = picks_theorem(shoelace_formula(coords), boundary)
print(res)
