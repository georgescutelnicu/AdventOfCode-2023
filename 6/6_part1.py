with open('6.txt', 'r') as f:
  txt = f.readlines()
  
  time = [int(t) for t in txt[0].split()[1:]]
  dist = [int(d) for d in txt[1].split()[1:]]

  res = 1

  for t, d in zip(time, dist):
    ways = 0
    for i in range(int(t)+1):
      if i * (t-i) > d:
        ways += 1
    res *= ways

print(res)
