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