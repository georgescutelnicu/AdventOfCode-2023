from  math import lcm

def steps(node):
  i = 0
  count = 0
  while not node.endswith('Z'):
    if directions[i] == 'R':
      node = graph[node].split(', ')[1]
    else:
      node = graph[node].split(', ')[0]

    i+=1
    if i == len(directions):
      i = 0
    count += 1

  return count


with open('8.txt', 'r') as f:
  inp = [line.strip() for line in f.readlines()]
  destinations = inp[2:]
  directions = inp[0]

  graph = {}
  
  for dest in destinations:
    position, target = dest.split(' = ')
    graph[position] = target[1:-1]

  filtered_graph = {key: value for key, value in graph.items() if key[-1] == 'A'}

  cycles = []

  for node in filtered_graph:
    cycles.append(steps(node))

  print(lcm(*cycles))
  
