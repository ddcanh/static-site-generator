
import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
  def test_extract_title(self):
    md = """
          # This is a heading
        """
    self.assertEqual(extract_title(md), "This is a heading")