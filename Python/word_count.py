def word_count_from_file(input_file, output_file):
    try:
        # Open the input.txt file for reading
        with open(input_file, 'r', encoding='utf-8') as file:
            # Read the entire content of the file
            text = file.read()

            # Split the text into words
            words = text.split()

            # Initialize an empty dictionary to store word counts
            word_count_dict = {}

            # Iterate through each word in the list of words
            for word in words:
                # Remove any trailing punctuation (like . or ,)
                word = word.strip('.,!?\'"')
                # Convert the word to lowercase to ignore case sensitivity
                word = word.lower()
                # Update the word count in the dictionary
                if word:
                    if word in word_count_dict:
                        word_count_dict[word] += 1
                    else:
                        word_count_dict[word] = 1

        # Open the output file for writing
        with open(output_file, 'w', encoding='utf-8') as file:
            # Write the word counts to the output file
            for word, count in word_count_dict.items():
                file.write(f"{word}: {count}\n")

        print(f"Word counts saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")


# Example usage:
input_file = 'input.txt'  # Replace with your input.txt file name
output_file = 'output.txt'  # Replace with your output file name

word_count_from_file(input_file, output_file)
