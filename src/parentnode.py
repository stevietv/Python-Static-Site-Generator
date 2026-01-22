from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode is missing a tag")
        if self.children is None:
            raise ValueError("ParentNode is missing children")
        
        html_string = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            html_string += child.to_html()
        html_string += f'</{self.tag}>'

        return html_string
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"