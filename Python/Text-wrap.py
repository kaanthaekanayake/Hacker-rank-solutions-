import textwrap
"""
Twxt wrap module used to wrap the input string into lines of specified width.
It provides a convenient way to format text for display or printing.
it break the long string into a shorter lines with the given width.
and it not break lines in the middle of a word.
it checks the max width and breaks the line at the last space before reaching the max width.
syntax: textwrap.fill(text, width=70)
"""

def wrap(string, max_width):
    wraped_text = textwrap.fill(string, max_width)
    return wraped_text
# textwrap.fill breaks the input string into lines of specified width with a new line character.after every line.
# there are some textwrap methods and all those are used  to format the text in different ways.
# study them in the official documentation for more understanding.
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)