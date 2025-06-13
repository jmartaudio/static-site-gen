from textnode import TextNode, TextType
from htmlnode import LeafNode
import re



def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    image = split_nodes_image(code)
    final = split_nodes_link(image)
    return final


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


def split_nodes_image(old_nodes):
    new_nodes= []
    for old_node in old_nodes:
        if old_node.text_type.value != "text":
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        img_parts = extract_markdown_images(remaining_text)
        if len(img_parts) == 0:
            new_nodes.append(old_node)
            continue
        for img in img_parts:
            chunk = remaining_text.split(f"![{img[0]}]({img[1]})", 1)
            if len(chunk) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if chunk[0].strip() != "":
                new_nodes.append(TextNode(chunk[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    img[0],
                    TextType.IMAGE,
                    img[1],
                )
            )
            remaining_text = chunk[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes= []
    for old_node in old_nodes:
        if old_node.text_type.value != "text":
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        url_parts = extract_markdown_url(remaining_text)
        if len(url_parts) == 0:
            new_nodes.append(old_node)
            continue
        for url in url_parts:
            chunk = remaining_text.split(f"[{url[0]}]({url[1]})", 1)
            if len(chunk) != 2:
                raise ValueError("invalid markdown, url section not closed")
            if chunk[0].strip() != "":
                new_nodes.append(TextNode(chunk[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    url[0],
                    TextType.LINK,
                    url[1],
                )
            )
            remaining_text = chunk[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def extract_markdown_url(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
