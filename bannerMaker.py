# Script by Brett Verney (@wifiwizardofoz)
# Version: v1.0 | 30-06-2023

import os
import sys
import parawrap

def main():

    # Character width of box (must be even integer)
    box_width = 76
    # Padding between text width and box (must be even integer)
    padding = 4
    # Banner heading text
    heading = 'WARNING'
 
    # Define error for argument parsing with example
    if len(sys.argv) != 2:
        print(f"\nError: Incorrect usage. Script must be executed using 'python {os.path.basename(__file__)} [input_file]'\n")
        print(f"Example: 'python {os.path.basename(__file__)} message.txt'\n")
        return

    text_width = box_width - padding
    heading = f" {heading} "

    infile = sys.argv[1]
    try:
        with open(infile, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"\nError: The file '{infile}' was not found in the current working directory.\n")
        return
    else:
        output_file = 'banner.txt'
        with open(output_file, 'wt') as outfile:
            outfile.write(f"{heading.center(box_width, '*')}\n")
            outfile.write(f"*{' ' * (box_width - 2)}*\n")
            for line in parawrap.wrap(contents, width=text_width):
                outfile.write(f"*{line.center(box_width - 2)}*\n")
            outfile.write(f"*{' ' * (box_width - 2)}*\n")
            outfile.write(f"{'*' * box_width}\n")
        print(f"\nSuccess! The banner has been written to {output_file}")

# Start Here
if __name__ == "__main__":
    main()