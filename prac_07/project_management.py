import datetime
from prac_07.project import Project

def load_projects(filename="projects.txt"):
    projects = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects

def save_projects(projects, filename="projects.txt"):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    incomplete = [project for project in projects if not project.is_complete()]
    completed = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete, key=lambda x: x.priority):
        print(" ", project)

    print("Completed projects:")
    for project in sorted(completed, key=lambda x: x.priority):
        print(" ", project)

def filter_projects_by_date(projects, date_str):
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = [project for project in projects if project.start_date > date]
    for project in sorted(filtered, key=lambda x: x.start_date):
        print(project)

def add_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Completion percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]

    new_completion = input("New completion percentage: ")
    new_priority = input("New priority: ")

    project.update_completion(new_completion)
    project.update_priority(new_priority)

def main():
    projects = load_projects()

    menu = """
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
        """
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt")

    running = True
    while running:
        print(menu)
        choice = input(">>> ").lower()

        if choice == "l":
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save to: ")
            save_projects(projects, filename)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            if input("Would you like to save to projects.txt? (y/n): ").lower() == "y":
                save_projects(projects)
            print("Thank you for using custom-built project management software")
            running = False
        else:
            print("Invalid choice. Try again.")


main()