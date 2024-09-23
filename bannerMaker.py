# Script by Brett Verney (@wifiwizardofoz)
# Version: v1.2 | 29-07-2024

import os
import sys
import parawrap

def print_error_and_exit(message, example_usage):
    """Prints an error message and exits the script."""
    print(f"\nError: {message}\n")
    print(f"Example: {example_usage}\n")
    sys.exit(1)

def read_file(file_path):
    """Reads the content of the file specified by file_path."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        # Handle file not found error
        print_error_and_exit(f"The file '{file_path}' was not found in the current working directory.",
                             "Please provide a valid file path.")

def create_banner_text(contents, box_width, padding, heading):
    """
    Creates the banner text from the given contents, box width, padding, and heading.

    Args:
        contents (str): The content to be wrapped inside the banner.
        box_width (int): The width of the banner box.
        padding (int): The padding between text and box borders.
        heading (str): The heading text for the banner.

    Returns:
        list: A list of strings representing the lines of the banner.
    """
    # Calculate the width for the text inside the box
    text_width = box_width - padding - 2  # -2 for the '|' on either side

    # Format heading with single space on either side
    heading = f" {heading} "
    total_dashes = box_width - len(heading) - 2  # -2 for the '+' characters
    heading_line = f"+{'-' * (total_dashes // 2)}{heading}{'-' * (total_dashes // 2 + total_dashes % 2)}+"

    # Initialize the list to hold each line of the banner
    banner_lines = [
        heading_line,  # Top border with heading
        f"|{' ' * (box_width - 2)}|"  # Empty line below heading
    ]

    # Wrap the contents to fit within the text width
    for line in parawrap.wrap(contents, width=text_width):
        if line.strip():  # Check if the line is not empty or just whitespace
            # Calculate the remaining space for padding
            remaining_space = box_width - 2 - len(line)
            padding_each_side = remaining_space // 2
            extra_space = remaining_space % 2

            # Create the padded line
            padded_line = f"{' ' * padding_each_side}{line}{' ' * (padding_each_side + extra_space)}"
        else:
            # For empty lines, fill with spaces to align vertical bars
            padded_line = ' ' * (box_width - 2)

        # Append the formatted line to the banner
        banner_lines.append(f"|{padded_line}|")

    # Add the empty line and bottom border
    banner_lines.append(f"|{' ' * (box_width - 2)}|")
    banner_lines.append(f"+{'-' * (box_width - 2)}+")

    return banner_lines

def write_banner(output_file, banner_lines):
    with open(output_file, 'w') as outfile:
        outfile.write("\n".join(banner_lines))
    print(f"\nSuccess! The banner has been written to {output_file}")

def main():
    """
    Main function to read input file, create banner, and write to output file.
    """
    # Character width of the box (must be even integer)
    box_width = 76
    # Padding between text width and box (must be even integer)
    padding = 4
    # Banner heading text
    heading = 'WARNING'

    # Validate argument count
    if len(sys.argv) != 2:
        print_error_and_exit("Incorrect usage. Script must be executed using 'python script.py [input_file]'",
                             f"python {os.path.basename(__file__)} message.txt")

    # Read the input file
    infile = sys.argv[1]
    contents = read_file(infile)

    # Create the banner text
    banner_lines = create_banner_text(contents, box_width, padding, heading)

    # Write the banner to the output file
    write_banner('banner.txt', banner_lines)

# Start the script execution
if __name__ == "__main__":
    main()
