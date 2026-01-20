import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_nultiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
    
    def test_to_html_with_children_parent_has_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"style": "text-align: center"})
        self.assertEqual(parent_node.to_html(), '<div style="text-align: center"><span>child</span></div>')
    
    def test_to_html_with_children_child_has_props(self):
        child_node = LeafNode("span", "child", {"style": "text-align: center"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><span style="text-align: center">child</span></div>')


if __name__ == "__main__":
    unittest.main()