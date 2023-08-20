import datetime

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

def main():
    assignments = []

    while True:
        print("\n1. Add Assignment")
        print("2. Display Assignments")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter assignment name: ")
            subject = input("Enter subject: ")
            due_date = get_due_date()
            assignment = Assignment(name, subject, due_date)
            assignments.append(assignment)
            print("Assignment added!")

        elif choice == "2":
            assignments.sort(key=lambda x: x.due_date)
            for assignment in assignments:
                weekends = count_weekends(datetime.date.today(), assignment.due_date)
                print(f"Assignment: {assignment.name}")
                print(f"Subject: {assignment.subject}")
                print(f"Due Date: {assignment.due_date}")
                print(f"Weekends before due: {weekends}\n")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
