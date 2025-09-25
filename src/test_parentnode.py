import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):  
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

  def test_to_html_with_props(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node], {"class": "container"})
    self.assertEqual(
        parent_node.to_html(),
        '<div class="container"><span>child</span></div>',
    )   

  def test_to_html_with_props_and_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node, LeafNode("","grandchild text")])
    parent_node = ParentNode("div", [child_node, grandchild_node], {"class": "container"})
    self.assertEqual(
        parent_node.to_html(),
        '<div class="container"><span><b>grandchild</b>grandchild text</span><b>grandchild</b></div>',
    )


  def test_to_html_no_children(self):
    with self.assertRaises(ValueError):
      parent_node = ParentNode("div", [])
      parent_node.to_html() 

  def test_to_html_no_tag(self):
    with self.assertRaises(ValueError):
      parent_node = ParentNode(None, ["child"])
      parent_node.to_html()