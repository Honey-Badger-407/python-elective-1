input_file = input("Enter the name of the file to read from: ")
output_file = input("Enter the name of the file to write to: ")
try:
    with open(input_file, 'r') as file_in:
        content = file_in.read()
    with open(output_file, 'w') as file_out:
        file_out.write(content)
    print(f"Contents of '{input_file}' have been successfully copied to '{output_file}'.")
except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")