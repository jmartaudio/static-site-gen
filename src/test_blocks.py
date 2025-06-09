import unittest

from blocktype import BlockType, block_to_block_type, markdown_to_blocks
from markdown_to_htmlnode import markdown_to_html_node

class Blocks(unittest.TestCase):
    def test_blocks_to_blocktype_header(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
    def test_blocks_to_blocktype_quote(self):
        block = "> This is a quote block"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
    def test_blocks_to_blocktype_code(self):
        block = "```This is a code block```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
    def test_blocks_to_blocktype_ulist(self):
        block = "- list item\n- more list\n- one more list"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ULIST)
    def test_blocks_to_blocktype_olist(self):
        block = "1. item one\n2. item two\n3. item three"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.OLIST)
    def test_blocks_to_blocktype_paragraph(self):
        block = "this is a paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    def test_blocks_to_blocktype_paragraph2(self):
        block = '"this is a paragraph"'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_types_from_boot_dev(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_extra_newlines(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_header(self):
        md = """
# This is a heading

## This is a subheading.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
        blocks,
        [
            "# This is a heading",
            "## This is a subheading.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        ],
    )

    def test_markdown_to_html_node_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        self.assertEqual(node, "something")
        


"""
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

"""

if __name__ == "__main__":
    unittest.main()
