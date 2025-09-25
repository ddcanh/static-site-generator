import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNode(unittest.TestCase):
  def test_text_to_textnodes(self):
    text = "This is some **bold** text with _italic_ and `code`"
    result = text_to_textnodes(text)
    self.assertEqual(
      result,
      [
        TextNode("This is some ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" text with ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" and ", TextType.TEXT),
        TextNode("code", TextType.CODE),
      ],
    )

  def test_text_to_textnodes_2(self):
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    result = text_to_textnodes(text)
    self.assertListEqual(
      result,
      [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
      ]
    )

  def test_text_to_textnodes_simple(self):
    text = "Hello, world!"
    expected = [TextNode("Hello, world!", TextType.TEXT)]
    actual = text_to_textnodes(text)
    self.assertListEqual(actual, expected)

  def test_text_to_textnodes_bold_only(self):
    text = "**Bold text**"
    expected = [TextNode("Bold text", TextType.BOLD)]
    actual = text_to_textnodes(text)
    assert actual == expected, f"Expected {expected}, got {actual}"

  def test_text_to_textnodes_multiple_bold(self):
    text = "This has **multiple** bold **sections**"
    expected = [
        TextNode("This has ", TextType.TEXT),
        TextNode("multiple", TextType.BOLD),
        TextNode(" bold ", TextType.TEXT),
        TextNode("sections", TextType.BOLD)
    ]
    actual = text_to_textnodes(text)
    assert actual == expected, f"Expected {expected}, got {actual}"

  def test_text_to_textnodes_mixed_formats(self):
    text = "A _italic_ and a `code` example"
    expected = [
        TextNode("A ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" and a ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode(" example", TextType.TEXT)
    ]
    actual = text_to_textnodes(text)
    assert actual == expected, f"Expected {expected}, got {actual}"

  def test_text_to_textnodes_empty_text(self):
    text = ""
    expected = []
    actual = text_to_textnodes(text)
    self.assertListEqual(actual, expected)

  def test_text_to_textnodes_whitespace_only(self):
    text = "   \n\t  "
    expected = [TextNode("   \n\t  ", TextType.TEXT)]
    actual = text_to_textnodes(text)
    self.assertListEqual(actual, expected)

  def test_text_to_textnodes_adjacent_formats(self):
    text = "**bold**_italic_`code`"
    expected = [
        TextNode("bold", TextType.BOLD),
        TextNode("italic", TextType.ITALIC),
        TextNode("code", TextType.CODE)
    ]
    actual = text_to_textnodes(text)
    self.assertListEqual(actual, expected)

  def test_text_to_textnodes_nested_formats(self):
    text = "**bold with _italic_ inside**"
    expected = [
        TextNode("bold with ", TextType.BOLD),
        TextNode("italic", TextType.ITALIC),
        TextNode(" inside", TextType.BOLD)
    ]
    actual = text_to_textnodes(text)
    self.assertListEqual(actual, expected)

  def test_text_to_textnodes_multiple_images(self):
    text = "![first image](url1) and ![second image](url2)"
    expected = [
        TextNode("first image", TextType.IMAGE, "url1"),
        TextNode(" and ", TextType.TEXT),
        TextNode("second image", TextType.IMAGE, "url2")
    ]
    actual = text_to_textnodes(text)
    self.assertListEqual(actual, expected)

  def test_text_to_textnodes_multiple_links(self):
    text = "[link1](url1) and [link2](url2)"
    expected = [
        TextNode("link1", TextType.LINK, "url1"),
        TextNode(" and ", TextType.TEXT),
        TextNode("link2", TextType.LINK, "url2")
    ]
    actual = text_to_textnodes(text)
    self.assertListEqual(actual, expected)

  def test_text_to_textnodes_complex_mix(self):
    text = "**Bold** with _italic_ and `code` and ![image](url.image) and [link](url.link)"
    expected = [
        TextNode("Bold", TextType.BOLD),
        TextNode(" with ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" and ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode(" and ", TextType.TEXT),
        TextNode("image", TextType.IMAGE, "url.image"),
        TextNode(" and ", TextType.TEXT),
        TextNode("link", TextType.LINK, "url.link")
    ]
    actual = text_to_textnodes(text)
    self.assertListEqual(actual, expected)

  def test_text_to_textnodes_with_special_chars(self):
    text = "**bold with * and _ and `**"
    expected = [
        TextNode("bold with * and _ and `", TextType.BOLD)
    ]
    actual = text_to_textnodes(text)
    self.assertListEqual(actual, expected)

  def test_text_to_textnodes_with_numbers(self):
    text = "**123** and _456_ and `789`"
    expected = [
        TextNode("123", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("456", TextType.ITALIC),
        TextNode(" and ", TextType.TEXT),
        TextNode("789", TextType.CODE)
    ]
    actual = text_to_textnodes(text)
    self.assertListEqual(actual, expected)

  # def test_text_to_textnodes_complex_nested_formats(self):
  #   text = "This is a **very _complicated_ and `complex`** text with ![image](url) and [link](url) and **more _nested_ `formats`** and some `code with * and _` and _italic with **bold** and `code`_"
  #   expected = [
  #       TextNode("This is a ", TextType.TEXT, None),
  #       TextNode("very ", TextType.BOLD, None),
  #       TextNode("complicated", TextType.ITALIC, None),
  #       TextNode(" and ", TextType.BOLD, None),
  #       TextNode("complex", TextType.CODE, None),
  #       TextNode(" text with ", TextType.TEXT, None),
  #       TextNode("image", TextType.IMAGE, "url"),
  #       TextNode(" and ", TextType.TEXT, None),
  #       TextNode("link", TextType.LINK, "url"),
  #       TextNode(" and ", TextType.TEXT, None),
  #       TextNode("more ", TextType.BOLD, None),
  #       TextNode("nested", TextType.ITALIC, None),
  #       TextNode(" ", TextType.BOLD, None),
  #       TextNode("formats", TextType.CODE, None),
  #       TextNode(" and some ", TextType.TEXT, None),
  #       TextNode("code with * and _", TextType.CODE, None),
  #       TextNode(" and ", TextType.TEXT, None),
  #       TextNode("italic with ", TextType.ITALIC, None),
  #       TextNode("bold", TextType.BOLD, None),
  #       TextNode(" and ", TextType.ITALIC, None),
  #       TextNode("code", TextType.CODE, None),
  #   ]
  #   actual = text_to_textnodes(text)
  #   for item in actual:
  #     print(item)
  #   self.assertListEqual(actual, expected)