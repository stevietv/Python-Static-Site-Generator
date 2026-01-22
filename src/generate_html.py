from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from inline_markdown import text_to_text_nodes
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    container = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        htmlnode = None
        blocktype = block_to_block_type(block)
        if blocktype == BlockType.HEADING:
            node = create_heading(block)
        if blocktype == BlockType.CODE:
            node = create_codeblock(block)
        if blocktype == BlockType.QUOTE:
            node = create_quoteblock(block)
        if (blocktype == BlockType.UNORDERED_LIST) or (blocktype == BlockType.ORDERED_LIST):
            node = create_list(block, blocktype)
        else:
            node = create_paragraph(block)

        container.children.append(node)

    print(container.to_html())


# need to process the text using inline markdown function

def create_heading(markdown):
    space = markdown.find(" ")
    heading_level = markdown.count("#", 0, space)
    split = markdown.split(" ", 1)
    children = text_to_children(split[1])
    return ParentNode(f"h{heading_level}", children)

def create_codeblock(markdown):
    node = LeafNode("code", markdown[3:-4])
    parent = ParentNode("pre", node)
    return parent

def create_quoteblock(markdown):
    splits = markdown.split("> ")
    children = []
    for split in splits:
        if split != "":
            children.append(text_to_children(split))
    return ParentNode("blockquote", children)

def create_list(markdown, list_type):
    list_items = []
    list_rows = markdown.split("\n")
    for row in list_rows:
        if list_type == BlockType.UNORDERED_LIST:
            list_items.append(ParentNode("li", text_to_children(row[2:])))
        else:
            space = markdown.find(" ")
            list_items.append(ParentNode("li", text_to_children(row[space + 1:])))
    if list_type == BlockType.UNORDERED_LIST:
        parent = ParentNode("ul", list_items)
    else:
        parent = ParentNode("ol", list_items)
    return parent

def create_paragraph(markdown):
    text = markdown.replace("\n", " ")
    nodes = text_to_children(text)
    parent = ParentNode("p", nodes)
    return parent

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

markdown_to_html_node("""
- item 1
- item _2_

this is **a** paragraph with an ![image](https://imgur.com/1.png)""")