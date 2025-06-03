import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("boot.dev url", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("google url", TextType.LINK, "https://www.google.com")
        self.assertNotEqual(node, node2)
        self.assertEqual(node.text_type, node2.text_type)

    def test_different(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("boot.dev url", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual (node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is some other text", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
                "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
