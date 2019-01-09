class LL:
  def __init__(self, value, prevnode = None, nextnode = None):
    self.value = value
    self.prevnode = prevnode
    self.nextnode = nextnode


# 2.1 Remove Dups


def remove_dups(ll):
  # to remove dups I just traverse linked list remembering what I see
  # when I see a repeat I remove it
  seen = {ll.value}
  head = LL(ll.value)
  current_out = head
  current_original = ll

  while current_original != None:
    if not (current_original.value in seen):
      current_out.nextnode = LL(current_original.value)
      current_out = current_out.nextnode

    current_original = current_original.next

  return head


# 2.2 Return Kth To Last


def find_kth_element(ll, k):
  out = ll
  for _ in range(k):
    out = out.nextnode
  return out

def find_ll_length(ll):
  length = 0
  while(ll != None):
    length += 1
    ll = ll.next
  return length

def kth_to_last(ll, k):
  # to return the kth to last we just have to count how long the linked list is, then return the length - kth element
  ll_length = find_ll_length(ll)
  return find_kth_element(ll, ll_length - k) # might want to check for off by 1 h3re


# 2.3 Delete Middle Node


def delete_middle_node(node):
  # from the perspective of the middle node
  # we just need to become the next node
  if !node.next:
    raise Exception('Node must be a middle node!')

  node.value = node.next.value
  node.next = node.next.next


# 2.4 Partition


def partition(head, num):
  # to partition we just traverse the linked list

  # this wouild be cleaned up significantly by doing the linked lists seperately and abstracting
  # this is poorly done.  Absolutely awful.  The rule from very beginning is do one thing and one thing well. DOn't solve entire problem in a single fwhile loop
  # refactoring this to do each linked list in seperate operations is slower is the only redeeming thing but not in terms of time complexity so who cares

  head1 = findHead(1)
  head2 = findHead(2)

  tail1 = None
  tail2 = None

  current_node = head

  while current_node:
    is_ll1 = current_node.value < num

    if ll1 == None && is_ll1:
      ll1 = LL(current_node.value)
    else if ll2 == None && !is_ll1:
      ll2 = LL(current_node.value)

    else if is_ll1:
      tail1.next = LL(current_node.value)
      tail1 = tail1.next
    else if !is_ll1: # explicit
      tail2.next = LL(current_node.value)
      tail2 = tail2.next

  def connectLL(head, tail, LL2):
    tail.next = ll2
    return head

  return connectLL(head1, tail1, head2) if head1 else tail1


# 2.5 Sum Lists


def ll_to_num(head):
  exp = 0
  out = 0

  current_node = head

  while(current_node):
    out += current_node.value * 10**exp
    exp += 1

  return out

def num_to_ll(num):
  reversed_number = str(num).split('').reverse()

  head = LL(reversed_number.pop())
  current = head

  while(reversed_number):
    current.next = LL(reversed_number.pop())

  return head

def sum_lists(ll1, ll2):
  # as a human I just do human addition
  # we could cocd this but that would not be the best way to solve this problem
  # instead we want two functions.  One to transform LL to number and one to do the opposite
  # this way we can just use Python addition and we have more reusable compononts that dop much simpler things well

  # this is stupid way to represent this
  return num_to_ll(sum(
    ll_to_num(ll) for ll in [ll1, ll2])
  )


# 2.6 Palindrome


def reverse_ll(head):
  out_tail = LL(head.value)
  out_head = out_tail

  current_node = head.next

  while current_node:
    new_head = LL(head.value, nextnode = out_head)
    out_head = new_head
    current_node = current_node.next

  return out_head

def ll_is_equal(head1, head2):
  if not head1 or not head2:
    return head1 == head2

  if head1.value != head2.value:
    return False

  return ll_is_equal(head1.next, head2.next)

def palindrome(head):
  return ll_is_equal(head, reverse_ll(head))


# 2.7 Intersection
def node_is_descendent(head, potential_descendent):
  current_node = head
  while(current_node):
    if current_node == potential_descendent:
      return true
    current_node = current_node.next
  return false

def intersection(head1, head2):
  # to see if it intersects, I just remember the heads of the linked lists
  # I then traverse both until I see if the node exists
  return node_is_descendent(head1, head2) or node_is_descendent(head2, head1)
