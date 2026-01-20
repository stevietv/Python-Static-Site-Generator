import unittest

from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
        
    def test_leaf_to_html_a(self):
        link_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        expected = '<a href="https://www.google.com" target="_blank">this is a link</a>'

        node1 = LeafNode("a", "this is a link", props=link_props)
        self.assertEqual(node1.to_html(), expected)
    
    def test_eq(self):
        link_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node1 = LeafNode("a", "this is a link", props=link_props)
        node2 = LeafNode("a", "this is a link", props=link_props)
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()