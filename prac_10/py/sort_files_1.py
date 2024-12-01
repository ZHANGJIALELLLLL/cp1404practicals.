import os
import shutil
def main():
    """Sort files into directories based on their extensions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Get a list of all files in the current directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]  # Only files, no directories

    # Set to store unique extensions
    extensions = set()

    # Loop through each file
    for filename in files:
        # Extract the file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()  # Make sure to work with lowercase extensions

        if ext:
            # Add extension to the set of extensions
            extensions.add(ext)

            # Create a directory for this extension if it doesn't exist
            if not os.path.exists(ext[1:]):  # Check if directory already exists (remove leading dot)
                os.mkdir(ext[1:])  # Create the directory (remove the dot from extension)

            # Move the file into the corresponding directory
            shutil.move(filename, os.path.join(ext[1:], filename))  # Move file to new directory

    print("Files have been sorted into directories based on their extensions.")

# Run the main function

main()