# Writing to files
with open("example.txt", "w") as file:
    file.write("Hello World!\nWelcome to Python file handling.\n")

# Move pointer back to start & Check file pointer using seek(0) and tell()
with open("example.txt", "r") as file:
    print("Pointer before seek:", file.tell())
    file.seek(0)
    print("Pointer after seek:", file.tell())

# readlines()
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Closing files manually
file = open("example.txt", "r")
print(file.read())
file.close()

# With statement
with open("example.txt", "r") as file:
    print(file.read())

#  Binary mode ("rb", "wb")
with open("binary_file.bin", "wb") as file:
    file.write(b"This is binary data.")

with open("binary_file.bin", "rb") as file:
    content = file.read()
    print("Binary content:", content)

# Create a file and write to it
with open("new_file.txt", "w") as file:
    file.write("This is a new file.\nPython is awesome.")

# Read the file and print its content
with open("new_file.txt", "r") as file:
    content = file.read()
    print(content)

# Read the file line by line
with open("new_file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read a single line
with open("new_file.txt", "r") as file:
    print(file.readline())

# Read all lines into a list
with open("new_file.txt", "r") as file:
    lines = file.readlines()
    print(lines)

#  Append to the file
with open("new_file.txt", "a") as file:
    file.write("\nAppended line here.")

# Reading with seek() and tell()
with open("new_file.txt", "r") as file:
    print("Initial position:", file.tell())
    file.seek(5)
    print("After seek(5):", file.tell())
    print("Content from position 5:", file.read())

# Demonstrating 'x' mode 
try:
    with open("exclusive.txt", "x") as file:
        file.write("This file is created using 'x' mode.")
except FileExistsError:
    print("File already exists!")

# Copy file example
with open("new_file.txt", "r") as source, open("copy_of_file.txt", "w") as target:
    for line in source:
        target.write(line)

print("File copied successfully.")