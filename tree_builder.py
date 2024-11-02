from element import Element
from bs4 import BeautifulSoup

class TreeBuilder:
    def __init__(self):
        self.element_tree: Element = None
        self.depth = 0

    def parse_tree(self, page: str):
        bs4 = BeautifulSoup(page, 'html.parser')

        # Set the first section as the root
        # Will be changed to be dynamic later
        root = bs4.find('section')
        
        if root:
            self.element_tree = self.build_element_tree(root)

        # Calculate the depth of the tree
        self.get_depth(self.element_tree)

    def build_element_tree(self, soup_element) -> Element:
        # Create the Element instance for the current node
        current_element = Element(
            tag=soup_element.name,
            content=soup_element.get_text(strip=True) if soup_element.get_text(strip=True) and soup_element.name in ['p', 'h1', 'h2'] else None,
            attr=soup_element.attrs,
            children=[], 
            depth=self.depth,
            is_self_closing=False # TODO: implement logic for determining if it's self closing
        )

        self.depth += 1

        for child in soup_element.find_all(recursive=False):  
            child_element = self.build_element_tree(child)
            current_element.children.append(child_element)

        self.depth -= 1

        return current_element

    def get_depth(self, element: Element):
        if element is not None:
            self.depth = max(self.depth, element.depth + 1)  # Update max depth

        # Iterate through children to find their depths
        for child in element.children:
            self.get_depth(child)
