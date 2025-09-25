from block_type import BlockType, block_to_block_type
from blocks_markdown import markdown_to_blocks
from htmlnode import HTMLNode
from text_to_textnodes import text_to_textnodes
from textnode import TextNode
import textwrap


def markdown_to_html_node(markdown: str):
    # Remove common leading indentation from triple-quoted test strings
    markdown = textwrap.dedent(markdown)
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.heading:
            # Count the number of # to determine heading level
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break
            # Remove the # and space from the beginning
            text = block[level + 1:].strip()
            children.append(HTMLNode(tag=f"h{level}", children=text_to_children(text)))
            
        elif block_type == BlockType.paragraph:
            # Replace internal newlines with spaces to form proper paragraphs
            para_text = block.replace("\n", " ")
            children.append(HTMLNode(tag="p", children=text_to_children(para_text)))
            
        elif block_type == BlockType.quote:
            # Remove the > from the beginning of each line
            lines = block.split("\n")
            text = "\n".join(line[1:].strip() for line in lines)
            children.append(HTMLNode(tag="blockquote", children=text_to_children(text)))
            
        elif block_type == BlockType.code:
            # Remove the ``` fence lines and preserve inner newlines and trailing newline
            lines = block.split("\n")
            inner_lines = lines[1:-1]
            text = "\n".join(inner_lines)
            if not text.endswith("\n"):
                text = text + "\n"
            children.append(HTMLNode(tag="pre", children=[HTMLNode(tag="code", value=text)]))
            
        elif block_type == BlockType.unordered_list:
            # Split into lines and remove the - from the beginning of each
            lines = block.split("\n")
            list_items = []
            for line in lines:
                text = line[2:].strip()  # Remove "- " from the beginning
                list_items.append(HTMLNode(tag="li", children=text_to_children(text)))
            children.append(HTMLNode(tag="ul", children=list_items))
            
        elif block_type == BlockType.ordered_list:
            # Split into lines and remove the number and dot from the beginning of each
            lines = block.split("\n")
            list_items = []
            for line in lines:
                # Find the first dot and space after the number
                dot_index = line.find(". ")
                text = line[dot_index + 2:].strip()  # Remove "N. " from the beginning
                list_items.append(HTMLNode(tag="li", children=text_to_children(text)))
            children.append(HTMLNode(tag="ol", children=list_items))
    
    return HTMLNode(tag="div", children=children)

def text_to_children(text: str):
  children = []
  text_nodes = text_to_textnodes(text)
  for text_node in text_nodes:
    children.append(TextNode.text_node_to_html_node(text_node))
  return children

