import unittest

from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a url node", TextType.LINK, "https://google.com")
        node2 = TextNode("This is a url node", TextType.LINK, "https://google.com")
        self.assertEqual(node, node2)

    def test_eq_with_url_none(self):
        node = TextNode("This is a url node", TextType.LINK, None)
        node2 = TextNode("This is a url node", TextType.LINK, None)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()