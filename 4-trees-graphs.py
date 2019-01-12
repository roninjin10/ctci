class GraphNode:
  def __init__(self, value, children = [], parent = None):
    self.value = value
    self.children = children
    self.parent = parent


# 4.1 Route Betweeen Nodes


def breadth_first_search(node, cb, depth = 0):
  queue = Queue()

  def _breadth_first_search(node, cb, depth = 0):
    cb(node, depth)

    for edge in node.edges:
      queue.enqueue({node: node.edges, depth: depth + 1})

    if len(queue):
      next_item = queue.dequeue
      return _breadth_first_search(next_item.node, cb, next_item.depth)


  _breadth_first_search(node, cb)


# 4.1 Route Between Nodes


def route_between_nodes(node1, node2):
  # As a human the best we can do is breadth first search with our friends until we exhaust our options
  start_nodes = [node1, node2]

  seen_nodes = set()
  is_route = False

  def check_node(node):
    if not node in seen_nodes:
      seen_nodes.add(node)
      return

    if node in start_nodes:
      is_route = True
      return

  for start_node in [node1, node2]:
    breadth_first_search(start_node, check_node)

  return is_route


# 4.2 Minimal Tree


def min_tree(sorted_array):
  # a binary search tree is going to have each root be a middle node of the array
  if len(sorted_array) == 0:
    return None

  middle_index = len(sorted_array) // 2

  middle_value = sorted_array[middle_index]

  left_child = min_tree(sorted_array[0:middle_index])
  right_child = min_tree(sorted_array[middle_index+1:])

  return GraphNode(middle_value, [left_child, right_child], None)


# 4.3 List of Depths


def arr_to_ll(arr):
  _arr = arr[::-1]

  if not _arr:
    return None

  head = LL(_arr.pop())
  current = head

  while _arr:
    next_node = LL(_arr.pop())
    current.next = next_node
    current = next_node

  return head

def list_of_depths(binary_tree):
  depths = {}

  def add_to_depth(node, depth):
    if not str(depth) in depths:
      depths[str(depth)] = []

    depths[str(depth)].append(node)

  add_to_depth(binary_tree)

  for depth of depths:
    depths[depth] = arr_to_ll(depths[depth])

  return depths


# 4.4 check balanced


def check_balanced:
  # 1. if only one child then a node must have no grandchildren
  if not node.left_node and node.right_node and node.right_node.children:
    return False
  if not node.right_node and node.left_node and node.left_node.children:
    return False

  # 2. all children nodes must also be balanced
  if node.right_node:
    if not check_balanced(node.right_node):
      return False
  if node.left_node:
    if not check_balanced(node.left_node):
      return False

  # 3. otherwise it is balanced
  return True


# 4.5 Validate BST


def validate_bst(bst, balanced = False):
  if bst.right_child and bst.left_child:
    if bst.right_child.value < bst.left_child:
      return False

  if bst.left_child:
    if not validate_bst(bst.left_child):
      return False

  if bst.right_child:
    if not validate_bst(bst.right_child):
      return False

  if balanced:
    if not check_balanced(bst):
      return False

  return True


# 4.6 Successor


def successor(bst):
  def find_first_larger_parent(bst):
    if not bst.parent:
      return None

    if bst.parent.value > bst.parent.value:
      return bst.parent

    return find_first_larger_parent(bst.parent)

  if not bst.right_child:
    return find_first_larger_parent(bst)

  return bst.right_child


