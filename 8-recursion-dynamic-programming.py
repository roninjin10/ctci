# 8.1 Triple Step

def memoizer(f):
  memoized = {}

  def memoized_function(*args):
    if not repr(x) in memoized:
      memoized[repr(x)] = f(x)

    return memoized[repr(x)]

  return memoized_function

def _triple_step(steps):
  if steps == 0:
    return 1

  if steps == 1:
    return 1

  if steps == 2:
    return 2

  if steps >= 3:
    return triple_step(steps - 3) + triple_step(steps - 2) + triple_step(steps - 1)

triple_step = memoizer(dumb_triple_step)


# 8.2 Robot in a Grid

# we are passed in a matrix of booleans
def traverse_grid(matrix):
  def is_in_bounds(location, matrix):
    return 0 <= location[0] < len(matrix) and 0 <= location[1] < len(matrix[0])

  def move(direction):
    out = None

    if direction == 'up':
      out = direction[0] + 1, direction[1]
    else if direction == 'down':
      out = direction[0] - 1, direction[1]
    else if direction == 'left':
      out = direction[0], direction[1] - 1
    else if direction == 'right':
      out = direction[0], direction[1] + 1

    if out == None:
      raise Exception(direction + ' is not a valid direction')

    if not is_in_bounds(out, matrix):
      return None

    return out 


  def can_step(row, col):
    return matrix[row][col]

  # start and end are tuples (row, col)
  # they return a tuple
  def shortest_path(start, end):
    if not can_step(*start):
      return None

    if start[0] == end[0] and start[1] == end[1]:
      return start, 0

    up_direction = shortest_path(move['up'](start), end)
    down_direction = shortest_path(move['down'](start), end)
    right_direction = shortest_path(move['right'](start), end)
    left_direction = shortest_path(move['left'](start), end)

    valid_directions = [d for d in [up_direction, down_direction, right_direction, left_direction] if d != None]

    if len(valid_directions) == 0:
      return None

    out = valid_directions.pop()

    while len(valid_directions) != 0:
      next_direction = valid_directions.pop()
      out = next_direction if next_direction.distance < out.distance else out

    return out

  memoized_shortest_path = memoizer(shortest_path)

  return memoized_shortest_path(matrix)

# 8.3 Magic Index 
def _magic_index(arr, offset = 0):
  if len(arr) == 0:
    return None

  if len(arr) == 1:
    return arr[0] == offset

  middle_index = len(arr) // 2

  middle_index_value = arr[middle_index]

  if middle_index_value == offset:
    return middle_index_value

  if middle_index_value < offset:
    return _magic_index(arr[middle_index:], middle_index)

  if middle_index_value > offset:
    return _magic_index(arr[0:middle_index])

def magic_index(arr):
  return _magic_index(arr)
