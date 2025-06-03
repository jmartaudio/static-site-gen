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



