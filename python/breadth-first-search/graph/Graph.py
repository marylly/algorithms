from functools import reduce
from operator import add

class Graph(object):
    nodes = {}
    paths = {}
    def __init__(self, qtd_nodes, start=None):
        self.qtd_nodes = qtd_nodes
        self.start = start

    def get_qtd_nodes(self):
        return self.qtd_nodes

    def get_start(self):
        return self.start

    def get_nodes(self):
        return self.nodes

    def get_origin_nodes(self):
        return list(self.nodes.keys())

    def get_all_destination_nodes(self):
        return set(reduce(add, [[dest['dest'] for dest in self.nodes[origin]] for origin in self.nodes.keys()]))

    def add_edge(self, origin, destination, cost=float('inf')):
        self.nodes.setdefault(origin, [])

        if self._dest_not_exists_in_node(origin, destination):
            self.nodes[origin].append({'dest': destination, 'cost': float('inf')})

    def get_destination_nodes(self, node):
        destinations = []
        nodes = self.nodes.get(node)
        if nodes != None and len(nodes) > 0:
            destinations = [dest_value['dest'] for dest_value in nodes]
        return destinations

    def _dest_not_exists_in_node(self, node, value):
        return value not in self.get_destination_nodes(node)

    def _node_not_origin(self, node):
        return node not in self.nodes.keys()

    def _node_not_destination(self, node):
        return node not in self.get_all_destination_nodes()

    def check_if_last_path_node(self, node):
        return node in self.get_all_destination_nodes() and self._node_not_origin(node)

    def get_path(self, node, path):
        print("to aqui", node)
        nodes_dest = self.get_destination_nodes(node)
        print(nodes_dest)
        for dest in range(0, len(nodes_dest)):
            path.append(nodes_dest[dest])
            self.get_path(nodes_dest[dest], path)
        print(path)

    def node_paths(self, node):
        self.paths[node] = []
        nodes_dest = self.get_dest_nodes(node)
        print("primeiro nivel", nodes_dest)

        for dest in range(0, len(nodes_dest)):
            path = []
            path.append(nodes_dest[dest])
            self.get_path(nodes_dest[dest], path)
            print("meu path", path)
            self.paths[node].append(path)

        print("meu resultado final")
        print(self.paths)
        print(self.nodes)