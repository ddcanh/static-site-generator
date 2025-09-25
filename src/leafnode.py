from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if self.value is None:
      raise ValueError("Value is required")
    if not self.tag:
      return f"{self.value}"
    props_value = self.props_to_html()
    if props_value:
      return f"<{self.tag} {props_value}>{self.value}</{self.tag}>"
    return f"<{self.tag}>{self.value}</{self.tag}>"