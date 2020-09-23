class Graph(object):
    nodes = {}
    qtd_levels = 0
    current_level = 0

    def __init__(self, expression):
        self.expression = expression
        self.create_nodes(self.expression)

    def get_expression_length(self):
        return len(self.expression)

    def get_current_level(self):
        return self.current_level

    def get_levels_qtd(self):
        return len(self.nodes)

    def create_nodes(self, expression):
        brackets = list(expression)
        for bracket in range(0, self.get_expression_length()):
            self.add_bracket(brackets[bracket])

    def add_bracket(self, bracket):
        if bracket in "{[(":
            if(self.current_level in self.nodes):
                if self.nodes.get(self.current_level)[-1] in '{[(':
                    self.current_level = self.current_level + 1
                    self.qtd_levels = self.qtd_levels + 1

        if self.last_is_closing_bracket(bracket):
            self._closing_level_brackets(bracket)
        
        self.nodes.setdefault(self.current_level, []).append(bracket)

    def _closing_level_brackets(self, bracket):
        if self.current_level <= self.qtd_levels and self.current_level >= 1:
            if bracket in ')' and self.nodes.get(self.current_level)[-1] != '(':
                self.current_level = self.current_level - 1
            elif bracket in ']' and self.nodes.get(self.current_level)[-1] != ']':
                self.current_level = self.current_level - 1
            elif bracket in '}' and self.nodes.get(self.current_level)[-1] != '}':
                self.current_level = self.current_level - 1

    def last_is_closing_bracket(self, bracket):
        return bracket in ')]}'

    def get_nodes(self):
        return self.nodes

    def is_balanced_brackets(self):
        balanced = 'YES'
        for level in range(0, self.get_levels_qtd() - 1):
            if level not in self.nodes:
                balanced = 'NO'
                break

            if len(self.nodes[level]) % 2 == 1:
                balanced = 'NO'
                break

            if any(pair not in '{}|[]|()|}{|][|)(' for pair in self.nodes[level]):
                balanced = 'NO'
                break
        return balanced