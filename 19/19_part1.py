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


def check_part(part, target):
  if target == 'R':
    return False
  if target == 'A':
    return True

  rules, default_target = workflows_dict[target]

  for category, sign, num, target in rules:
    if sign == '<':
      if part[category] < num:
        return check_part(part, target)
    elif sign == '>':
      if part[category] > num:
        return check_part(part, target)
  
  return check_part(part, default_target)


with open('19.txt', 'r') as f:
  inp = f.read().splitlines()
  index_of_empty_string = inp.index('')
  workflows = inp[:index_of_empty_string]
  parts = inp[index_of_empty_string + 1:]

workflows_dict, parts_list = process_data(workflows, parts)

res = 0

for part in parts_list:
  if check_part(part, 'in'):
    res += sum(part.values())

print(res)
