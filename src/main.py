from extract_markdown import extract_markdown_images
from textnode import TextNode, TextType


def main():
  textNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
  print(textNode)
  text = "This is text with a ![alt text1](https://url.com/image.jpg) and ![alt text2](https://url.com/image.jpg)"
  result = extract_markdown_images(text)
 
  print("===========")
  print(result)

if __name__ == "__main__":
  main()
