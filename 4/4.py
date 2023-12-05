res = 0
card_sets = 0

with open('4.txt', 'r') as f:
 
  card_dict = {key: 1 for key in range(0, len(f.readlines()))}
  f.seek(0)

  for card_set, line in enumerate(f):
    nums = line.strip().split(':')[1]

    count = 0
    
    my_numbers = [n for n in nums.split('|')[0].split()]
    winning_numbers = [n for n in nums.split('|')[1].split()]

    for number in my_numbers:
      if number in winning_numbers:
        count += 1

    if count > 0:
      res += 2 ** (count-1)

    for i in range(card_set+1, card_set+1+count):
      card_dict[i] += card_dict[card_set]

  for val in card_dict.values():
    card_sets += val

print(res)
print(card_sets)
