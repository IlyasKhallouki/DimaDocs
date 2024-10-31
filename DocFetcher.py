from tree_builder import TreeBuilder
import requests
from typing import Optional
from element import Element

class DocFetcher:
    def __init__(self, url):
        self.url = url
        
        self.html: Optional[str] = None
        self.tree: Optional[Element] = None

        self.fetch_HTML()
        self.parse_HTML()

    def fetch_HTML(self):
        response = requests.get(self.url)
        return response.content
    
    def parse_HTML(self):
        tb = TreeBuilder()
        tb.parse_tree(self.html)
        self.tree = tb.element_tree
