import unittest
from function_workspace import (
    split_nodes_delimiter,
    text_node_to_html_node,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_convert_textnode_htmlnode_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_convert_textnode_htmlnode_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_convert_textnode_htmlnode_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_convert_textnode_htmlnode_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_convert_textnode_htmlnode_url(self):
        node = TextNode("This is a url node", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})
    
    def test_convert_textnode_htmlnode_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.boot.dev/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {'alt': 'This is an image node', 'src': 'https://www.boot.dev/image.png'})

    def test_convert_textnode_htmlnode_unknown(self):
        node = TextNode("This is an unknown type node", "unknown_type")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

    def test_split_textnode_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type.value, "text")
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type.value, "code")
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type.value, "text")
    
    def test_split_textnode_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type.value, "text")
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type.value, "bold")
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type.value, "text")

    def test_split_textnode_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text, "This is text with an ")
        self.assertEqual(new_nodes[0].text_type.value, "text")
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[1].text_type.value, "italic")
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type.value, "text")

    def test_split_textnode_not_text(self):
        node = TextNode("_This is text that is all italic_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text, "_This is text that is all italic_")
        self.assertEqual(new_nodes[0].text_type.value, "italic")
    
    def test_split_nodes_image(self):
        node = TextNode(
    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes[0].text, "This is text with an ")
        self.assertEqual(new_nodes[0].text_type.value, "text")
        self.assertEqual(new_nodes[1].text, "image")
        self.assertEqual(new_nodes[1].text_type.value, "image")
        self.assertEqual(new_nodes[1].url, "https://i.imgur.com/zjjcJKZ.png")
        self.assertEqual(new_nodes[2].text, " and another ")
        self.assertEqual(new_nodes[2].text_type.value, "text")
        self.assertEqual(new_nodes[3].text, "second image")
        self.assertEqual(new_nodes[3].text_type.value, "image")
        self.assertEqual(new_nodes[3].url, "https://i.imgur.com/3elNhQu.png")

    def test_split_nodes_link(self):
        node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes[0].text, "This is text with a link ")
        self.assertEqual(new_nodes[0].text_type.value, "text")
        self.assertEqual(new_nodes[1].text, "to boot dev")
        self.assertEqual(new_nodes[1].text_type.value, "link")
        self.assertEqual(new_nodes[1].url, "https://www.boot.dev")
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[2].text_type.value, "text")
        self.assertEqual(new_nodes[3].text, "to youtube")
        self.assertEqual(new_nodes[3].text_type.value, "link")
        self.assertEqual(new_nodes[3].url, "https://www.youtube.com/@bootdotdev")
    
    def test_split_nodes_link_not_link(self):
        node = TextNode("_This is text that is all italic_", TextType.ITALIC)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes[0].text, "_This is text that is all italic_")
        self.assertEqual(new_nodes[0].text_type.value, "italic")

    def test_split_nodes_image_not_img(self):
        node = TextNode("_This is text that is all italic_", TextType.ITALIC)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes[0].text, "_This is text that is all italic_")
        self.assertEqual(new_nodes[0].text_type.value, "italic")

    def test_split_nodes_link_empty_string(self):
        node = TextNode(
    "Here are two links [to boot dev](https://www.boot.dev) [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes[0].text, "Here are two links ")
        self.assertEqual(new_nodes[0].text_type.value, "text")
        self.assertEqual(new_nodes[1].text, "to boot dev")
        self.assertEqual(new_nodes[1].text_type.value, "link")
        self.assertEqual(new_nodes[1].url, "https://www.boot.dev")
        self.assertEqual(new_nodes[2].text, "to youtube")
        self.assertEqual(new_nodes[2].text_type.value, "link")
        self.assertEqual(new_nodes[2].url, "https://www.youtube.com/@bootdotdev")

    def test_text_to_textnodes_all(self):
        new_nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(new_nodes,
                         [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]
                         )

    def test_text_to_textnodes_multi_link(self):
        new_nodes = text_to_textnodes("This is a text node with a [link](https://boot.dev) and **another** [link](https://google.com) and some text after")
        self.assertEqual(new_nodes,
                         [
    TextNode("This is a text node with a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
    TextNode(" and ", TextType.TEXT),
    TextNode("another", TextType.BOLD),
    TextNode("link", TextType.LINK, "https://google.com"),
    TextNode(" and some text after", TextType.TEXT),
]
                         )

    def test_text_to_textnodes_multi_wrong_format(self):
        new_nodes = text_to_textnodes("This is a text node with a link(https://boot.dev) and some text after")
        self.assertEqual(new_nodes,
                         [
    TextNode("This is a text node with a link(https://boot.dev) and some text after", TextType.TEXT),]
    )


if __name__ == "__main__":
    unittest.main()
