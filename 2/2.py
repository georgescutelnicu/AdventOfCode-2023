sum_of_id = 0
sum_of_sets = 0

with open('2.txt', 'r') as f:
  for line in f:
    score = 1
    is_possible = True
    cubes_set = {'red': 0, 'green': 0, 'blue': 0}

    _id, balls = line.split(':')

    for balls_pack in balls.split(';'):
      cubes = {'red': 12, 'green': 13, 'blue': 14}

      for ball in balls_pack.split(','):
        count, clr = ball.split()

        cubes[clr] -= int(count)
        cubes_set[clr] = max(cubes_set[clr], int(count))

      if any(val < 0 for val in cubes.values()):
        is_possible = False

    if is_possible:
      sum_of_id += int(_id.split()[-1])

    for val in cubes_set.values():
      score *= val
    sum_of_sets += score

print(sum_of_id)
print(sum_of_sets)
