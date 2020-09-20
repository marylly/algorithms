import unittest
from balanced_brackets.BalancedBrackets import BalancedBrackets

class Test_Balanced_Brackets(unittest.TestCase):
    expression = None
    bb = None

    def setUp(self):
        self.expression = "{{[[(())]]}}"
        self.bb = BalancedBrackets(self.expression)
        return super().setUp()

    def test_expression_length(self):
        self.assertEqual(self.bb.get_lenght(),12)

    def test_qtd_brackets_pairs(self):
        self.assertEqual(self.bb.get_qtd_brackets_pairs(),6)

    def test_get_brackets(self):
        self.assertEqual(self.bb.get_brackets(),['{','{','[','[','(','(',')',')',']',']','}','}'])

    def test_get_opened_brackets(self):
        self.assertEqual(self.bb.get_opened_brackets(),['{','{','[','[','(','('])

    def test_get_closing_brackets(self):
        self.assertEqual(self.bb.get_closing_brackets(),[')',')',']',']','}','}'])

    def test_is_balanced_brackets(self):
        self.assertEqual(self.bb.is_balanced_brackets(),'YES')

    def tearDown(self):
        self.expression = None
        self.bb = None
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()