import unittest
from block_type import BlockType, block_to_block_type  # import your implementation

class TestBlockTypes(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a simple paragraph with no special formatting."
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)
        # Paragraph with characters that might be confused with other block types
        self.assertEqual(block_to_block_type("A paragraph with # but not at the start"), BlockType.paragraph)
        self.assertEqual(block_to_block_type("A paragraph with > but not at the start of every line"), BlockType.paragraph)
  
        
    def test_heading(self):
        # Test different heading levels
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.heading)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.heading)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.heading)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.heading)
        
        # Not a heading - more than 6 #s
        self.assertEqual(block_to_block_type("####### Not a heading"), BlockType.paragraph)
        
        # Not a heading - no space after #
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.paragraph)

        
    def test_code_block(self):
        code = "```\ndef hello():\n    print('hello')\n```"
        self.assertEqual(block_to_block_type(code), BlockType.code)

         # Simple code block
        self.assertEqual(block_to_block_type("```\ncode here\n```"), BlockType.code)
        
        # Multi-line code block
        self.assertEqual(block_to_block_type("```\ndef hello():\n    print('hello')\n```"), BlockType.code)

        
    def test_quote(self):
        quote = "> This is a quote\n> It spans multiple lines"
        self.assertEqual(block_to_block_type(quote), BlockType.quote)
        
    def test_unordered_list(self):
        unordered = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(unordered), BlockType.unordered_list)
        
    def test_ordered_list(self):
        ordered = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(ordered), BlockType.ordered_list)
        