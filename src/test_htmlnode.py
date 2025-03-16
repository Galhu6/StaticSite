import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_single_attribute(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_attributes(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_no_attributes(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")



class TestLeafNode(unittest.TestCase):

    def test_leafnode_basic_html(self):
        """Test that LeafNode renders simple HTML correctly."""
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leafnode_with_props(self):
        """Test that LeafNode renders with attributes correctly."""
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leafnode_without_tag(self):
        """Test that LeafNode renders raw text if no tag is provided."""
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leafnode_raises_error_without_value(self):
        """Test that LeafNode raises an error when value is None."""
        with self.assertRaises(ValueError):
            LeafNode("p", None)

if __name__ == "__main__":
    unittest.main()
