import subprocess

# Set the number of iterations to run
iterations = 10

# Set the base command
command = ["g++", "main.cpp", "subclass.cpp", "-o", "main"]

# Iterate over the number of iterations
for i in range(iterations):
    # Build the input file name
    input_file = f"input{i+1:02d}.txt"

    # Run the command with the input file
    subprocess.run(command + [f"&&", "./main", f"<", input_file])