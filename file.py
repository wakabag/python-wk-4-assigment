def main():
    # Ask the user for the input filename
    input_filename = input("Enter the filename to read: ")

    # Initialize variable to store file content
    content = ""

    # Try to open and read the file, handle possible errors
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print(f"Successfully read from {input_filename}")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
        return
    except IOError:
        print(f"Error: Cannot read the file '{input_filename}'.")
        return

    # Modify the content, e.g., convert to uppercase
    modified_content = content.upper()

    # Ask the user for the output filename
    output_filename = input("Enter the filename to write the modified content: ")

    # Write the modified content to the new file
    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"Modified content has been written to {output_filename}")
    except IOError:
        print(f"Error: Cannot write to the file '{output_filename}'.")

if __name__ == "__main__":
    main()