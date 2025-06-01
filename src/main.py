from textnode import TextNode, TextType

def main():
    node = TextNode("Hello! are you working?", TextType.BOLD_TEXT)

    print(node)

if __name__ == "__main__":
    main()
