# File Read & Write Challenge 🖋️

## Overview
This Python program reads a file specified by the user, modifies its content, and writes the modified content to a new file. It also includes error handling to manage cases where the file might not exist or cannot be read, ensuring the program runs smoothly without crashing.

## Features
- **File Reading**: Reads the content of a user-specified file.
- **Content Modification**: Modifies the content of the file (e.g., converts text to uppercase).
- **File Writing**: Writes the modified content to a new file.
- **Error Handling**: Gracefully handles file-related errors such as missing files or read errors.

## How It Works
1. The program prompts the user to enter the name of a file to read.
2. It attempts to open and read the file.
3. If the file is read successfully, the content is modified and written to a new file prefixed with "modified_".
4. The program handles errors such as file not found or read errors, providing informative messages to the user.

## Usage
1. Run the script in a Python environment.
2. When prompted, enter the filename of the file you want to read.
3. If the file exists and can be read, the program will create a new file with the modified content.
4. Check the console for messages about the success or any errors encountered.

### Example
```plaintext
Enter the name of the file to read: example.txt
File read successfully.
Modified content written to modified_example.txt.
