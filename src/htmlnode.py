
class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    if self.children:
      return f"<{self.tag}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
    else:
      return f"<{self.tag}>{self.value}</{self.tag}>"
  
  def props_to_html(self):
    if self.props:
      return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    return ""
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  
  