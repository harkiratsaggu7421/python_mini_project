
import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, roll, name, cls, m1, m2, m3):
        self.roll = roll
        self.name = name
        self.cls = cls
        self.marks = [m1, m2, m3]

    def details(self):
        total = sum(self.marks)
        avg = total / 3
        grade = "A" if avg >= 80 else "B" if avg >= 60 else "C" if avg >= 40 else "F"
        return f"{self.roll} | {self.name} | {self.cls} | {total} | {avg:.2f} | {grade}"

students = {}

def add():
    try:
        r, n, c = roll.get().strip(), name.get().strip(), cls.get().strip()
        if not r or not n or not c:
            raise ValueError("Enter all student details.")
        if r in students:
            raise ValueError("Roll number already exists.")
        marks = [int(e.get()) for e in (m1, m2, m3)]
        if any(x < 0 or x > 100 for x in marks):
            raise ValueError("Marks must be between 0 and 100.")
        students[r] = Student(r, n, c, *marks)
        show()
        clear()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def search():
    s = students.get(roll.get().strip())
    if s:
        name.set(s.name)
        cls.set(s.cls)
        m1.set(str(s.marks[0]))
        m2.set(str(s.marks[1]))
        m3.set(str(s.marks[2]))
        show(s)
    else:
        messagebox.showinfo("Search", "Student not found.")

def update():
    r = roll.get().strip()
    if r not in students:
        messagebox.showerror("Error", "Search a valid roll number first.")
        return
    try:
        n, c = name.get().strip(), cls.get().strip()
        if not n or not c:
            raise ValueError("Enter name and class.")
        marks = [int(e.get()) for e in (m1, m2, m3)]
        if any(x < 0 or x > 100 for x in marks):
            raise ValueError("Marks must be between 0 and 100.")
        students[r] = Student(r, n, c, *marks)
        show()
        clear()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def delete():
    r = roll.get().strip()
    if r in students:
        del students[r]
        show()
        clear()
    else:
        messagebox.showerror("Error", "Student not found.")

def show(one=None):
    output.delete("1.0", tk.END)
    output.insert(tk.END, "Roll | Name | Class | Total | Average | Grade\n")
    output.insert(tk.END, "-" * 60 + "\n")
    records = [one] if one else list(students.values())
    for s in records:
        output.insert(tk.END, s.details() + "\n")

def clear():
    for v in (roll, name, cls, m1, m2, m3):
        v.set("")

root = tk.Tk()
root.title("Student Management System")
root.geometry("700x520")

roll, name, cls = tk.StringVar(), tk.StringVar(), tk.StringVar()
m1, m2, m3 = tk.StringVar(), tk.StringVar(), tk.StringVar()

fields = [("Roll No.", roll), ("Name", name), ("Class", cls),
          ("Marks 1", m1), ("Marks 2", m2), ("Marks 3", m3)]

for i, (label, var) in enumerate(fields):
    tk.Label(root, text=label).grid(row=i, column=0, padx=8, pady=5, sticky="w")
    tk.Entry(root, textvariable=var, width=25).grid(row=i, column=1, padx=8, pady=5)

for i, (text, command) in enumerate([
    ("Add", add), ("Search", search), ("Update", update),
    ("Delete", delete), ("Show All", show), ("Clear", clear)
]):
    tk.Button(root, text=text, command=command, width=10).grid(
        row=i // 3, column=2 + i % 3, padx=4, pady=5
    )

output = tk.Text(root, width=82, height=14)
output.grid(row=7, column=0, columnspan=5, padx=8, pady=10)

show()
root.mainloop()
