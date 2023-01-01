import os

def rename_files(directory):
    # Iterate over all the files in the directory
    # Construct the full file path
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # If the file is a JavaScript file
        # Check if the file is a regular file (not a directory)
        if filename.endswith(".js"):
            print("A File: " + filename)
            if os.path.isfile(file_path):
                os.rename(file_path, os.path.join(directory, "main.js"))

        # or a directory, recursively call this function on that directory
        elif os.path.isdir(file_path):
            print("A Directory: " + filename)
            rename_files(file_path)

# Call the rename_files function on the current working directory
rename_files(os.getcwd())