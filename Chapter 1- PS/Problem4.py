import os

# Specify the directory you want to list
directory_path = "/New folder"  # replace with your folder path

try:
    # Use os.listdir() to get the directory contents
    contents = os.listdir(directory_path)

    # Print the contents
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: The directory was not found!")
except PermissionError:
    print("Error: You don't have permission to access this directory!")
