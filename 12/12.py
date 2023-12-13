from functools import lru_cache

@lru_cache
def arrangements(group, num):
  result = 0

  if len(group) == 0:
    return 1 if len(num) == 0 else 0

  if len(num) == 0:
    return 0 if "#" in group else 1

  if group[0] == '.':
    return arrangements(group[1:], num)
  
  if group[0] == '?':
    return arrangements(group.replace('?', '.', 1), num)  \
           + arrangements(group.replace('?', '#', 1), num)
    
  if group[0] == '#':
    if num[0] <= len(group) and '.' not in group[:num[0]] and (num[0] == len(group) or group[num[0]] != '#'):
      result += arrangements(group[num[0] + 1:], num[1:])

  return result
      

with open('12.txt', 'r') as f:
  lines = f.read().splitlines()
  groups = [line.split()[0] for line in lines]
  nums = [tuple(map(int, line.split()[1].split(','))) for line in lines]

res1 = 0
res2 = 0

for i in range(len(groups)):
  res1 += arrangements(groups[i], nums[i])
  res2 += arrangements('?'.join([groups[i]]*5), nums[i]*5)

print(res1)
print(res2)


# Really struggled on this problem, shemetz' solution helped me a lot!
# https://github.com/shemetz/advent_of_code_2023/blob/main/day12.py
