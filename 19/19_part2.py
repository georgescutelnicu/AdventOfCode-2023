def process_data(workflows, parts):
  workflows_dict = {}
  parts_list = []

  for workflow in workflows:
    name, rules = workflow.split('{')[0], workflow.split('{')[1][:-1].split(',')
    default_target = rules.pop()
    temp = []
    for rule in rules:
      condition, target = rule.split(':')
      category = condition[0]
      sign = condition[1]
      num = condition[2:]
      temp.append((category, sign, int(num), target))
    workflows_dict[name] = (temp, default_target)

  for part in parts:
    temp = {}
    part = part[1:-1].split(',')
    for p in part:
      temp[p.split('=')[0]] = int(p.split('=')[-1])
    parts_list.append(temp)

  return workflows_dict, parts_list


def combinations(ranges, name):
  
  if name == 'R':
    return 0

  elif name == 'A':
    res = 1
    for _range in ranges.values():
      res *= _range[1] - _range[0] + 1
    return res

  else:
    rules, default_target = workflows_dict[name]

    total = 0

    for category, sign, num, target in rules:
      min_range = ranges[category][0]
      max_range = ranges[category][1]

      if sign == '>':
        A_range = (num + 1, max_range)
        R_range = (min_range, num)
      elif sign == '<':
        A_range = (min_range, num - 1)
        R_range = (num, max_range)

      copy_ranges = dict(ranges)
      copy_ranges[category] = A_range
      total += combinations(copy_ranges, target)

      ranges[category] = R_range

    total += combinations(ranges, default_target)

    return total

with open('19.txt', 'r') as f:
  inp = f.read().splitlines()
  index_of_empty_string = inp.index('')
  workflows = inp[:index_of_empty_string]
  parts = inp[index_of_empty_string + 1:]

workflows_dict, parts_list = process_data(workflows, parts)

ranges = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}

res = combinations(ranges, 'in')

print(res)

# Really struggled with this, so i decided to follow HyperNeutrino's explanation
# which can be found here https://www.youtube.com/watch?v=3RwIpUegdU4
