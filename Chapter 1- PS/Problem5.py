import os
# Select the directory whose contents you want to list
directory_path = "/"
# Use the os moduke to list the directory path
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: The directory was not found!")
except PermissionError:
    print("Error: You don't have permission to access this directory!")
# Print the contents of the directory
print(contents)
