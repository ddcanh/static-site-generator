import unittest
from blocks_markdown import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
  def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )

  def test_markdown_to_blocks_simple(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"""
        
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
            ]
        )

  def test_markdown_to_blocks_empty(self):
        markdown = ""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [])

  def test_markdown_to_blocks_whitespace(self):
        markdown = """   # Heading with spaces   

Paragraph with spaces   at the end   

- List item with spaces   """
        
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "   # Heading with spaces   ",
                "Paragraph with spaces   at the end   ",
                "- List item with spaces   "
            ]
        )

  def test_markdown_to_blocks_multiple_blank_lines(self):
        markdown = """# First heading


# Second heading



# Third heading"""
        
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "# First heading",
                "# Second heading",
                "# Third heading"
            ]
        )

  def test_markdown_to_blocks_no_blank_lines(self):
        markdown = """# Heading
This is a paragraph
- List item 1
- List item 2"""
        
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "# Heading\nThis is a paragraph\n- List item 1\n- List item 2"
            ]
        )

  def test_markdown_to_blocks_with_code_blocks(self):
        markdown = """# Heading

This is a paragraph with `code` in it.

```
def hello():
    print("Hello, world!")
```

- List item"""
        
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "# Heading",
                "This is a paragraph with `code` in it.",
                "```\ndef hello():\n    print(\"Hello, world!\")\n```",
                "- List item"
            ]
        )

