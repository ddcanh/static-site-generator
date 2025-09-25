import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
  def test_extract_markdown_images(self):
    text = "![alt text](https://url.com/image.jpg)"
    result = extract_markdown_images(text)
    self.assertEqual(result, [("alt text", "https://url.com/image.jpg")])

    text = "This is text with a ![alt text1](https://url.com/image.jpg) and ![alt text2](https://url.com/image.jpg)"
    result = extract_markdown_images(text)
    self.assertEqual(
        result,
        [
            ("alt text1", "https://url.com/image.jpg"), ("alt text2", "https://url.com/image.jpg")
        ],
    )

  def test_extract_markdown_images2(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


  def test_extract_markdown_link(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    result = extract_markdown_links(text)
    self.assertListEqual(
      result,
      [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    )