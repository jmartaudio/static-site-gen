from blocktype import block_to_block_type, markdown_to_blocks
from htmlnode import ParentNode
from textnode import TextNode
from function_workspace import text_to_textnodes, text_node_to_html_node

def markdown_to_html_node(markdown):
    split_md = markdown_to_blocks(markdown)
    block_obj_list = []
    final_html_nodes = []
    for block in split_md:
        block_obj_list.append(TextNode(block, block_to_block_type(block)))
    for obj in block_obj_list:
        children = text_to_textnodes(obj.text)
        html_children = []
        for node in children:
            html_children.append(text_node_to_html_node(node))
        final_html_nodes.append(ParentNode(None, [html_children], None))
    print(final_html_nodes)
