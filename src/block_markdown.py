def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    output_blocks = []

    for block in blocks:
        output = block.strip()
        if output != "":
            output_blocks.append(output)
    
    return output_blocks