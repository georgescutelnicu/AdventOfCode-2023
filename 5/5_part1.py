with open('5.txt', 'r') as f:
  almanac = f.read().split('\n\n')
  
  seeds = [int(seed) for seed in almanac[0].split()[1:]]
  parts = [[list(map(int, line.split())) for line in part.splitlines()[1:]] for part in almanac[1:]]

  locations = []

  for seed in seeds:
    loc = seed

    for part in parts:

      for _map in part:
        dest, src, rng = _map
      
        if src <= loc < src+rng:
          loc = dest + (loc-src)
          break

    locations.append(loc)

print(min(locations))
