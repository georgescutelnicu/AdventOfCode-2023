from collections import Counter

CARD_MAPPING = {"T": "A", "J": "-", "Q": "C", "K": "D", "A": "E"}

def classify_hand(hand):

  copy_of_hand = hand
  joker_count = sum(1 for card in hand if card == 'J')
  
  if joker_count == 5:
      hand = 'AAAAA'
  else:
      most_freq = Counter(char for char in hand if char != 'J')
      sorted_freq = sorted(most_freq.items(), key=lambda item: (item[1], CARD_MAPPING.get(item[0], item[0])), reverse=True)
      most_frequent_char = sorted_freq[0][0]
      hand = hand.replace('J', most_frequent_char)
  
  counts = [hand.count(card) for card in hand]

  rank = 0
  if 5 in counts:
    rank = 6
  elif 4 in counts:
    rank = 5
  elif 3 in counts:
    if 2 in counts:
      rank = 4
    else:
      rank = 3
  elif counts.count(2) == 4:
    rank = 2
  elif 2 in counts:
    rank = 1

  return (rank, [CARD_MAPPING.get(card, card) for card in copy_of_hand])
  

with open('7.txt', 'r') as f:
  card_hands = [(hand.split()[0], int(hand.split()[1])) for hand in f.readlines()]

  card_hands.sort(key=lambda hand: classify_hand(hand[0]))
 
  res = 0

  for rank, hand in enumerate(card_hands, 1):
    res += rank * hand[1]

  print(res)
