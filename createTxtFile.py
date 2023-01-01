import os

def createTxt(directory):
	with open(os.path.join(directory, "in.txt"), "w") as f:
		pass

""" 
    directory: The path to the current location
    foreach: The next possible path for a file or directory
"""
def createTxtFiles(directory):
    # Iterate over all files and directory in the cwd
    for foreach in os.listdir(directory):
        # Construct the fuil file path
        curr_path = os.path.join(directory, foreach)
        
        # We need to create a txt file for each [directory]
        if os.path.isdir(curr_path):
            createTxt(curr_path)
            createTxtFiles(curr_path)

if __name__ == "__main__":
    # Create the txt files
    createTxtFiles(os.getcwd())