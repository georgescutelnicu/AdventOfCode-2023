def func(l):
  if all(x == 0 for x in l):
    return 0
  
  l2 = [y - x for x, y in zip(l, l[1:])]
  
  return l[-1] + func(l2)

with open('9.txt', 'r') as f:
  l = [[int(x) for x in line.split()] for line in f]


print(sum(func(line) for line in l))
print(sum(func(line[::-1]) for line in l))
