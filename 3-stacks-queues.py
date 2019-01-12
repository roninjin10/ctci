# 3.1 Three in One

# make three array sout of 1 array
class Array:
  def __init__(self):
    # first 3 indexes represent where the next unused index for that array is
    self._arr = [3, 4, 5]

  def get_arr(self,i):
    self._validate_index(i)

    return [x for j,x in self._arr if j % (self._count + i - 1)]

  def push(self, i, item):
    self._validate_index(i)

    next_index = self._arr[i]

    while next_index > len(self._arr):
      self._arr.push(None)

    self._arr[next_index] = item

    self._arr[i] += 3

  def pop(self,i):
    self._validate_index(i)

    item_index = self._arr[i] - 3

    if item_index < 3:
      return None

    popped_item = self._arr[item_index]

    self._arr[item_index] = None

    return popped_item

  def _validate_index(self, i):
    if i >= 3:
      raise Exception('That array does not exist')


# 3.2 Stack Min


# stacks are a good datastructure for being able to go back in history in a browser
# we can use a second data structure to similarly keep track of the history of the min
class Stackmin:
  def __init__(self):
    self._stack = []
    self._mins = []

  def push(self, item):
    min_at_index = self._min if self._min != None and self._min < item else item

    self._mins.append(min_at_index)
    self._stack.append(item)

  def pop():
    self._mins.pop()
    return self._stack.pop()

  def get_min():
    return self._mins[-1]


# 3.3 Stack Of Plates


class StackOfPlates:
  def __init__(self, max_height):
    self._stacks = [[]]
    self._max_height = 10

  def push(self, item):
    if len(self._stacks[-1]) >= self._max_height:
      self._stacks.append([])

    self._stacks[-1].append(item)

  def pop(self, item):
    popped_item = self._stacks[-1].pop()

    if len(self._stacks[-1]) == 0:
      self._stacks.pop()

    return popped_item


# 3.4 Queue vs Stacks


class MyQueue:
  def __init__(self):
    self.inbound = []
    self.outbound = []

  def enqueue(self, item):
    self.inbound.append(item)

  def dequeue(self):
    self.populate_outbound()
    return self.outbound.pop()

  def peak(self):
    self.populate_outbound()
    return self.outbound[-1]

  def populate_outbound(self):
    if !self.outbound:
      while self.inbound:
        self.outbound.append(self.inbound.pop())

# 3.5 Sort Stack


def sort_stack(stack):
  def insert_item(stack, item, buffer_stack):
    let items_popped = 0

    while stack and stack[-1] < item:
      buffer_stack.append(stack.pop())
      items_popped++

    stack.append(item)

    while items_popped:
      stack.append(buffer_stack.pop())
      items_popped--

  internal_stack = []
  while stack:
    next_item = internal_stack.pop()

    insert_item(internal_stack, item, stack)

  return internal_stack


# 3.6 Animal Shelter


class Animal:
  # with an abritrary amount of possible animals we might want a heap structure to keep track of the animal type that has been there the longest

  def __init__(self, animal_type, name):
    self.type = animal_type
    self.name = name

class AnimalShelter:
  _oldest_pet = None

  def __init__(self):
    self._dogs = MyQueue()
    self._cats = MyQueue()
    self._setOldestPet()

  def enqueue(self, animal):
    # add time
    animal.time_added = getCurrentDateAndTime()
    if animal.type === 'DOG':
      self._dogs.enqueue(animal)

    else if animal.type === 'CAT':
      self._cats.enqueue(animal)

    else:
      raise Exception('invalid animal type')

    self._setOldestPet()

  def dequeueAny(self):
    if _oldest_pet == None:
      return None

    if _oldest_pet == 'CAT':
      return self.dequeueCat()

    if _oldest_pet == 'DOG'
      return self.dequeueDog()

    raise Exception('Oldest pet is not an animal')

  def dequeueDog(self):
    out = self._dogs.dequeue()
    self._setOldestPet()
    return out

  def dequeueCat(self):
    out = self._cats.dequeue()
    self._setOldestPet()
    return out

  def _setOldestPet(self):
    oldest_dog = self._dogs.peak()
    oldest_cat = self._cats.peak()

    if !oldest_cat and !oldest_dog:
      self._oldest_pet = 'DOG'

    if !oldest_cat or !oldest_dog:
      self._oldest_pet = 'DOG' if oldest_dog else 'CAT'

    self._oldest_pet = 'DOG' if oldest_dog.time_added < oldest_cat.time_added else 'CAT'