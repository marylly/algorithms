import unittest

from graph.Graph import Graph

class TestBreadthFirstSearch(unittest.TestCase):
    START = None
    graph = None

    def setUp(self):
        self.START = 1
        self.graph = Graph(self.START)
        self.graph.add_edge(4, 2)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        return super().setUp()

    def test_node_quantity_input(self):
        self.assertEqual(self.graph.get_qtd_nodes(), 4)

    def test_node_start_input(self):
        self.assertEqual(self.graph.get_start(), self.START)

    def test_add_edges(self):
        self.assertEqual(list(self.graph.get_nodes().keys()), [4, 1])

    def test_get_origin_nodes(self):
        self.assertEqual(set(self.graph.get_origin_nodes()), set([1,4]))

    def test_get_all_destination_nodes(self):
        self.assertEqual(self.graph.get_all_destination_nodes(), set([2,3]))

    def test_get_destination_nodes(self):
        self.assertEqual(self.graph.get_destination_nodes(1), [2,3])
        
    def test_node_not_origin(self):
        self.assertEqual(self.graph._node_not_origin(5), True)

    def test_node_not_destination(self):
        self.assertEqual(self.graph._node_not_destination(4), True)

    def test_last_path_node(self):
        self.assertEqual(self.graph.check_if_last_path_node(2), True)

    # def test_node_path(self):
    #     self.assertEqual(self.graph.get_node_paths(1),[[2],[3,5]])

    # def test_all_paths(self):
    #     self.assertEqual(self.graph.get_all_paths(),[[],[[2],[3,5]],[[5]],[[2]],[]])

    # def test_node_cost(self):
    #     self.assertEqual(self.graph.get_node_cost(5), 12)

    def test_all_cost(self):
        self.graph.get_all_paths()
        self.assertEqual(self.graph.get_costs(),  [6, 6, -1])

    # def test_add_node(self):
    #     """
    #     Test the graph nodes input
    #     1
    #     3 1
    #     2 3
    #     2
    #     """

    # def test_path_cost(self):
    #     """
    #     6 6 -1
    #     -1 6
    #     """

    def tearDown(self):
        del self.START
        del self.graph
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()