import datetime
import pickle
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from ttkthemes import ThemedStyle  # Install ttkthemes using pip: pip install ttkthemes

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

def main():
    assignments = load_assignments()

    root = tk.Tk()
    root.title("Schoolwork Organizer")
    root.geometry("800x500")  # Adjust the window size as needed

    style = ThemedStyle(root)
    style.set_theme("equilux")  # You can choose other themes from ttkthemes

    def toggle_theme():
        current_theme = style.theme_use()
        new_theme = "equilux" if current_theme == "equilux-dark" else "equilux-dark"
        style.set_theme(new_theme)

    # Create a treeview to display assignments
    tree = ttk.Treeview(root, columns=("Name", "Subject", "Due Date"))
    tree.heading("#1", text="Name")
    tree.heading("#2", text="Subject")
    tree.heading("#3", text="Due Date")
    tree.pack(fill=tk.BOTH, expand=True)

    def populate_treeview():
        for assignment in assignments:
            tree.insert("", "end", values=(assignment.name, assignment.subject, assignment.due_date))

    populate_treeview()

    def add_assignment():
        name = simpledialog.askstring("Add Assignment", "Enter assignment name:")
        subject = simpledialog.askstring("Add Assignment", "Enter subject:")
        due_date = get_due_date()
        assignment = Assignment(name, subject, due_date)
        assignments.append(assignment)
        save_assignments(assignments)
        tree.insert("", "end", values=(assignment.name, assignment.subject, assignment.due_date))
        messagebox.showinfo("Assignment Added", "Assignment added!")

    def edit_assignment():
        selected_item = tree.selection()[0]
        index = tree.index(selected_item)
        assignment = assignments[index]
        new_name = simpledialog.askstring("Edit Assignment", "Enter new assignment name:", initialvalue=assignment.name)
        new_subject = simpledialog.askstring("Edit Assignment", "Enter new subject:", initialvalue=assignment.subject)
        new_due_date = get_due_date()
        assignment.name = new_name
        assignment.subject = new_subject
        assignment.due_date = new_due_date
        save_assignments(assignments)
        tree.item(selected_item, values=(assignment.name, assignment.subject, assignment.due_date))
        messagebox.showinfo("Assignment Edited", "Assignment edited!")

    def remove_assignment():
        selected_item = tree.selection()[0]
        index = tree.index(selected_item)
        removed_assignment = assignments.pop(index)
        save_assignments(assignments)
        tree.delete(selected_item)
        messagebox.showinfo("Assignment Removed", f"Assignment '{removed_assignment.name}' removed.")

    # Create buttons for actions
    add_button = ttk.Button(root, text="Add Assignment", command=add_assignment)
    edit_button = ttk.Button(root, text="Edit Assignment", command=edit_assignment)
    remove_button = ttk.Button(root, text="Remove Assignment", command=remove_assignment)
    toggle_button = ttk.Button(root, text="Toggle Theme", command=toggle_theme)

    add_button.pack(pady=5)
    edit_button.pack(pady=5)
    remove_button.pack(pady=5)
    toggle_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
