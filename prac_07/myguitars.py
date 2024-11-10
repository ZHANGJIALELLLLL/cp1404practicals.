import csv
from prac_07.guitar import Guitar

CURRENT_YEAR = 2017
VINTAGE_AGE = 50
FILE_NAME = 'guitars.csv'
def main():
    guitars = load_guitars(FILE_NAME)
    display_guitars(guitars, "Existing Guitars")

    guitars.sort()
    display_guitars(guitars, "Sorted Guitars by Year")

    guitars += get_new_guitars_from_user()
    display_guitars(guitars, "All Guitars After Adding New Ones")

    save_guitars(FILE_NAME, guitars)


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return guitars


def display_guitars(guitars, title="Guitars"):
    """Display a list of Guitar objects with a title."""
    print(f"\n{title}:")
    for guitar in guitars:
        print(guitar)


def get_new_guitars_from_user():
    """Get new guitars from user input and return them as a list."""
    new_guitars = []
    print("\nEnter new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            new_guitars.append(Guitar(name, year, cost))
        except ValueError:
            print("Invalid input. Please enter numeric values for year and cost.")
    return new_guitars


def save_guitars(filename, guitars):
    """Save a list of Guitar objects to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])
main()
