res = []
nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('1.txt', 'r') as f:
  for line in f:
    temp = ''

    for idx, c in enumerate(line.strip()):
      if c.isdigit():
        temp += c

      for num in nums:
        if line[idx:].startswith(num):
          temp += str(nums.index(num)+1)
          break

    if len(temp) < 2:
      res.append(int(temp+temp))
    else:
      res.append(int(temp[0]+temp[-1]))

score = 0

for r in res:
  score += r
  
print(score)
