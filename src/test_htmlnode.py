import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
  def test_props_to_html(self):
    node = HTMLNode("div", "This is a div", None, {"class": "container"})
    self.assertEqual(node.props_to_html(), 'class="container"')

  def test_props_to_html_none(self):
    node = HTMLNode("div", "This is a div", None, None)
    self.assertEqual(node.props_to_html(), '')

  def test_props_to_html_empty(self):
    node = HTMLNode("div", "This is a div", None, {})
    self.assertEqual(node.props_to_html(), '')


if __name__ == "__main__":
    unittest.main()