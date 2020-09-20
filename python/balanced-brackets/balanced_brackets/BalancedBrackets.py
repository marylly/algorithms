import math
import shlex

class BalancedBrackets(object):

    def __init__(self, expression):
        self.expression = expression

    def get_lenght(self):
        return len(self.expression)

    def get_qtd_brackets_pairs(self):
        return math.floor(self.get_lenght()/2)

    def get_brackets(self):
        return list(self.expression)

    def get_opened_brackets(self):
        return [bracket for bracket in self.get_brackets() if bracket in '([{']

    def get_closing_brackets(self):
        return [bracket for bracket in self.get_brackets() if bracket in ')]}']

    def is_balanced_brackets(self):
        balanced = 'YES'
        opened = self.get_opened_brackets()
        closed = self.get_closing_brackets()
        qtd_pairs = self.get_qtd_brackets_pairs() - 1
        for pair_brackets in range(0, qtd_pairs):
            if opened[pair_brackets]+closed[qtd_pairs - pair_brackets] not in '()[]{}':
                balanced = 'NO'

        return balanced