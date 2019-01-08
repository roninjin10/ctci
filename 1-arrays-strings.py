# 1.1 Is Unique

def is_unique(str):
  # As a human, my algorithm is as follows.
  # I want to look at every character in the string
  # I will remember what I see
  # I answer the question

  seenChars = set()

  for c in str:
    if c in seenChars:
      return False
    seenChars.add(c)
  return true

def is_unique(str):
  # As a human, my algorithm is as follows:
  # We want to look at ever char in sth str
  # we will remember what we see via a set hash
  # this will allow constant time lookups to see if we remember
  # we will then return true if we find no dopops



# Check Permutation

from collections import defaultdict

  def count_letters(str):
    letters = defaultdict(lamda: 0)

    for c in str:
      letters[c] += 1

    return letters

def check_permutation(str1, str2):
  # As a human, my algorithm is as follows.
  # a string is a permutation when they have the same letters
  # we can be more specific and say a string is a permutation when they have the same count of every letter letters

  # so lets count the letters and then assert they are equal


  def combine_letter_counts(letters1, letters2):
    combined_keys = set(letters1.keys).union(letters2.keys)

    out = defaultdict(lamda: [0, 0])

    for key in combined_keys:
      out[key][0] += 1
      out[key][1] += 1

    return out

  def counts_are_equal(counts):
    for count in counts:
      if count[0] != counts[1]:
        return false
    return true

  count1 = count_letters(str1)
  count2 = count_letters(str2)

  counts = combine_letter_counts(count1, count2)

  return counts_are_equal(counts)

def urlify(str):
  # As a human, my algorithm is as follows.
  # I look for spaces
  # I replace with %20

  # We must be careful to escape %20s that aren't spaces first though
  return str.replace('%20', '\%20').replace(' ', '%20')

def palindrome_permutation(str):
  # dumb algo, find every permutation until you find a palindrome
  # time complexity of this is going to be the combitorics of taking every letter in the string where order matters
  # so we follow a decision tree to figure out the time complexity
  # the first letter can be n characters (discounting the fact that characters likely repeat though we will need to circle back here because this makes a huge difference and might lead to a fun clever solution)
  # we remove that letter from the pool of letters and choose one of n-1 then n-2 so we see there are n! combinations therefore that is the time complexity and it is AWFUL

  # the clever solution the more I think of it the more it turns into what I think is the best solution
  # instead we loop through the palindrome and count letters (we can reuse count letters from above)
  # palindromes seem to naturally have an even amount of numbers
  # but we can have one letter in the middle that is it's own color and still be symetric
  # so the algorithm I take as a human is to count the letters and then assert that 0 or 1 letters have an odd count
  is_odd_count = False

  counts = count_letters(str)

  for key, value in counts:
    if value % 2:
      if is_odd_count:
        return False
      is_odd_count = True
  return true

def one_away(str1, str2):
  # as a very dumb human I would just look through both strings attempting to make all three edits
  # we will have to spec them out seperately but if we do this and we find an match we are good
  # so we are attempting the same thing on every letter of both strings so the time complexity is str1.length + str2.length
  # Have to look lemma, if it's ever impossible to know without looking at entire input of an array or string then time complexity will never be less than O(n)

  def check_string_edit(str_to_edit, str2):

    for i in range(len(str_to_edit))
      if (
        attemptDeletion(str_to_edit, i)  == str2 or
        attemptChange(str_to_edit, i) == str2 or
        attemptInsert(str_to_edit, i) == str2
      ):
        return False
    return True

  return check_string_edit(str1, str2) or check_string_edit(str2, str1)

def string_compression(str):
  # as a human I would follow the following algorithm
  # I would look at every character
  # I would keep track of runs
  # I would then append to my final answer everytime I reach the end of a letter

  out = ''
  lastChar = None
  currentRun = 0

  for c of str:
    if c == lastChar:
      currentRun++
    else:
      out += lastChar + str(currentRun) if currentRun else ''
      currentRun = 1
      lastChar = c

  return out if len(out) < str else str

# refactor this to be cleaner
def rotate_matrix(matrix): # rotates in place
  # we are trying to do this in place
  # as a computer I am going to rotate 4 things at once
  # these 4 things can be found by looking at examples
  # 4 x 4 matrix 0,0 0,3 3,3 3,0 = 0,3, 3,3, 0,0
  #              1,1 1,2 2,2 2,1S

  # note just for readability I am doing extra work looking at every cell instead of 25% of them

  size = len(matrix)
  halfway_mark = math.ceil(size / 2)

  for i in range(halfway_mark):
    for j in range(halfway_mark):
      top_right = matrix[i][j]
      top_left = matrix[i][size - 1 - j]
      bottom_right = matrix[size - 1 - i][size - 1 - j]
      bottom_left = matrix[size - 1 - i][j]

      matrix[i][j] = bottom_left
      matrix[i][size - 1 - j] = top_left
      matrix[size - 1 - i][size - 1 - j] = top_right
      matrix[size - 1 - i][j] = bottom_right

  return matrix

def zero_matrix(matrix):
  # as a human I am going to look through the entire matrix
  # everytime I see a 0 I will draw a circle around the entire row and col
  # anything that is incircled is then changed to 0
  # to represent thisx in python we can circle via adding the index of the row or col to a set and then loop through the matrix marking

  def findRowAndColsWithZero(matrix):
    out = {
      rows: set(),
      cols: set(),
    }

    for i,row in matrix:
      for j,value in row:
        if value == 0:
          out.rows.add(i)
          out.cols.add(j)

    return out

  def shouldBeZero(i, j, zeros):
    return i in zeros.rows or j in zeros.cols

  zeros = findRowAndColsWithZero(matrix)

  out = [row[:] for row in matrix]

  for i,row in matrix:
    for j,value in row:
      out[i][j] = matrix[i][j] if not shouldBeZero(i, j, zeros) else 0

  return out

def is_string_rotation(str1, str2):
  # as a human I would go letter by letter down the string until I found a rotation
  return len(str1) == len(str2) && str1 in (str1 + str2)
