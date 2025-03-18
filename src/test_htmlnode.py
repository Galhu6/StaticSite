import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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


class TestParentNode(unittest.TestCase):

    def test_to_html_single_child(self):
        # """Test a ParentNode with a single LeafNode child."""
        child = LeafNode("p", "Hello world")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><p>Hello world</p></div>")

    def test_to_html_multiple_children(self):
        # """Test a ParentNode with multiple LeafNode children."""
        child1 = LeafNode("p", "First paragraph")
        child2 = LeafNode("p", "Second paragraph")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(parent.to_html(), "<div><p>First paragraph</p><p>Second paragraph</p></div>")

    def test_to_html_with_attributes(self):
        # """Test a ParentNode with attributes (props)."""
        child = LeafNode("p", "Text with class")
        parent = ParentNode("div", [child], props={"class": "container"})
        self.assertEqual(parent.to_html(), '<div class="container"><p>Text with class</p></div>')

    def test_to_html_nested_structure(self):
        # """Test deeply nested ParentNodes."""
        grandchild = LeafNode("i", "italic text")
        child = ParentNode("p", [grandchild])
        parent = ParentNode("section", [child])
        self.assertEqual(parent.to_html(), "<section><p><i>italic text</i></p></section>")

    def test_to_html_mixed_content(self):
        # """Test ParentNode with both LeafNode and ParentNode children."""
        grandchild = LeafNode("strong", "bold text")
        child = ParentNode("span", [grandchild])
        sibling = LeafNode("p", "A separate paragraph")
        parent = ParentNode("div", [child, sibling])
        self.assertEqual(parent.to_html(), "<div><span><strong>bold text</strong></span><p>A separate paragraph</p></div>")

    def test_to_html_parent_with_text_and_children(self):
        # """Ensure ParentNode does not allow a value (should only have children)."""
        with self.assertRaises(TypeError):
            ParentNode("div", [], value="Invalid")

    def test_to_html_empty_children(self):
        # """Ensure ParentNode raises ValueError when initialized without children."""
        with self.assertRaises(ValueError):
            ParentNode("ul", [])

    def test_to_html_with_multiple_attributes(self):
        # """Test ParentNode with multiple attributes."""
        child = LeafNode("p", "Paragraph with styles")
        parent = ParentNode("div", [child], props={"class": "content", "id": "main"})
        self.assertEqual(parent.to_html(), '<div class="content" id="main"><p>Paragraph with styles</p></div>')

    # def test_to_html_parent_with_only_text(self):
    #     # """Ensure ParentNode with text but no children is not allowed."""
    #     with self.assertRaises(TypeError):
    #         ParentNode("span", "Just text")

    def test_to_html_list_structure(self):
        # """Test ParentNode for an unordered list structure."""
        li1 = LeafNode("li", "Item 1")
        li2 = LeafNode("li", "Item 2")
        ul = ParentNode("ul", [li1, li2])
        self.assertEqual(ul.to_html(), "<ul><li>Item 1</li><li>Item 2</li></ul>")


if __name__ == "__main__":
    unittest.main()

