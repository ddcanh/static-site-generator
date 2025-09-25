def markdown_to_blocks(markdown: str) -> list[str]:
    # Split the markdown text into lines
    lines = markdown.split('\n')
    
    # Initialize blocks list and current block
    blocks = []
    current_block = []
    
    # Process each line
    for line in lines:
        # If line is empty and we have content in current_block
        if not line.strip() and current_block:
            # Join the current block and add it to blocks
            blocks.append('\n'.join(current_block))
            current_block = []
        # If line is not empty, add it to current block
        elif line.strip():
            current_block.append(line)
    
    # Add the last block if it exists
    if current_block:
        blocks.append('\n'.join(current_block))
    
    return blocks
