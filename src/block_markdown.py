import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(markdown):
    if re.match(r"^#{1,6} .+$", markdown):
        return BlockType.HEADING
    if re.match(r"^```\n(?:[^\n]*\n)*[^\n]*```$", markdown):
        return BlockType.CODE
    if re.match(r"^(?:>\s*.+\n)*>\s*.+$", markdown):
        return BlockType.QUOTE
    if re.match(r"^(?:- .+\n)*- .+$", markdown):
        return BlockType.UNORDERED_LIST
    if re.match(r"^(?:\d+\. .+\n)*\d+\. .+$", markdown):
        splits = markdown.split("\n")
        is_sequential = True

        for i, line in enumerate(splits):
            number_str = line.split(".", 1)[0]
            if int(number_str) != i + 1:
                is_sequential = False
                break

        if is_sequential:
            return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
    
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    output_blocks = []

    for block in blocks:
        output = block.strip()
        if output != "":
            output_blocks.append(output)
    
    return output_blocks