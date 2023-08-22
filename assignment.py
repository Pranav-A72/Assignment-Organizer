import datetime
import pickle
import tkinter as tk
from tkinter import messagebox, simpledialog

class Assignment:
    def __init__(self, name, subject, due_date):
        self.name = name
        self.subject = subject
        self.due_date = due_date

def get_due_date():
    while True:
        try:
            year = int(simpledialog.askstring("Due Date", "Enter year: "))
            month = int(simpledialog.askstring("Due Date", "Enter month: "))
            day = int(simpledialog.askstring("Due Date", "Enter day: "))
            due_date = datetime.date(year, month, day)
            return due_date
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date.")

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

    root = tk.Tk()
    root.title("Schoolwork Organizer")

    def add_assignment():
        name = simpledialog.askstring("Add Assignment", "Enter assignment name:")
        subject = simpledialog.askstring("Add Assignment", "Enter subject:")
        due_date = get_due_date()
        assignment = Assignment(name, subject, due_date)
        assignments.append(assignment)
        save_assignments(assignments)
        messagebox.showinfo("Assignment Added", "Assignment added!")

    def display_assignments():
        today = datetime.date.today()
        assignments_to_display = [assignment for assignment in assignments if (assignment.due_date - today).days >= -2]
        assignments_to_display.sort(key=lambda x: x.due_date)
        
        display_window = tk.Toplevel(root)
        display_window.title("Display Assignments")
        
        for assignment in assignments_to_display:
            weekends = count_weekends(today, assignment.due_date)
            assignment_info = (
                f"Assignment: {assignment.name}\n"
                f"Subject: {assignment.subject}\n"
                f"Due Date: {assignment.due_date}\n"
                f"Weekends before due: {weekends}\n\n"
            )
            assignment_label = tk.Label(display_window, text=assignment_info, justify=tk.LEFT)
            assignment_label.pack()

    # Create GUI buttons
    add_button = tk.Button(root, text="Add Assignment", command=add_assignment)
    display_button = tk.Button(root, text="Display Assignments", command=display_assignments)
    exit_button = tk.Button(root, text="Exit", command=root.destroy)

    # Place buttons on the window
    add_button.pack(pady=10)
    display_button.pack(pady=10)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

