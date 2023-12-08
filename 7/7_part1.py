CARD_MAPPING = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

def classify_hand(hand):

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

  return (rank, [CARD_MAPPING.get(card) if not card.isdigit() else card for card in hand])


with open('7.txt', 'r') as f:
  card_hands = [(hand.split()[0], int(hand.split()[1])) for hand in f.readlines()]

  card_hands.sort(key=lambda hand: classify_hand(hand[0]))

  res = 0

  for rank, hand in enumerate(card_hands, 1):
    res += rank * hand[1]

  print(res)
