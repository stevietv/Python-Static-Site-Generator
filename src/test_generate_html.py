import unittest
from generate_html import markdown_to_html_node

class TestGenerateHTML(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_ordered_list(self):
        md = """
1. Item 1
2. **Item** 2
3. Item 3
4. Item 4"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li><b>Item</b> 2</li><li>Item 3</li><li>Item 4</li></ol></div>"
        )

    def test_unordered_list(self):
        md = """
- Item 1
- **Item** 2
- Item 3
- Item 4"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li><b>Item</b> 2</li><li>Item 3</li><li>Item 4</li></ul></div>"
        )
    
    def test_heading(self):
        md = "### This is an **Important** heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is an <b>Important</b> heading</h3></div>"
        )
    
    def test_heading_paragraph_image(self):
        md = """
### This is an **Important** heading

This paragraph describes the image underneath

![Image text](https://www.imgur.com/1.png)

Click [here](https://www.google.com) for more information
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h3>This is an <b>Important</b> heading</h3><p>This paragraph describes the image underneath</p><p><img src="https://www.imgur.com/1.png" alt="Image text"></img></p><p>Click <a href="https://www.google.com">here</a> for more information</p></div>'
        )

if __name__ == "__main__":
    unittest.main()