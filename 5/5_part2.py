
with open('5.txt', 'r') as f:
  almanac = f.read().split('\n\n')


  seeds = [int(seed) for seed in almanac[0].split()[1:]]
  parts = [[list(map(int, line.split())) for line in part.splitlines()[1:]] for part in almanac[1:]]

  locations = []

  for i in range(0, len(seeds), 2):
    seed_pairs = [(seeds[i], seeds[i]+seeds[i+1])]
    res = []

    for part in parts:
      while len(seed_pairs) > 0:
        s, e = seed_pairs.pop()

        for _map in part:
          dest, src, rng = _map
          end_range = src + rng
          offset = dest - src

          if end_range <= s or e <= src:
            continue
          if s < src:
            seed_pairs.append((s, src))
            s = src
          if end_range < e:
            seed_pairs.append((end_range, e))
            e = end_range
          res.append((s+offset, e+offset))
          break

        else:
          res.append((s, e))
      seed_pairs = res
      res = []
    locations += seed_pairs

  print(min(locations)[0])

  # Synedh's solution from the "r/adventofcode"-"2023 Day 5 Solutions" subreddit
  # helped me a lot!
