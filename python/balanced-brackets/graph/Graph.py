class Graph(object):
    nodes = {}
    qtd_levels = 0
    current_level = 0
    tail = None

    def __init__(self, expression):
        self.expression = expression
        self.create_nodes(self.expression)

    def get_expression_length(self):
        return len(self.expression)

    def get_current_level(self):
        return self.current_level

    def get_levels_qtd(self):
        return self.qtd_levels

    def create_nodes(self, expression):
        brackets = list(expression)
        for bracket in range(0, self.get_expression_length()):
            self.add_bracket(brackets[bracket])

    def add_bracket(self, bracket):
        if bracket in "{[(":
            self.current_level = self.current_level + 1
            self.qtd_levels = self.qtd_levels + 1

        if bracket in ")]}":
            if self.last_is_closing_bracket():
                self.current_level = self.current_level - 1
        
        self.nodes.setdefault(self.current_level, []).append(bracket)
        self.tail = bracket

    def last_is_closing_bracket(self):
        return self.tail in ')]}'

    def get_nodes(self):
        return self.nodes

    def is_balanced_brackets(self):
        balanced = 'YES'
        for level in range(1, self.get_levels_qtd()):
            if level not in self.nodes:
                balanced = 'NO'
                break

            print('to aqui', level, self.nodes[level])
            if ''.join(self.nodes[level]) not in '{}|[]|()|}{|][|)(':
                balanced = 'NO'
                break
        print(self.nodes)
        return balanced