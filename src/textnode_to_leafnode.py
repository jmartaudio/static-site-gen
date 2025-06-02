from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        html_node = LeafNode(None, text_node.value)
        return html_node



