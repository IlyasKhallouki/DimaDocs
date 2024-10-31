from typing import Optional, List

class Element:
    def __init__(self, tag: str,
                 content: Optional[str] = None, 
                 attr: Optional[dict] = None, 
                 parent: Optional['Element'] = None, 
                 children: List['Element'] = None, 
                 depth: int = 0, 
                 is_self_closing: bool = False):
        
        self.content = content
        self.tag = tag
        self.attr = attr
        self.parent = parent
        self.children = children
        self.depth = depth
        self.is_self_closing = is_self_closing
    