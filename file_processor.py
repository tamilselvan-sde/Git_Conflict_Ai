# file_processor.py (branch-one)
import os

def read_file(file_path):
    """ Reads content from a file and counts lines """
    if not os.path.exists(file_path):
        return "File not found!"
    
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Lines in file: {len(content.splitlines())}")  # New feature
        return content

def process_text(text):
    """ Improved text processing with word count """
    words = text.lower().strip().split()
    print(f"Word Count: {len(words)}")  # New feature
    return " ".join(words)

def write_file(file_path, content):
    """ Writes content to a file """
    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    input_file = "sample.txt"
    content = read_file(input_file)
    processed_content = process_text(content)
    write_file("output.txt", processed_content)
    print("Processing complete!")
