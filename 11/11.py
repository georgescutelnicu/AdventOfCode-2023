with open('11.txt', 'r') as f:
  field = f.read().splitlines()

res1 = 0
res2 = 0

empty_rows = [r for r, row in enumerate(field) if '#' not in row]
empty_cols = [c for c in range(len(field[0])) if '#' not in [field[r][c] for r in range(len(field))]]
galaxies = [(r, c) for r, row in enumerate(field) for c, col in enumerate(row) if col == "#"]

expansion1 = 2
expansion2 = 1000000


for i, galaxy in enumerate(galaxies):
  for pair in galaxies[i:]:
    min_row, max_row = min(galaxy[0], pair[0]), max(galaxy[0], pair[0])
    min_col, max_col = min(galaxy[1], pair[1]), max(galaxy[1], pair[1])

    for r in range(min_row, max_row):
      res1 += expansion1 if r in empty_rows else 1
      res2 += expansion2 if r in empty_rows else 1
    for c in range(min_col, max_col):
      res1 += expansion1 if c in empty_cols else 1
      res2 += expansion2 if c in empty_cols else 1

print(res1)
print(res2)
