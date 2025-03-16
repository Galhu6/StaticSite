import json
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        
    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def props_to_html(self):
        return "".join(f' {key}="{value}"' for key, value in self.props.items())
    def __repr__(self):
        return(f'HTMLNode(tag="{self.tag}", value={self.value}, children={len(self.children)}, props={self.props})')
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        if value is None:
            raise ValueError("All leaf nodes must have a value.")
        super().__init__(tag, value, props = props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        props_str = self.props_to_html()
        return  f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f'LeafNode(tag="{self.tag}", value="{self.value}", props={self.props})'