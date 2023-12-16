with open('15.txt', 'r') as f:
  inp = f.read().split(',')

res = 0
for seq in inp:
  temp = 0
  for c in seq:
    temp += ord(c)
    temp *= 17
    temp %= 256
  res += temp

print(res)
