"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
def main():
    data = load_data()
    display_subject_details(data)
def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data
def display_subject_details(data):
    """Display subject details in a formatted way."""
    for subject in data:
        code, lecturer, num_students = subject
        print(f"{code} is taught by {lecturer} and has {num_students} students")



main()