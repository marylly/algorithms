import unittest

from graph.Graph import Graph

class TestBFS_Case_6(unittest.TestCase):
    START = None
    graph = None

    def setUp(self):
        self.START = 3
        self.graph = Graph(self.START)
        self.graph.add_edge(10, 6)
        self.graph.add_edge(3, 1)
        self.graph.add_edge(10, 1)
        self.graph.add_edge(3, 1)
        self.graph.add_edge(1, 8)
        self.graph.add_edge(5, 2)
        return super().setUp()

    def test_case_6(self):
        self.graph.get_all_paths()
        self.graph.get_costs()
        self.assertEqual(self.graph.get_costs(),[6, -1, -1, -1, -1, -1, 12, -1, 12])

    def tearDown(self):
        del self.START
        del self.graph
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()