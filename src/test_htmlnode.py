import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "a",
            "Give me your Data",
            None,
            {"class": "Data!!!", "href": "https://google.com"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="Data!!!" href="https://google.com"',

        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "Typing is hard",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "Typing is hard",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
    )


if __name__ == "__main__":
    unittest.main()

