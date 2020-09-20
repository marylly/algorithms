import unittest

from graph.Graph import Graph

class TestBFS_Case_0(unittest.TestCase):
    START = None
    graph = None

    def setUp(self):
        self.START = 1
        self.graph = Graph(self.START)
        self.graph.add_edge(4, 2)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        return super().setUp()

    def test_case_0(self):
        self.graph.get_all_paths()
        self.graph.get_costs()
        self.assertEqual(self.graph.get_costs(),[6,6,-1])

    def tearDown(self):
        del self.START
        del self.graph
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()