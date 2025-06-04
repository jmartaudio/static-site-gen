import unittest
from function_workspace import *

class TestFunctions(unittest.TestCase):
    def test_extract_img(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_url(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_url(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_extract_url_more(self):
        text = "This is text with a link [to boot dev](boot.dev) and [to youtube](youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_url(text), [("to boot dev", "boot.dev"), ("to youtube", "youtube.com/@bootdotdev")])
    
    def test_extract_url_no_brackets(self):
        text = "This is text with a link to boot dev(https://www.boot.dev) and to youtube(https://www.youtube.com/@bootdotdev)"
        with self.assertRaises(Exception):
            extract_markdown_url(text)
     
    def test_extract_url_no_parentheses(self):
        text = "This is text with a link to [boot dev]https://www.boot.dev and [to youtube]https://www.youtube.com/@bootdotdev"
        with self.assertRaises(Exception):
            extract_markdown_url(text)
     
    def test_extract_img_no_exclamation(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        with self.assertRaises(Exception):
            extract_markdown_images(text)
