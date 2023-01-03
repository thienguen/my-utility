import os

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

		# Print the file name
		print(file)

		# Build the full path to the file
		file_path = os.path.join(root, file)

		# Read the file contents
		with open(file_path, "r") as f:
			contents = f.read()

		# Replace CRLF end-of-line sequences with LF
		contents = contents.replace("\r\n", "\n")

		# Convert indentation to 2 spaces
		indentation = 0
		new_contents = []
		for line in contents.split("\n"):
			# Calculate the number of leading spaces
			leading_spaces = 0
			for char in line:
				if char == " ":
					leading_spaces += 1
				else:
					break

			# Calculate the number of indentation levels
			indentation_change = leading_spaces // 2 - indentation
			indentation += indentation_change

			# Strip leading and trailing spaces
			line = line.strip()

			# Add the modified line to the new contents
			new_contents.append("  " * indentation + line)

		# Join the modified lines into a single string
		contents = "\n".join(new_contents)

		# Write the modified contents back to the file
		with open(file_path, "w") as f:
			f.write(contents)