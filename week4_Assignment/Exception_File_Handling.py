# File Read & Write Challenge
def read_and_write_file():
    # Ask the user for the filename to read
    filename = input("Enter the filename to read: ")
    
    try:
        # Open the file for reading
        with open(filename, "r") as file:
            content = file.read()
            print("File content read successfully.")
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
            print(f"Modified content written to {new_filename}.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read/write the file '{filename}'.")

# Run the program
read_and_write_file()
