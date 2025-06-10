from blocktype import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import ParentNode, LeafNode
from textnode import TextNode
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
        if value == BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(key)
            html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
            final_html_nodes.append(ParentNode(tag, html_nodes))
        else:
            final_html_nodes.append(LeafNode(tag, key))
    
    result =  ParentNode("div", final_html_nodes)
    print(result.to_html())
    return result
    

def blocktype_to_tag(block, BlockType):
    if BlockType == BlockType.HEADING:
        match = re.match(r"#{0,6}", block)
        if match:
            level = match.group(0).count("#")
            return f"h{level}"
    if BlockType == BlockType.QUOTE:
        return "quoteblock"
    if BlockType == BlockType.ULIST:
        return "ul"
    if BlockType == BlockType.OLIST:
        return "ol"
    if BlockType == BlockType.CODE:
        return "pre><code"
    else:
        return "p"