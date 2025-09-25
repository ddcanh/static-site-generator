import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_eq_not_equal2(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a text node 2", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, TextType.BOLD, None)")
    
    def test_text(self):
      node = TextNode("This is a text node", TextType.TEXT)
      html_node = TextNode.text_node_to_html_node(node)
      self.assertEqual(html_node.tag, None)
      self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")
    
    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>This is an italic node</i>")

    def test_text_node_to_html_node_underline(self):
        node = TextNode("This is an underline node", TextType.UNDERLINE)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<u>This is an underline node</u>")

    def test_text_node_to_html_node_strikethrough(self):
        node = TextNode("This is a strikethrough node", TextType.STRIKETHROUGH)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<s>This is a strikethrough node</s>")
    
    def test_text_node_to_html_node_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")
    
    def test_text_node_to_html_node_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.boot.dev">This is a link node</a>')

    def test_text_node_to_html_node_image(self):  
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.boot.dev/image.jpg")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.boot.dev/image.jpg" alt="This is an image node"></img>')

if __name__ == "__main__":
    unittest.main()