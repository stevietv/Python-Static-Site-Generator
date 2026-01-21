import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        new_node = []
        if node.text_type is not TextType.TEXT or node.text.count(delimiter) == 0:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) < 2:
            raise Exception("invalid markdown syntax found")
        
        split_node = node.text.split(delimiter)
        new_node.append(TextNode(split_node[0], TextType.TEXT))
        new_node.append(TextNode(split_node[1], text_type))
        new_node.append(TextNode(split_node[2], TextType.TEXT))

        new_nodes.extend(new_node)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_node = []
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue

        original_text = node.text
        for match in matches:
            image_alt = match[0]
            image_link = match[1]
            split_node = original_text.split(f"![{image_alt}]({image_link})", 1)

            if split_node[0] != "":
                new_node.append(TextNode(split_node[0], TextType.TEXT))
            new_node.append(TextNode(image_alt, TextType.IMAGE, image_link))
            original_text = split_node[1]
        
        if original_text != "":
            new_node.append(TextNode(original_text, TextType.TEXT))

        new_nodes.extend(new_node)                           
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_node = []
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue

        original_text = node.text
        for match in matches:
            link_text = match[0]
            link = match[1]
            split_node = original_text.split(f"[{link_text}]({link})", 1)

            if split_node[0] != "":
                new_node.append(TextNode(split_node[0], TextType.TEXT))
            new_node.append(TextNode(link_text, TextType.LINK, link))
            original_text = split_node[1]
        
        if original_text != "":
            new_node.append(TextNode(original_text, TextType.TEXT))

        new_nodes.extend(new_node)                           
    return new_nodes