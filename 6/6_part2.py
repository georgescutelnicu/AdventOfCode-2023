with open('6.txt', 'r') as f:
  txt = f.readlines()
  
  time = [int(t) for t in txt[0].split()[1:]]
  dist = [int(d) for d in txt[1].split()[1:]]
  
  time = int(''.join([str(t) for t in time]))
  dist = int(''.join([str(d) for d in dist]))

  res = 1

  for t, d in zip([time], [dist]):
    ways = 0
    for i in range(int(t)+1):
      if i * (t-i) > d:
        ways += 1
    res *= ways

print(res)
