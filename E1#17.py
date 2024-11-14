file_name = input("Enter the name of the text file: ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
        words = content.split()
        cleaned_words = [word.strip('.,!?;:"()[]{}').lower() for word in words]
        unique_words = set(cleaned_words)
        # Convert the set to a sorted list
        sorted_unique_words = sorted(unique_words)
        # Print the sorted unique words
        print("Unique words in alphabetical order:")
        for word in sorted_unique_words:
            print(word)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")