# file_processor.py (branch-two)
import os

def read_file(file_path):
    """ Reads content from a file and logs the file size """
    if not os.path.exists(file_path):
        return "File not found!"
    
    file_size = os.path.getsize(file_path)  # New feature
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"File size: {file_size} bytes")  # New feature
        return content
#
def process_text(text):
    """ Enhanced text processing with unique word count """
    words = set(text.lower().strip().split())
    print(f"Unique Words: {len(words)}")  # New feature
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
