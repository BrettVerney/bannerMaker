# Script by Brett Verney (@wifiwizardofoz)
# Version: v1.1 | 18-09-2023

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

    text_width = box_width - padding - 2  # -2 for the '|' on either side
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
            outfile.write(f"+{'-' * (box_width - 2)}+\n")  # Top border
            outfile.write(f"|{heading.center(box_width - 2)}|\n")  # Heading
            outfile.write(f"|{' ' * (box_width - 2)}|\n")  # Empty line below heading

            for line in parawrap.wrap(contents, width=text_width):
                if line.strip():  # Check if line is not empty or just whitespace
                    actual_line_length = len(line)
                    remaining_space = box_width - 2 - actual_line_length  # -2 for the '|' on either side
                    padding_each_side = remaining_space // 2
                    extra_space = remaining_space % 2  # If remaining space is odd, add 1 space at the end

                    padded_line = ' ' * padding_each_side + line + ' ' * padding_each_side + ' ' * extra_space
                else:
                    padded_line = ' ' * (box_width - 2)  # For empty lines, fill with spaces to align vertical bars

                outfile.write(f"|{padded_line}|\n")

            outfile.write(f"|{' ' * (box_width - 2)}|\n")  # Empty line below text
            outfile.write(f"+{'-' * (box_width - 2)}+\n")  # Bottom border

        print(f"\nSuccess! The banner has been written to {output_file}")

# Start Here
if __name__ == "__main__":
    main()