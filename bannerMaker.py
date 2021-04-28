# Script by Brett Verney (@wifiwizardofoz)
# Version: v0.1 | 28-04-2021

import os
import sys
import parawrap

def main():

    # Character width of box (must be even integer)
    box_width = int(76)
    # Padding between text width and box (must be even integer)
    padding = int(4)
    # Banner heading text
    heading = ('WARNING')
 
    # Define error for arguement parsing with example
    if len(sys.argv) !=2:
        print('')
        print(f'Error: Incorrect usage. Script must be executed using \'python {os.path.basename(__file__)} [input_file]\'')
        print('')
        print(f'Example: \'python {os.path.basename(__file__)} message.txt\'')
        print('')
        sys.exit(2)

    text_width = int(box_width - padding)
    heading = (' ' + heading + ' ')
    try:
        infile = (sys.argv[1])
        with open(infile) as f:
            contents = f.read()
    except FileNotFoundError:
        print('')
        print(f'Error: \'{infile}\' was not found in the current working directory.')
        print('')
    else:
        sys.stdout = open('banner.txt','wt')
        print (heading.center(box_width,'*'))
        print('*' + (' ' * (box_width - 2)) + '*')
        for line in parawrap.wrap(contents, width=text_width):
            print('*' + line.center(box_width-2) + '*')
        print('*' + (' ' * (box_width - 2)) + '*')
        print('*' * (box_width))
        sys.exit(0)

# Start Here
if __name__ == "__main__":
    main()
