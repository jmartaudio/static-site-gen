from blocktype import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import ParentNode, LeafNode
from function_workspace import text_to_textnodes, text_node_to_html_node
import re

def markdown_to_html_node(markdown):
    split_md = markdown_to_blocks(markdown)
    block_dict = {}
    final_html_nodes = []
    for block in split_md:
        block_dict[block] = block_to_block_type(block)
    for key, value in block_dict.items():
        tag = blocktype_to_tag(key, value)
        if value == BlockType.ULIST:
            split_items = key.split('\n')
            children_html_nodes = []
            for item in split_items:
                grand_children_html_nodes = []
                text_nodes = text_to_textnodes(item[1:])
                for node in text_nodes:
                    grand_children_html_nodes.append(text_node_to_html_node(node))
                children_html_nodes.append(ParentNode("li", grand_children_html_nodes))
            final_html_nodes.append(ParentNode(tag, children_html_nodes))
        elif value == BlockType.OLIST:
            split_items = key.split('\n')
            children_html_nodes = []
            for item in split_items:
                grand_children_html_nodes = []
                text_nodes = text_to_textnodes(item)
                for node in text_nodes:
                    grand_children_html_nodes.append(text_node_to_html_node(node))
                children_html_nodes.append(ParentNode("li", grand_children_html_nodes))
            final_html_nodes.append(ParentNode(tag, children_html_nodes))
        elif value == BlockType.CODE:
            final_html_nodes.append(ParentNode('pre', [LeafNode(tag, key[4:-3])]))
        else:
            text_nodes = text_to_textnodes(key)
            html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
            final_html_nodes.append(ParentNode(tag, html_nodes))
    
    result =  ParentNode("div", final_html_nodes)
    return result
    

def blocktype_to_tag(key, value):
    if value == BlockType.HEADING:
        match = re.match(r"#{0,6}", key)
        if match:
            level = match.group(0).count("#")
            return f"h{level}"
    if value == BlockType.QUOTE:
        return "quoteblock"
    if value == BlockType.ULIST:
        return "ul"
    if value == BlockType.OLIST:
        return "ol"
    if value == BlockType.CODE:
        return "code"
    else:
        return "p"

