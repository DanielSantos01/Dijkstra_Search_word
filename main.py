from data_handler import get_data
from node import Node, List


def main():
    data = get_data()
    nodes = []
    for node in data['nodes']:
        nodes.append(Node(node['id'], node['value'], node['label']))

    for edge in data['edges']:
        source = nodes[edge['source']]
        target = nodes[edge['target']]
        source.link_to(target)

    graph = List(nodes)
    
    print(graph.find_connection_label('man', 'agreeable'))


if __name__ == '__main__':
    main()
