import os
import shutil
def main():
    # sort files into user-defined categories based on extensions.
    print("Starting directory is: {}".format(os.getcwd()))

    # get all list in the current directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]  # only files, no directories

    # dictionary to store extension -> category mapping
    extension_categories = {}

    # loop through each file
    for filename in files:
        # Extract the file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()  # make sure to work with lowercase extensions

        if ext:
            # if this extension hasn't been categorized yet, ask the user for a category
            if ext not in extension_categories:
                category = input(f"What category would you like to sort {ext} files into? ")
                extension_categories[ext] = category

                # create the directory for this category if it doesn't exist
                if not os.path.exists(category):
                    os.mkdir(category)

            # get the category for this extension and move the file
            category = extension_categories[ext]
            old_path = os.path.join(os.getcwd(), filename)
            new_path = os.path.join(os.getcwd(), category, filename)

            # move the file into the corresponding category directory
            shutil.move(old_path, new_path)
            print(f"Moved {filename} to {category}/")

    print("Files have been sorted into their respective categories.")

# run the main function
main()