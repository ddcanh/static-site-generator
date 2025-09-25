from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if not self.tag:
      raise ValueError("Tag is required")
    if not self.children:
      raise ValueError("Children are required")
    props_value = self.props_to_html()
    if not props_value:
      return f"<{self.tag}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
    return f"<{self.tag} {props_value}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"