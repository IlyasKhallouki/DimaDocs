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
        self.attr = attr if attr is not None else {}
        self.parent = parent
        self.children = children if children is not None else []
        self.depth = depth
        self.is_self_closing = is_self_closing

    # A better print for the element
    def __str__(self):
        indent = "  " * self.depth  # Indentation based on depth
        attrs = ', '.join(f'{key}="{value}"' for key, value in self.attr.items())
        attrs_str = f" [{attrs}]" if attrs else ""
        
        content_str = f": {self.content}" if self.content else ""
        
        # Print the element and its children
        result = f"{indent}<{self.tag}{attrs_str}{content_str}>"
        
        for child in self.children:
            result += f"\n{str(child)}"  # Recursive call for children
        
        if self.children:  # If there are children, close the tag
            result += f"\n{indent}</{self.tag}>"
        
        return result

    def __repr__(self):
        return f"Element(tag='{self.tag}', content='{self.content}', attributes={self.attr}, depth={self.depth})"
