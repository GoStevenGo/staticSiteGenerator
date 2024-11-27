from textnode import *

def main():
    test = TextNode("This is a text node", TextType.BOLD, "http://www.boot.dev")
    print(repr(test))

main()