from entities import Node, List
from .data.handler import get_data

def relact(src, tgt):
  data = get_data()
  nodes = []
  for node in data['nodes']:
    nodes.append(Node(node['id'], node['value'], node['label']))

  for edge in data['edges']:
    source = nodes[edge['source']]
    target = nodes[edge['target']]
    source.link_to(target)

  graph = List(nodes)
  return graph.find_connection_label(src, tgt)
