# 17.2 Shuffle

def shuffle(arr):
  # to have a perfect shuffle each of the 52 cards must be likely to be in each spot
  # iterate 0 through 51 and swap card with one of the other remaining cards
  out = arr[:]

  for i in range(len(out)):
    cards_left = len(out) - i

    card_index = i + random_int(0, cards_left)

    temp = out[i]
    out[i] = out[card_index]
    out[card_index] = temp

  return out
