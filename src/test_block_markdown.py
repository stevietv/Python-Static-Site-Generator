import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestBlockMarkdown(unittest.TestCase):

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
    
    def test_markdown_to_blocks_removes_blank_blocks(self):
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

    def test_markdown_to_blocks_trims_white_space(self):
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
            

    def test_block_type_heading1(self):
        md = "# This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_block_type_heading2(self):
        md = "## This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_block_type_heading3(self):
        md = "### This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_block_type_heading4(self):
        md = "#### This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_block_type_heading5(self):
        md = "##### This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_block_type_heading6(self):
        md = "###### This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)
    
    def test_block_type_heading7_invalid(self):
        md = "####### This is not a heading"
        self.assertNotEqual(block_to_block_type(md), BlockType.HEADING)

    
    def test_block_type_heading_space_required(self):
        md = "#This is not a heading"
        self.assertNotEqual(block_to_block_type(md), BlockType.HEADING)

    def test_block_type_code(self):
        md = """```
this is some code
in a code block```"""
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_block_type_code_one_line(self):
        md = """```
this is some code
```"""
        self.assertEqual(block_to_block_type(md), BlockType.CODE)
    
    def test_block_type_single_quote(self):
        md = "> This is a quote"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_block_type_multi_quote(self):
        md = """> This is a quote
> over multiple
> lines"""
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)
    
    def test_block_type_single_quote_no_space(self):
        md = ">This is a quote"
        self.assertNotEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_block_type_multi_quote_no_space(self):
        md = """> This is a quote
>over multiple
> lines"""
        self.assertNotEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_block_type_unordered_list(self):
        md = """- item 1
- item 2
- item 3"""
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    def test_block_type_unordered_list_with_error(self):
        md = """- item 1
- item 2
item 3"""
        self.assertNotEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    def test_block_type_ordered_list(self):
        md = """1. item 1
2. item 2
3. item 3"""
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)

    def test_block_type_ordered_list_with_error(self):
        md = """1. item 1
2. item 2
2. item 3"""
        self.assertNotEqual(block_to_block_type(md), BlockType.ORDERED_LIST)
        

        



if __name__ == "__main__":
    unittest.main()