import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_basic(self):
        node1 = HTMLNode("h1", "This is header text")
        node2 = HTMLNode("h1", "This is header text")
        self.assertEqual(node1, node2)

    def test_eq_advanced(self):
        link_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node1 = HTMLNode("a", "this is a link", props=link_props)
        node2 = HTMLNode("a", "this is a link", props=link_props)
        self.assertEqual(node1, node2)

    def test_not_eq_advanced(self):
        link_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        link_props_with_title = link_props.copy()
        link_props_with_title["title"] = "alt text"

        node1 = HTMLNode("a", "this is a link", props=link_props)
        node2 = HTMLNode("a", "this is a link", props=link_props_with_title)
        self.assertNotEqual(node1, node2)

    def test_props_to_html(self):
        link_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node1 = HTMLNode("a", "this is a link", props=link_props)
        props_to_html = node1.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(props_to_html, expected)


if __name__ == "__main__":
    unittest.main()