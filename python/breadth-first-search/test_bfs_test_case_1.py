import unittest

from graph.Graph import Graph

class TestBFS_Case_1(unittest.TestCase):
    START = None
    graph = None

    def setUp(self):
        self.START = 2
        self.graph = Graph(self.START)
        self.graph.add_edge(3, 1)
        self.graph.add_edge(2, 3)
        return super().setUp()

    def test_case_1(self):
        self.graph.get_all_paths()
        self.graph.get_costs()
        self.assertEqual(self.graph.get_costs(),[-1,6])

    def tearDown(self):
        del self.START
        del self.graph
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()