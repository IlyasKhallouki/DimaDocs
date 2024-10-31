class TreeBuilder:
    def __init__(self, page):
        self.page = page
        self.element_tree = None
        self.depth = 0

    def parse_tree(self):
        self.element_tree = None
    
    def get_depth(self):
        self.depth = 0