from warnings import warn
from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        html_node = LeafNode(None, text_node.text)
        return html_node
    elif text_node.text_type == TextType.BOLD:
        html_node = LeafNode("b", text_node.text)
        return html_node
    elif text_node.text_type == TextType.ITALIC:
        html_node = LeafNode("i", text_node.text)
        return html_node
    elif text_node.text_type == TextType.CODE:
        html_node = LeafNode("code", text_node.text)
        return html_node
    elif text_node.text_type == TextType.LINK:
        html_node = LeafNode("a", text_node.text, {"href": text_node.url},)
        return html_node
    elif text_node.text_type == TextType.IMAGE:
        html_node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text},)
        return html_node
    else:
        raise Exception("Unknown text type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type.value != "text":
            return node
        else:
            parts = node.text.split(delimiter)
            if len(parts) != 3:
                raise Exception("invalid md syntax")
            else:
                new_node1 = TextNode(parts[0], node.text_type)
                new_node2 = TextNode(parts[1], text_type)
                new_node3 = TextNode(parts[2], node.text_type)
                new_nodes.extend([new_node1, new_node2, new_node3])
    return new_nodes
