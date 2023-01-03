import os

def rename_files(directory):
    # Iterate over all the files in the directory
    # Construct the full file path
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # If the file is a JavaScript file, rename it to main.js
        if filename.endswith(".js"):
            print("A JavaScript file: " + filename)
            if os.path.isfile(file_path):
                os.rename(file_path, os.path.join(directory, "main.js"))

        # If the file is an HTML file, rename it to index.html
        elif filename.endswith(".html"):
            print("An HTML file: " + filename)
            if os.path.isfile(file_path):
                os.rename(file_path, os.path.join(directory, "index.html"))

        # If the file is a CSS file, rename it to style.css
        elif filename.endswith(".css"):
            print("A CSS file: " + filename)
            if os.path.isfile(file_path):
                os.rename(file_path, os.path.join(directory, "style.css"))

        # If the file is a directory, recursively call this function on that directory
        elif os.path.isdir(file_path):
            print("A directory: " + filename)
            rename_files(file_path)

# Call the rename_files function on the current working directory
rename_files(os.getcwd())