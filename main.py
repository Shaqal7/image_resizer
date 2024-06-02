import sys
import os
from imgProcessor import imgProcessor

def main():
    directory_from = sys.argv[1] if len(sys.argv) > 1 else 'Photos/'
    directory_to = sys.argv[2] if len(sys.argv) > 2 else 'Converted/'

    if not os.path.exists(directory_to):
        try:
            os.mkdir(directory_to)
            print(f"Successfully created the directory {directory_to}")
        except OSError as e:
            print(f"Creation of the directory {directory_to} failed. Error: {e}")
            return  # Exit the script if directory creation fails

    for filename in os.listdir(directory_from):
        full_file_name = os.path.join(directory_from, filename)
        if os.path.isfile(full_file_name):
            try:
                imgProcessor(directory_from, directory_to, filename)
            except Exception as e:
                print(f"Processing file {filename} failed. Error: {e}")

if __name__ == "__main__":
    main()