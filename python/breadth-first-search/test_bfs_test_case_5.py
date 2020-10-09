import unittest

from graph.Graph import Graph

class TestBFS_Case_5(unittest.TestCase):
    START = None
    graph = None

    def setUp(self):
        self.START = 2
        self.graph = Graph(self.START)
        self.graph.add_edge(7, 4)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(3, 4)
        self.graph.add_edge(2, 5)
        return super().setUp()

    def test_case_5(self):
        self.graph.get_all_paths()
        self.graph.get_costs()
        self.assertEqual(self.graph.get_costs(),[6, 12, 18, 6, -1, -1])

    def tearDown(self):
        del self.START
        del self.graph
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()