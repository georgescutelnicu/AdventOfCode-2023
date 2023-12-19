def get_coords(directions, steps):
  coords = [(0, 0)]
  boundary = 0
  for d, s in zip(directions, steps):
    row, col = coords[-1]
    if d == 'L':
      _row = 0
      _col = -1
    elif d == 'R':
      _row = 0
      _col = 1
    elif d == 'U':
      _row = -1
      _col = 0
    elif d == 'D':
      _row = 1
      _col = 0

    boundary += s
    coords.append((row + _row * s, col + _col * s))

  return coords, boundary


def shoelace_formula(coords):
  l = len(coords)
  area_sum = sum(points[i][0] * (points[i - 1][1] - points[i + 1][1] if i + 1 < l else points[0][1]) for i in range(l))
  A = abs(area_sum) // 2

  return A


def picks_theorem(shoelace_A, boundary):
  A = shoelace_A + boundary  // 2 + 1

  return A


D = {'0': 'R',
     '1': 'D',
     '2': 'L',
     '3': 'U'}

with open('18.txt', 'r') as f:
  directions, steps, colors = [list(x) for x in zip(*(line.split() for line in f.read().splitlines()))]
  colors = [c[2:-1] for c in colors]
  colors_steps = [int(c[:-1], 16) for c in colors]
  colors_directions = [D[c[-1]] for c in colors]

coords, boundary = get_coords(colors_directions, colors_steps)
res = picks_theorem(shoelace_formula(coords), boundary)

print(res)
