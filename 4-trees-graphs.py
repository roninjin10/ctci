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


# 4.7 Build Order


def build_order(nodes):
  processed_nodes = set()
  processing_nodes = set()
  out = []

  def build_node(node):
    if node in processing_nodes:
      raise Exception('Circular dependency')

    if node in seen_nodes:
      return

    processing_nodes.add(node)

    # edges must be directed
    for dependency in nodes.edges:
      build_order(dependency)

    out.append(node)

    processing_nodes.remove(node)
    processed_nodes.add(node)

  for node in nodes:
    build_node(node)

  return out.reverse()


# 4.8 First Common Ancestor


def first_common_ancestor(node1, node2):
  # to do this without storing in an additional datastructure we just need to find the depth of the two nodes
  # after finding the depth we then move the further down node up until they are on same level
  # then we move them botht at the same time until they are on the same ancestor
  def _first_common_ancestor(deep_node, shallow_node):
    ancestor_1 = deep_node
    ancestor_2 = shallow_node

    for i in range(abs(depth_1 - depth_2)):
      ancestor_1 = ancestor_1.parent

    while ancestor_1 != ancestor_2:
      ancestor_1 = ancestor_1.parent
      ancestor_2 = ancestor_2.parent

    return ancestor_1

  depth_1 = find_depth_bt(node1)
  depth_2 = find_depth_bt(node2)

  args = node1, node2 if depth_1 > depth_2 else node2, node1

  return _first_common_ancestor(*args)


# 4.9 BST sequences

# unfinished
def bst_sequences(bst):
  # we can generate every sequence kinda recursively
  # we start with just root node in a set of potential next nodes
  # whenever we pick a next node we delete that next node from the set and add all it's children
  # the arrays that can lead to that bst are the concatanation of every order of next node

  next_nodes = {bst}

  def process_nodes(bst, next_nodes):
    if len(next_nodes) == 0:
      return []

    out = []

    for next_node in next_nodes:
      out.append([next_node.value] + process_nodes())
