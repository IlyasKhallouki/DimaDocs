from element import Element

class TreeBuilder:
    def __init__(self):
        self.element_tree: Element = None
        self.depth = 0

    def parse_tree(self, page):
        self.element_tree = None
        self.get_depth()
    
    def get_depth(self):
        self.depth = 0