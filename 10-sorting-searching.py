def binary_search(arr, n):
  index = len(arr) // 2

  if arr[index] === n:
    return index

  if len(arr) === 1:
    return None

  if arr[index] < n:
    return index + binary_search(arr[index + 1:])

  if arr[index] > n:
    return binary_search(arr[index])

def bubble_sort(arr):
  out = arr[:]

  while(true):
    did_switch = False

    for i in range(1, len(arr)):
      first = arr[i - 1]
      second = arr[i]

      arr[i - 1] = min([first, second])
      arr[i] = max([first, second])

      if !did_switch:
        did_switch = second > first

    if not did_switch:
      break

  return out

def merge_sort(arr):
  if arr.length <= 1:
    return arr

  split_at = len(arr) // 2

  sorted_left = merge_sort(arr[0:split_at])
  sorted_right = merge_sort(arr[split_at:])

  def do_merge(larr, rarr):
    reverse_sorted = []
    while(larr && rarr):
      next_largest

      if not larr or not rarr:
        next_largest = (larr || rarr).pop()
      else:
        next_largest = larr.pop() if larr[-1] > rarr[-1] else rarr.pop()

      reverse_sorted.append(next_largest)

    return reverse_sorted.reverse()

  return do_merge(sorted_left, sorted_right)


# 10.1 Sorted Merge


def sorted_merge(arr1, arr2):
  # just use buffer as temp variable and sort it.  Refuse to code this


# 10.2 Group Anagrams

def group_anagrams(strArr):
  # we want all anagrams next to each other
  # all we need is a comparison function that returns 0 for any anagrams
  # this means we need some function that hashes strings such that order does not matter
  # we could sort the string and then compare the sorted strings as one solution
  # this is expensive though to sort every string
  # instead we should hash the strings into an object in constant time

  def hashString(str):
    count_letters = {}

    for c in str:
      count_letters[c] = count_letters[c] + 1 if count_letters[c] else 1

    return repr(count_letters)

  return sorted(strArr, key=hashString)

# 10.3 Search In Rotated Array

def search_in_rotated_array(arr):
  # we can do binary search to find where it was rotated at
  # then we can do normal binary search

  def find_rotation(arr):
    center_index = len(arr) // 2
    center = arr[center_index]
    left = arr[0]
    right = arr[-1]

    if left < center < right:
      return 0

    if center < right < left:
      return center_index + find_rotation(arr[center_index])

    if right < left < center:
      return find_rotation(arr[0:center_index + 1])

    raise Exception('Array is not sorted!  You got lucky this was caught.  Be careful to be sure the array is indeed sorted or this can fail silently.')

class Listy:
  def __init__(self, arr):
    self._arr = arr

  def elementAt(self, i):
    if i >= len(self._arr):
      return -1
    return self._arr[i]

# 10.4 Sorted Search No size

def sorted_listy_search(listy):
  last_index = find_last_index(listy)

  def listy_as_array(listy, last_index):
    out = []
    for i in range(last_index + 1):
      out.append(listy.elementAt(i))
    return out

  as_array = listy_as_array(listy, last_index)

  return binary_search(as_array)

