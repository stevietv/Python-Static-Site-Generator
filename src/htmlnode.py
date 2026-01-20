class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        prop_string = ""
        if self.props:
            for prop in self.props:
                prop_string += f' {prop}="{self.props[prop]}"'
        return prop_string
        
    def __eq__(self, other):
        return (self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"