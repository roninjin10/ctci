# 4.1 Route Betweeen Nodes 
def _breadth_first_search(node, cb):
  def _breadth_first_search(node, cb):
    for edge in node.edges:
      cb(node.edges)

  cb(node)
  _breadth_first_search(node, cb)

def route_between_nodes(node1, node2):
  # As a human the best we can do is breadth first search with our friends until we exhaust our options