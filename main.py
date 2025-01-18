def modify_content(content):
    """
    This function modifies the content of the file.
    For demonstration, we'll convert the text to uppercase.
    """
    return content.upper()

def read_and_write_file():
    # Prompt the user for the input filename
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Try to open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("File read successfully.")
            
            # Modify the content
            modified_content = modify_content(content)
            
            # Define the output filename
            output_filename = "modified_" + input_filename
            
            # Write the modified content to a new file
            with open(output_filename, 'w') as outfile:
                outfile.write(modified_content)
            print(f"Modified content written to {output_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()
