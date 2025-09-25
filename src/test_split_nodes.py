import unittest

from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestConverter(unittest.TestCase):
  def test_split_nodes_delimiter_code(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(
       new_nodes,
        [
          TextNode("This is text with a ", TextType.TEXT, None),
          TextNode("code block", TextType.CODE, None),
          TextNode(" word", TextType.TEXT, None),
        ],
    )

    # Test with backticks for code
    node = TextNode("Text with `code` in it", TextType.TEXT)
    result = split_nodes_delimiter([node], "`", TextType.CODE)
    # Should return 3 nodes: text, code, text
    self.assertEqual(
        result,
        [
          TextNode("Text with ", TextType.TEXT),
          TextNode("code", TextType.CODE),
          TextNode(" in it", TextType.TEXT),
        ],  
    )

    # Test with double asterisks for bold
    node = TextNode("Text with **bold** in it", TextType.TEXT)
    result = split_nodes_delimiter([node], "**", TextType.BOLD)
    # Should return 3 nodes: text, bold, text
    self.assertEqual(
        result,
        [
          TextNode("Text with ", TextType.TEXT),
          TextNode("bold", TextType.BOLD),
          TextNode(" in it", TextType.TEXT),
        ],
    )

    # Test with underscores for italic
    node = TextNode("Text with _italic_ in it", TextType.TEXT)
    result = split_nodes_delimiter([node], "_", TextType.ITALIC)
    # Should return 3 nodes: text, italic, text
    self.assertEqual(
        result,
        [
          TextNode("Text with ", TextType.TEXT),
          TextNode("italic", TextType.ITALIC),
          TextNode(" in it", TextType.TEXT),
        ],
    )

  def test_split_nodes_delimiter_multiple(self):
    node = TextNode("Start `code1` middle `code2` end", TextType.TEXT)
    result = split_nodes_delimiter([node], "`", TextType.CODE)
    # Should return 5 nodes
    self.assertEqual(
        result,
        [
          TextNode("Start ", TextType.TEXT),
          TextNode("code1", TextType.CODE),
          TextNode(" middle ", TextType.TEXT),
          TextNode("code2", TextType.CODE),
          TextNode(" end", TextType.TEXT),
        ],
    )

  def test_split_nodes_delimiter_mixed_node(self):
    nodes = [
      TextNode("Text with `code`", TextType.TEXT),
      TextNode("Already bold", TextType.BOLD)
    ]
    result = split_nodes_delimiter(nodes, "`", TextType.CODE)
    # Should properly handle the TEXT node and leave the BOLD node as is
    self.assertEqual(
        result,
        [
          TextNode("Text with ", TextType.TEXT),
          TextNode("code", TextType.CODE),
          TextNode("Already bold", TextType.BOLD),
        ],
    )

  def test_split_nodes_delimiter_edge_cases(self):
    # Empty string
    node = TextNode("", TextType.TEXT)
    result = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(result, [node])

    # No delimiters present
    node = TextNode("Plain text without delimiters", TextType.TEXT)
    result = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(result, [node])

  ### Test split_nodes_image
  def test_split_nodes_image_1(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

  ### Test split_nodes_link
  def test_split_nodes_link_1(self):
    node = TextNode(
        "This is text with a [link](https://www.boot.dev) and another [second link](https://www.boot.dev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link", TextType.LINK, "https://www.boot.dev"
            ),
        ],
        new_nodes,
    )

  # Test when there are no images/links
  def test_no_images(self):
    node = TextNode(
        "This is text without any images.",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [TextNode("This is text without any images.", TextType.TEXT)],
        new_nodes,
    )

  # Test for consecutive images
  def test_consecutive_images(self):
    node = TextNode(
        "Here are two images back-to-back ![image1](https://i.imgur.com/img1.png)![image2](https://i.imgur.com/img2.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("Here are two images back-to-back ", TextType.TEXT),
            TextNode("image1", TextType.IMAGE, "https://i.imgur.com/img1.png"),
            TextNode("image2", TextType.IMAGE, "https://i.imgur.com/img2.png"),
        ],
        new_nodes,
    )

  # Test malformed markdown (e.g., missing `![`)
  def test_malformed_image(self):
    node = TextNode(
        "This is text with a malformed image [image1](https://i.imgur.com/img1.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [TextNode("This is text with a malformed image [image1](https://i.imgur.com/img1.png)", TextType.TEXT)],
        new_nodes,
    )