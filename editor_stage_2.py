# Project: Markdown Editor
# Stage: 2/5
'''
Implement the help function that will print available syntax commands, which we have indicated above, as well as the special commands. When called, it should print the following:
Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done
Implement the exit function that exits the editor without saving.
Ask a user for input:
Choose a formatter:
!help prints the help page, !done exits the editor.
If the input contains one of the correct formatters (plain, bold, italic, etc.), ask for the input once again.
If the input contains no formatters or unknown command is sent, print the following message and ask for input again: Unknown formatting type or command
'''

formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
while True:
    input_cmd = input('Choose a formatter: ')
    if input_cmd == '!help':
        print('Available formatters: ', end='')
        for formatter in formatters:
            print(formatter + ' ', end='')
        print('\nSpecial commands: !help !done')
    elif input_cmd == '!done':
        break
    elif input_cmd in formatters:
        continue
    else:
        print('Unknown formatting type or command')
