from textnode import TextNode, TextType

from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        text = old_node.text
        if delimiter not in text:
            new_nodes.append(old_node)
            continue
            
        # Find all delimiter positions
        delimiter_positions = []
        pos = 0
        while True:
            pos = text.find(delimiter, pos)
            if pos == -1:
                break
            delimiter_positions.append(pos)
            pos += len(delimiter)
            
        if len(delimiter_positions) % 2 != 0:
            new_nodes.append(old_node)
            continue
        # Process text between delimiters
        current_pos = 0
        for i in range(0, len(delimiter_positions), 2):
            start = delimiter_positions[i]
            end = delimiter_positions[i + 1]
            
            # Add text before the first delimiter
            if start > current_pos:
                new_nodes.append(TextNode(text[current_pos:start], old_node.text_type))
                
            # Add the delimited text, preserving all characters
            delimited_text = text[start + len(delimiter):end]
            new_nodes.append(TextNode(delimited_text, text_type))
            current_pos = end + len(delimiter)
            
        # Add any remaining text
        if current_pos < len(text):
            new_nodes.append(TextNode(text[current_pos:], old_node.text_type))
                
    return new_nodes
    

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
      if node.text_type != TextType.TEXT:
        new_nodes.append(node)
      else:
        text = node.text
        images_matches = extract_markdown_images(text)
        if len(images_matches) == 0:
          new_nodes.append(node)
          continue
        for match in images_matches:
          image_alt = match[0]
          image_link = match[1]
          sections = text.split(f"![{image_alt}]({image_link})", 1) 
          if sections[0] != "":
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
          new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1])) 
          text = sections[1]
        if text != "":
          new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
      if node.text_type != TextType.TEXT:
        new_nodes.append(node)
      else:
        text = node.text
        links_matches = extract_markdown_links(text)
        if len(links_matches) == 0:
          new_nodes.append(node)
          continue
        for match in links_matches:
          image_alt = match[0]
          image_link = match[1]
          sections = text.split(f"[{image_alt}]({image_link})", 1) 
          if sections[0] != "":
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
          new_nodes.append(TextNode(match[0], TextType.LINK, match[1])) 
          text = sections[1]
        if text != "":
          new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

