import datetime
import pickle

class Assignment:
    def __init__(self, name, subject, due_date):
        self.name = name
        self.subject = subject
        self.due_date = due_date

def get_due_date():
    while True:
        try:
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
            due_date = datetime.date(year, month, day)
            return due_date
        except ValueError:
            print("Invalid date. Please enter a valid date.")

def count_weekends(start_date, end_date):
    total_weekends = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() >= 5:  # Saturday or Sunday
            total_weekends += 1
        current_date += datetime.timedelta(days=1)
    return total_weekends

def save_assignments(assignments):
    with open("assignments.pkl", "wb") as f:
        pickle.dump(assignments, f)

def load_assignments():
    try:
        with open("assignments.pkl", "rb") as f:
            assignments = pickle.load(f)
            return assignments
    except FileNotFoundError:
        return []

def edit_assignment(assignment):
    print(f"Editing assignment: {assignment.name}")
    new_name = input("Enter new assignment name: ")
    new_subject = input("Enter new subject: ")
    new_due_date = get_due_date()
    assignment.name = new_name
    assignment.subject = new_subject
    assignment.due_date = new_due_date

def main():
    assignments = load_assignments()

    while True:
        print("\n1. Add Assignment")
        print("2. Display Assignments")
        print("3. Edit Assignment")
        print("4. Remove Assignment")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter assignment name: ")
            subject = input("Enter subject: ")
            due_date = get_due_date()
            assignment = Assignment(name, subject, due_date)
            assignments.append(assignment)
            print("Assignment added!")
            save_assignments(assignments)

        elif choice == "2":
            assignments.sort(key=lambda x: x.due_date)
            for assignment in assignments:
                weekends = count_weekends(datetime.date.today(), assignment.due_date)
                print(f"Assignment: {assignment.name}")
                print(f"Subject: {assignment.subject}")
                print(f"Due Date: {assignment.due_date}")
                print(f"Weekends before due: {weekends}\n")

        elif choice == "3":
            index = int(input("Enter the index of the assignment to edit: "))
            if 0 <= index < len(assignments):
                edit_assignment(assignments[index])
                save_assignments(assignments)
                print("Assignment edited!")
            else:
                print("Invalid index.")

        elif choice == "4":
            index = int(input("Enter the index of the assignment to remove: "))
            if 0 <= index < len(assignments):
                removed_assignment = assignments.pop(index)
                save_assignments(assignments)
                print(f"Assignment '{removed_assignment.name}' removed.")
            else:
                print("Invalid index.")

        elif choice == "5":
            save_assignments(assignments)
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
