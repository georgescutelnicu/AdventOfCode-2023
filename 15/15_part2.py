def hash(s):
  val = 0
  for c in s:
    val = ((val + ord(c)) * 17) % 256
  return val


with open('15.txt', 'r') as f:
  inp = f.read().split(',')

boxes = [[] for _ in range(256)]
focal_lengths = {}

for seq in inp:
  if '-' in seq:
    label = seq[:-1]
    box = hash(label)
    if label in boxes[box]:
      boxes[box].remove(label)

  else:
    label = seq[:-2]
    focal_length = int(seq[-1])
    box = hash(label)
    if label not in boxes[box]:
      boxes[box].append(label)

    focal_lengths[label] = focal_length

res = 0

for i, box in enumerate(boxes):
  for j, label in enumerate(box):
    res += (i+1) * (j+1) * focal_lengths[label]

print(res)
