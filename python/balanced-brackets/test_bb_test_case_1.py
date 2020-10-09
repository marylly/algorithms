import unittest
from balanced_brackets.BalancedBrackets import BalancedBrackets

class Test_Balanced_Brackets(unittest.TestCase):
    START = None
    graph = None

    def test_is_balanced_brackets(self):
        expression = "{{[[(())]]}}"
        bb = BalancedBrackets(expression)
        self.assertEqual(bb.is_balanced_brackets(),'YES')

if __name__ == '__main__':
    unittest.main()