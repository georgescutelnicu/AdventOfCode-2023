def search(patterns, multiply=True):
  res = 0
  
  for pattern in patterns:
    for i in range(1, len(pattern)):
      first, second = pattern[:i], pattern[i:]
      l = len(first) if len(first) < len(second) else len(second)
      first, second = list(reversed(first))[:l], second[:l]

      if first == second:
        if multiply:
          res +=  i * 100
        else:
          res += i

  return res


with open('13.txt', 'r') as f:
  patterns = [pattern.splitlines() for pattern in f.read().split("\n\n")]
  transposed_patterns = [[''.join(row) for row in zip(*pattern)] for pattern in patterns]

  res = 0

  res += search(patterns)
  res += search(transposed_patterns, multiply=False)
            
  print(res)
