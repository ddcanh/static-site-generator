import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  def test_to_html_div(self):
    node = LeafNode("div", "This is a div", {"class": "container"})
    self.assertEqual(node.to_html(), '<div class="container">This is a div</div>')