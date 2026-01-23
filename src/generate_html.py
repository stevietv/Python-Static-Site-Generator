from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from inline_markdown import text_to_text_nodes
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import text_node_to_html_node
import os

def markdown_to_html_node(markdown):
    children=[]
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        htmlnode = None
        blocktype = block_to_block_type(block)
        if blocktype == BlockType.HEADING:
            node = create_heading(block)
        elif blocktype == BlockType.CODE:
            node = create_codeblock(block)
        elif blocktype == BlockType.QUOTE:
            node = create_quoteblock(block)
        elif (blocktype == BlockType.UNORDERED_LIST) or (blocktype == BlockType.ORDERED_LIST):
            node = create_list(block, blocktype)
        else:
            node = create_paragraph(block)

        children.append(node)

    return ParentNode("div", children)

def create_heading(markdown):
    space = markdown.find(" ")
    heading_level = markdown.count("#", 0, space)
    split = markdown.split(" ", 1)
    children = text_to_children(split[1])
    return ParentNode(f"h{heading_level}", children)

def create_codeblock(markdown):
    text = markdown.replace("```", "")
    if text.startswith("\n"):
        text = text[1:]
    node = LeafNode("code", text)
    parent = ParentNode("pre", [node])
    return parent

def create_quoteblock(markdown):
    lines = markdown.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
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
    lines = markdown.split("\n")
    text = " ".join(lines)
    nodes = text_to_children(text)
    parent = ParentNode("p", nodes)
    return parent

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    html_nodes = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)
    return html_nodes

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    title = ""
    for block in blocks:
        if block_to_block_type(block) is not BlockType.HEADING:
            continue
            
        space = block.find(" ")
        heading_level = block.count("#", 0, space)
        if heading_level == 1:
            split = block.split(" ", 1)
            title = split[1].strip()
            break
    
    if title == "":
        raise Exception("No H1 found in markdown")
    return title

