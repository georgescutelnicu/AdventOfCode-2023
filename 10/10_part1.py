def explore(field, starting_position, loop):
  stack = [(starting_position)]

  while stack:
    r, c = stack.pop()
    if 0 <= r < len(field) and 0 <= c < len(field[r]) and (r, c) not in loop:
      pipe = field[r][c]
      loop.add((r, c))

      if pipe in pipes['up'][0] and r > 0 and field[r - 1][c] in pipes['up'][1]:
        stack.append((r - 1, c))

      if pipe in pipes['down'][0] and r < len(field) - 1 and field[r + 1][c] in pipes['down'][1]:
        stack.append((r + 1, c))

      if pipe in pipes['left'][0] and c > 0 and field[r][c - 1] in pipes['left'][1]:
        stack.append((r, c - 1))

      if pipe in pipes['right'][0] and c < len(field[r]) - 1 and field[r][c + 1] in pipes['right'][1]:
        stack.append((r, c + 1))


pipes = {
    'up': ('S|JL', '|7F'),
    'down': ('S|7F', '|JL'),
    'left': ('S-J7', '-LF'),
    'right': ('S-LF', '-J7')
}

with open('10.txt', 'r') as f:
  field = f.read().splitlines()

starting_position = None

for r, row in enumerate(field):
  for c, col in enumerate(row):
    if col == "S":
      starting_position = (r, c)
      break
  if starting_position != None:
    loop = set()
    explore(field, starting_position, loop)
    print(len(loop) // 2)
    break
