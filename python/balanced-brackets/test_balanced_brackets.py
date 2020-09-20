import unittest
from balanced_brackets.BalancedBrackets import BalancedBrackets

class Test_Balanced_Brackets(unittest.TestCase):
    START = None
    graph = None

    def setUp(self):
        return super().setUp()

    def test_expression_length(self):
        expression = "{{[[(())]]}}"
        bb = BalancedBrackets(expression)
        self.assertEqual(bb.get_lenght(),12)

    def test_qtd_brackets_pairs(self):
        expression = "{{[[(())]]}}"
        bb = BalancedBrackets(expression)
        self.assertEqual(bb.get_qtd_brackets_pairs(),6)

    def test_get_brackets(self):
        expression = "{{[[(())]]}}"
        bb = BalancedBrackets(expression)
        self.assertEqual(bb.get_brackets(),['{','{','[','[','(','(',')',')',']',']','}','}'])

    def test_get_opened_brackets(self):
        expression = "{{[[(())]]}}"
        bb = BalancedBrackets(expression)
        self.assertEqual(bb.get_opened_brackets(),['{','{','[','[','(','('])

    def test_get_closing_brackets(self):
        expression = "{{[[(())]]}}"
        bb = BalancedBrackets(expression)
        self.assertEqual(bb.get_closing_brackets(),[')',')',']',']','}','}'])

    def test_is_balanced_brackets(self):
        expression = "{{[[(())]]}}"
        bb = BalancedBrackets(expression)
        self.assertEqual(bb.is_balanced_brackets(),'YES')

    def tearDown(self):
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()