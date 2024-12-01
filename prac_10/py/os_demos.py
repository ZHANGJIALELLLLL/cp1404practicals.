"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # TODO: Use exception handling to avoid the crash (just pass)
    os.mkdir('temp')

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # TODO: Try these options one at a time
        # Option 1: rename file to new name - in place
        old_path = os.path.join(os.getcwd(), filename)  # full path for old file
        new_path = os.path.join(os.getcwd(), new_name)  # full path for new file
        os.rename(old_path, new_path)
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name

        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # TODO: add a loop to rename the files
        # Loop through each file in the current directory
        for filename in filenames:
            old_path = os.path.join(directory_name, filename)  # Full path for the file
            new_name = get_fixed_filename(filename)
            new_path = os.path.join(directory_name, new_name)  # Full path for the new file
            print(f"Renaming {old_path} to {new_path}")
            os.rename(old_path, new_path)

main()
# demo_walk()