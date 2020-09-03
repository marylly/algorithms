import unittest

from graph.Graph import Graph

class TestBreadthFirstSearch(unittest.TestCase):
    QUANTITY = None
    START = None
    graph = None

    def setUp(self):
        self.QUANTITY = 2
        self.START = 2
        self.graph = Graph(self.QUANTITY, self.START)
        self.graph.add_edge(4, 2)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(3, 5)
        return super().setUp()

    def test_node_quantity_input(self):
        self.assertEqual(self.graph.get_qtd_nodes(), self.QUANTITY)

    def test_node_start_input(self):
        self.assertEqual(self.graph.get_start(), self.START)

    def test_add_edges(self):
        self.assertEqual(list(self.graph.get_nodes().keys()), [4, 1, 3])

    def test_get_origin_nodes(self):
        self.assertEqual(set(self.graph.get_origin_nodes()), set([1,3,4]))

    def test_get_all_destination_nodes(self):
        self.assertEqual(self.graph.get_all_destination_nodes(), set([2,3,5]))

    def test_get_destination_nodes(self):
        self.assertEqual(self.graph.get_destination_nodes(1), [2,3])
        
    def test_node_not_origin(self):
        self.assertEqual(self.graph._node_not_origin(5), True)

    def test_node_not_destination(self):
        self.assertEqual(self.graph._node_not_destination(4), True)

    def test_last_path_node(self):
        self.assertEqual(self.graph.check_if_last_path_node(2), True)

    def test_node_path(self):
        path = []
        # self.graph.get_path(4, path)
        # self.assertEqual(path, [2])
        self.graph.get_path(1, path)


    # def test_add_node(self):
    #     """
    #     Test the graph nodes input
    #     2 <- Node Start
    #     4 2 <- Nodes
    #     1 2
    #     1 3
    #     1
    #     3 1
    #     2 3
    #     2
    #     """
        # graph = Graph(2)
        # graph.add_node(4, 2, 6)
        # graph.add_node(1, 2, 6)
        # graph.add_node(1, 3, 6)
        # graph.add_node(3, 5, 6)

        # print(graph.nodes)
        # self.assertEqual(graph.get_dest_nodes(4), [2])
        # self.assertEqual(graph.get_dest_nodes(1), [2, 3])
        # graph.check_if_last_path_node(3)
        # print(graph.node_paths(1))

        # graph = Graph(7, 2)
        # graph.add_edge(1,2,6)
        # graph.add_edge(1,3,6)
        # graph.add_edge(3,4,6)
        # graph.add_edge(2,5,6)
        # print(graph.node_paths(2))
        # graph.calc_node_paths()


    def test_path_cost(self):
        """
        6 6 -1
        -1 6
        """

    def tearDown(self):
        del self.QUANTITY
        del self.START
        del self.graph
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()