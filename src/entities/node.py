class Node:
  def __init__(self, id, value, label):
    self.id = id
    self.value = value
    self.label = label
    self.visited = False
    self.links = []

  def visit(self):
    self.visited = True

  def unvisit(self):
    self.visited = False

  def link_to(self, node):
    self.links.append(node)
