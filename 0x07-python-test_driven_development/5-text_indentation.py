#!/usr/bin/python3
"""
This module prints a text with 2 new lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Process text
    new_text = ""
    add_newline = False     # Flag to indicate when to add two newlines

    for char in text:
        new_text += char

        if char in ['.', '?', ':']:
            new_text += '\n\n'
            add_newline = True
        elif add_newline and char == ' ':
            add_newline = False

    # Split the modified text into lines
    lines = new_text.split('\n')
    formatted_text = '\n'.join(line.strip() for line in lines if line.strip())
    print(formatted_text)
