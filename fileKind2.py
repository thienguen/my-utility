import os
import re

# Set the target directory
directory = os.getcwd()

# Set the file types to modify
file_types = [".html", ".css", ".js", ".jsx", ".ts", ".tsx"]

# Iterate over all files in the directory
for root, _, files in os.walk(directory):
	for file in files:
		# Check the file extension
		_, file_extension = os.path.splitext(file)
		if file_extension not in file_types:
			continue

		# print file name
		print(file)

		# Build the full path to the file
		file_path = os.path.join(root, file)

		# Read the file contents
		with open(file_path, "r") as f:
			contents = f.read()

		# Replace CRLF end-of-line sequences with LF
		contents = contents.replace("\r\n", "\n")

		# Convert indentation to spaces of size 2
		contents = re.sub(r" {2}", "  ", contents)

		# Remove all trailing spaces from each line
		contents = [line.rstrip() for line in contents.split("\n")]
		contents = "\n".join(contents)

		# Write the modified contents back to the file
		with open(file_path, "w") as f:
			f.write(contents)