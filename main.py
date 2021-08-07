from data_handler import get_data
from node import Node

def main():
  data = get_data()
  nodes = []
  for node in data['nodes']:
    nodes.append(Node(node['id'], node['value'], node['label']))

  for edge in data['edges']:
    source = nodes[edge['source']]
    target = nodes[edge['target']]
    if source.value == 1 and target.value == 0:
      target.link_to(source)
    else:
      source.link_to(target)

if __name__ == '__main__':
  main()