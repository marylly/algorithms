from functools import reduce
from operator import add

class Graph(object):
    nodes = {}
    paths = []
    costs = []
    qtd_nodes = 0
    def __init__(self, start=None):
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
        self.set_node_quantity(origin)
        self.set_node_quantity(destination)

        if self._dest_not_exists_in_node(origin, destination):
            self.nodes[origin].append({'dest': destination, 'cost': float('inf')})

    def set_node_quantity(self, node):
        if node > self.qtd_nodes:
            self.qtd_nodes = node

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

    def _node_only_origin(self, node):
        return node in list(self.nodes.keys()) and node not in self.get_all_destination_nodes()

    def _node_not_destination(self, node):
        return node not in self.get_all_destination_nodes()

    def check_if_last_path_node(self, node):
        return node in self.get_all_destination_nodes() and len(self.get_destination_nodes(node)) == 0

    def get_node_paths(self, node):
        nodes_dest = self.get_destination_nodes(node)
        dest_count = len(nodes_dest)
        count_path = 0
        self.paths.insert(node, [])
        for dest in range(0, dest_count):
            self.paths[node].insert(count_path, [nodes_dest[dest]])
            self.get_path(node, nodes_dest[dest], count_path)
            count_path = count_path + 1

        if dest_count == 0:
            self.paths[node].insert(count_path, [])

        return self.paths

    def get_path(self, node_origin, node, count_path):
        nodes_dest = self.get_destination_nodes(node)

        for dest in range(0, len(nodes_dest)):
            self.paths[node_origin][count_path].append(nodes_dest[dest])
            self.get_path(node_origin, nodes_dest[dest], count_path)
            

    def get_all_paths(self):
        self.paths.insert(0, [])
    
        for node in range(0, self.get_qtd_nodes()):
            self.get_node_paths(node)

        return self.paths

    def get_node_cost(self, node):
        self.costs = [0] * (self.get_qtd_nodes() + 1)
        self.get_costs()
        return self.costs[node]

    def get_costs(self):
        self.costs = [0] * (self.get_qtd_nodes() + 1)
        list_nodes = [ node for node in range(0, self.get_qtd_nodes())]
        for index, node in enumerate(list_nodes, 0):
            if self._node_only_origin(node):
                if len(self.paths[node]) == 1:
                    self.costs[node] = -1
                else:
                    self.costs[node] = 6
            
            self.get_cost(self.paths[node])

        del self.costs[self.start -1 ]
        self.costs = [-1 if cost==0 else cost for cost in self.costs]
        del self.costs[0]
        return self.costs

    def get_cost(self, paths):
        for path in range(0, len(paths)):
            for edge in range(len(paths[path])-1, -1, -1):
                if self.get_start() in paths[path]:
                    custo = (edge -1)  * 6
                else:
                    custo = ((edge + 1) * 6)

                if(self.costs[paths[path][edge]] < custo):
                    self.costs[paths[path][edge]] = custo   
