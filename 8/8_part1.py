with open('8.txt', 'r') as f:
  inp = [line.strip() for line in f.readlines()]
  destinations = inp[2:]
  directions = inp[0]

  graph = {}
  current_node = 'AAA'
  count = 0
  i = 0

  for dest in destinations:
    position, target = dest.split(' = ')
    graph[position] = target[1:-1]

  while current_node != 'ZZZ':
    if directions[i] == 'R':
      current_node = graph[current_node].split(', ')[1]
    else:
      current_node = graph[current_node].split(', ')[0]

    i+=1
    if i == len(directions):
      i = 0

    count+=1

  print(count)
