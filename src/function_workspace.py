from textnode import TextNode, TextType
from htmlnode import LeafNode
import re

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url},)
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text},)
    else:
        raise Exception("Unknown text type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type.value != "text":
            new_nodes.append(old_node)
            continue
        split_nodes = []
        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception("invalid md syntax")
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(parts[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_url(text):
    extracted_url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    if not extracted_url:
        raise Exception("no valid url found")
    else:
        return extracted_url

def extract_markdown_images(text):
    extracted_img = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    if not extracted_img:
        raise Exception("no valid image found")
    else:
        return extracted_img

