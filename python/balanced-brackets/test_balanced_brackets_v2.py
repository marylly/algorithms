import unittest
from graph.Graph import Graph

class Test_Balanced_Brackets_v2(unittest.TestCase):

    # def test_get_expression_length(self):
    #     expression = "{{[[(()]]]}}"
    #     graph = Graph(expression)
    #     self.assertEqual(graph.get_expression_length(),12)

    # def test_create_one_level_tree(self):
    #     expression = "()"
    #     graph = Graph(expression)
    #     self.assertEqual(graph.get_current_level(),0)

    # def test_create_one_level_tree(self):
    #     expression = "[()]"
    #     graph = Graph(expression)
    #     self.assertEqual(graph.get_levels_qtd(),2)

    # def test_get_nodes(self):
    #     expression = "([])"
    #     graph = Graph(expression)
    #     self.assertEqual(graph.get_nodes(),{1: ['(',')'], 2: ['[',']']})

    # def test_get_nodes_01(self):
    #     expression = "{{([])}}"
    #     graph = Graph(expression)
    #     self.assertEqual(graph.get_nodes(),{1: ['{','}'], 2: ['{','}'], 3: ['(',')'], 4: ['[',']']})

    def test_is_balanced_brackets(self):
        # expression = "{[()]}" #YES - Ok
        # expression = "{[(])}" #NO - Ok
        # expression = "{{[[(())]]}}" #YES
        # expression = "{{([])}}" #YES
        # expression = "{{)[](}}" #YES
        # expression = "{(([])[])[]}" #YES
        # expression = "{(([])[])[]]}" #NO - Ok
        # expression = "{(([])[])[]}[]" #YES
        expression = "{[(())]}[]" #YES - Ok
        graph = Graph(expression)
        self.assertEqual(graph.is_balanced_brackets(),'YES')     

if __name__ == '__main__':
    unittest.main()