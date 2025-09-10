import tkinter as tk
from tkinter import messagebox

attendance = {str(i): [] for i in range(1, 13)}

def add_attendance():
    cls = class_var.get()
    roll = roll_entry.get()
    if cls in attendance:
        attendance[cls].append(roll)
        messagebox.showinfo("Success", f"Added roll {roll} to class {cls}")
    roll_entry.delete(0, tk.END)

def show_class():
    cls = class_var.get()
    messagebox.showinfo("Attendance", f"Class {cls}: {attendance[cls]}")

def show_all():
    result = ""
    total = 0
    for cls, students in attendance.items():
        result += f"Class {cls}: {students}\n"
        total += len(students)
    result += f"\nTotal Present: {total}"
    messagebox.showinfo("All Attendance", result)

root = tk.Tk()
root.title("School Attendance")

tk.Label(root, text="Select Class:").pack()
class_var = tk.StringVar(value="1")
tk.OptionMenu(root, class_var, *attendance.keys()).pack()

tk.Label(root, text="Enter Roll No:").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Button(root, text="Add Attendance", command=add_attendance).pack()
tk.Button(root, text="Show Class", command=show_class).pack()
tk.Button(root, text="Show All", command=show_all).pack()

root.mainloop()
