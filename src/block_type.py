from enum import Enum

class BlockType(Enum):
  paragraph = "paragraph"
  heading = "heading"
  quote = "quote"
  code = "code"
  unordered_list = "unordered_list"
  ordered_list = "ordered_list"

def block_to_block_type(block: str):
    lines = block.split("\n")
    
    # Check for code block
    if len(lines) >= 2 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.code
    
    # Check for heading (must be single line)
    if len(lines) == 1:
        line = lines[0]
        if line.startswith("#"):
            for i in range(1, 7):
                if line.startswith("#" * i + " "):
                    return BlockType.heading
    
    # Check for quote block
    if all(line.startswith(">") for line in lines):
        return BlockType.quote
    
    # Check for unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.unordered_list
    
    # Check for ordered list
    if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, 1)):
        return BlockType.ordered_list
    
    # Default to paragraph
    return BlockType.paragraph
  