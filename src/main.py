import os
from textnode import TextNode, TextType
from os_interact import delete_public, copy_source

def main():
    src = './static'
    dest = 'public'

    if not os.path.exists(dest):
        os.makedirs(dest)

    delete_public(dest)
    copy_source(src, dest)


    node = TextNode("Hello! are you working?", TextType.BOLD)
    print(node)

main()
