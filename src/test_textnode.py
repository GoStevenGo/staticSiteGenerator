import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test2_eq(self):
        node = TextNode("Trying different urls", TextType.BOLD, "https://URL.com")
        node2 = TextNode("Trying different urls", TextType.BOLD, "https://differentURL.com")
        self.assertNotEqual(node, node2)

    def test3_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://URL.com")
        node2 = TextNode("Let's try different text", TextType.ITALIC, "https://URL.com")
        self.assertNotEqual(node, node2)

    def test4_eq(self):
        node = TextNode("What if the TextType is different", TextType.BOLD)
        node2 = TextNode("What if the TextType is different", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test5_eq(self):
        node = TextNode("What if the TextType is different with url", TextType.BOLD, "https://URL.com")
        node2 = TextNode("What if the TextType is different with url", TextType.LINK, "https://URL.com")
        self.assertNotEqual(node, node2)

    def test6_eq(self):
        node = TextNode("correct with url", TextType.IMAGE, "https://URL.com")
        node2 = TextNode("correct with url", TextType.IMAGE, "https://URL.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()