import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_equal_text(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_text_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_equal_url(self):
        node1 = TextNode("This is a link", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://another.com")
        self.assertNotEqual(node1, node2)

    def test_default_url_none(self):
        node = TextNode("This is normal text", TextType.NORMAL)
        self.assertIsNone(node.url)

    def test_repr(self):
        node = TextNode("Test", TextType.CODE, None)
        expected_repr = 'TextNode("Test", code, "None")'
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
