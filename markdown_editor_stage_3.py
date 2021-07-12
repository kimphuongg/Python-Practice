# Project: Markdown Editor
# Stage: 3/5
'''
Objectives
Implement a separate function for each of the formatters. It will keep your code structured. With functions, you also will be able to find and fix a bug with ease if something is wrong.
The program should work in the following way:
Ask a user to input a formatter.
If the formatter doesn't exist, print the following error message: Unknown formatting type or command
Ask a user to input a text that will be applied to the formatter: Text: <user's input>.
Save the text with the chosen formatter applied to it and print the markdown. Each time you should print out the whole text in markdown accumulated so far.
Different formatters may require different inputs.
The new-line formatter does not require text input.
Plain, bold, italic, and inline-code formatters require only text input, and should not add an extra space or line break at the end:
Text: > Some text
Headers require a level and text. A level is a number from 1 to 6. Don't forget to check it too: if it is out of bounds, print the corresponding error: The level should be within the range of 1 to 6. Also, remember that a heading automatically adds a new line in the end.
Level: > 4
Text: > Hello World!
Link requires a label and a URL:
Label: > Tutorial
URL: > https://www.markdownguide.org/basic-syntax/
'''


def formatter_plain():
    text = input('Text: ')
    return text


def formatter_bold():
    text = input('Text: ')
    return '**' + text + '**'


def formatter_italic():
    text = input('Text: ')
    return '*' + text + '*'


def formatter_inline_code():
    text = input('Text: ')
    return '`' + text + '`'


def formatter_newline():
    return '\n'


def formatter_header():
    level = int(input('Level: '))
    while level not in range(1, 7):
        print('The level should be within the range of 1 to 6')
        level = int(input('Level: '))
    text = input('Text: ')
    return level * '#' + ' ' + text + '\n'


def formatter_link():
    label = input('Label: ')
    url = input('URL: ')
    return '[' + label + '](' + url + ')'


def input_process():
    markdown_str = ''
    while True:
        input_cmd = input('Choose a formatter: ')
        if input_cmd == 'plain':
            markdown_str += formatter_plain()
            print(markdown_str)
        elif input_cmd == 'bold':
            markdown_str += formatter_bold()
            print(markdown_str)
        elif input_cmd == 'italic':
            markdown_str += formatter_italic()
            print(markdown_str)
        elif input_cmd == 'inline-code':
            markdown_str += formatter_inline_code()
            print(markdown_str)
        elif input_cmd == 'new-line':
            markdown_str += formatter_newline()
            print(markdown_str)
        elif input_cmd == 'header':
            markdown_str += formatter_header()
            print(markdown_str)
        elif input_cmd == 'link':
            markdown_str += formatter_link()
            print(markdown_str)
        elif input_cmd == '!done':
            break
        else:
            print('Unknown formatting type or command')

# formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line']


input_process()
