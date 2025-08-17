import tkinter as tk
from tkinter import ttk


def create_root():
    root = tk.Tk()
    root.title("Student Database Management System")
    root.geometry("800x500")
    var = tk.StringVar()
    label = tk.Label(root, textvariable=var, relief=tk.RAISED, font=("Arial", 18), fg="black")
    var.set("Welcome to the Student Database Management System")
    label.pack(side=tk.TOP, pady=20)
    tree = ttk.Treeview(root, columns=("ID", "First_Name", "Last_Name", "DOB", "Gender", "Email Address", "Course"), show='headings')
    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    tree.heading("ID", text="ID", anchor=tk.W)
    tree.column("ID", width=15) 
    tree.heading("First_Name", text="First Name", anchor=tk.W)
    tree.column("First_Name", width=70)
    tree.heading("Last_Name", text="Last Name", anchor=tk.W)
    tree.column("Last_Name", width=70)
    tree.heading("DOB", text="Date of Birth", anchor=tk.W)
    tree.column("DOB", width=50)
    tree.heading("Gender", text="Gender", anchor=tk.W)
    tree.column("Gender", width=50)
    tree.heading("Email Address", text="Email Address", anchor=tk.W)
    tree.column("Email Address", width=100)
    tree.heading("Course", text="Course", anchor=tk.W)
    tree.column("Course", width=100)
    return root, tree