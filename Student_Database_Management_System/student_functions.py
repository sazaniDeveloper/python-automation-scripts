import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime
import random
import pyodbc
import re

def add_student(root, tree, connection_string):
    new_window = tk.Toplevel(root)
    new_window.title("Add Student")
    new_window.geometry("300x300")
    new_window.resizable(False, False)
    new_window.grid_columnconfigure(0, weight=1)
    new_window.grid_columnconfigure(1, weight=1)

    date_var = tk.StringVar()
    date_var.set("")  
    
    tk.Label(new_window, text="First Name").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    first_name_text = tk.Entry(new_window, width=20)
    first_name_text.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    tk.Label(new_window, text="Last Name").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    last_name_text = tk.Entry(new_window, width=20)
    last_name_text.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    tk.Label(new_window, text="DOB").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    cal = DateEntry(new_window, width=17, background="darkblue", foreground="white", borderwidth=2, state="readonly", textvariable=date_var)
    cal.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    tk.Label(new_window, text="Gender").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    cb = ttk.Combobox(new_window, width=17, values=["Male", "Female"], state="readonly")
    cb.set("Select Gender")
    cb.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    tk.Label(new_window, text="Email").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    email_text = tk.Entry(new_window, width=20)
    email_text.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    tk.Label(new_window, text="Course").grid(row=5, column=0, padx=5, pady=5, sticky="e")
    cb_1 = ttk.Combobox(new_window, width=17, values=["Web Development 101", "Python 101", "Java 101", "C# 101", "DevOps 101"],  state="readonly")
    cb_1.set("Select Course")
    cb_1.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    def save_student():
        if not first_name_text.get() or not last_name_text.get() or not email_text.get() or not cal.get() or not cb.get() or cb_1.get()=="Select Course":
            tk.messagebox.showerror("Input Error", "Please fill all fields")
            return
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email_text.get()):
            tk.messagebox.showerror("Input Error", "Please enter a valid email address")
            return

        student_id = random.randint(1000, 9999)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Students WHERE EMAIL_ADDRESS=?", (email_text.get(),))
        if cursor.fetchone():
            tk.messagebox.showerror("Input Error", "Email address already exists")
            return
        cmd = "INSERT INTO Students(ID, First_Name, Last_Name, DOB, Gender, Email_Address, Course) VALUES (?,?,?,?,?,?,?)"
        dob_str = cal.get_date().strftime("%Y-%m-%d")
        cursor.execute(cmd, (
            student_id,
            first_name_text.get(),
            last_name_text.get(),
            dob_str,
            cb.get(),
            email_text.get(),
            cb_1.get()
        ))
        tree.insert("", "end", values=(
            student_id,
            first_name_text.get(),
            last_name_text.get(),
            cal.get_date(),
            cb.get(),
            email_text.get(),
            cb_1.get()
        ))
        connection.commit()
        connection.close()
        new_window.destroy()
        messagebox.showinfo("Success", "Student added successfully")

    addbutton = tk.Button(new_window, text="Add Student", padx=30, pady=15, relief=tk.RAISED, command=save_student)
    addbutton.config(font=("Arial", 12, "bold"))
    addbutton.grid(row=6, column=0, columnspan=2, pady=15)




def find_student(root, tree, connection_string):
    new_window = tk.Toplevel(root)
    new_window.title("Find Student")
    new_window.geometry("700x700")
    new_window.resizable(False, False)
    new_window.grid_columnconfigure(0, weight=1)
    new_window.grid_columnconfigure(1, weight=1)

    date_var = tk.StringVar()
    date_var.set("")  
    
   
    tk.Label(new_window, text="ID").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    ID_text = tk.Entry(new_window, width=20)
    ID_text.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    tk.Label(new_window, text="First Name").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    first_name_text = tk.Entry(new_window, width=20)
    first_name_text.grid(row=1, column=1, padx=5, pady=5, sticky="w")

   
    tk.Label(new_window, text="Last Name").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    last_name_text = tk.Entry(new_window, width=20)
    last_name_text.grid(row=2, column=1, padx=5, pady=5, sticky="w")

  
    tk.Label(new_window, text="DOB").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    cal = DateEntry(new_window, width=17, background="darkblue", foreground="white", borderwidth=2, state="readonly", textvariable=date_var)
    cal.grid(row=3, column=1, padx=5, pady=5, sticky="w")

 
    tk.Label(new_window, text="Gender").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    cb = ttk.Combobox(new_window, width=17, values=["Male", "Female"], state="readonly")
    cb.set("Select Gender")
    cb.grid(row=4, column=1, padx=5, pady=5, sticky="w")


    tk.Label(new_window, text="Email").grid(row=5, column=0, padx=5, pady=5, sticky="e")
    email_text = tk.Entry(new_window, width=20)
    email_text.grid(row=5, column=1, padx=5, pady=5, sticky="w")


    tk.Label(new_window, text="Course").grid(row=6, column=0, padx=5, pady=5, sticky="e")
    cb_1 = ttk.Combobox(new_window, width=17,
                        values=["Web Development 101", "Python 101", "Java 101", "C# 101", "DevOps 101"],
                        state="readonly")
    cb_1.set("Select Course")
    cb_1.grid(row=6, column=1, padx=5, pady=5, sticky="w")

 
    tree = ttk.Treeview(new_window,
                        columns=("ID", "First_Name", "Last_Name", "DOB", "Gender", "Email Address", "Course"),
                        show='headings')
    tree.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    new_window.grid_rowconfigure(7, weight=1)
    new_window.grid_columnconfigure(0, weight=1)
    new_window.grid_columnconfigure(1, weight=1)

    for col, w in zip(("ID", "First_Name", "Last_Name", "DOB", "Gender", "Email Address", "Course"),
                      (50, 100, 100, 80, 60, 150, 150)):
        tree.heading(col, text=col, anchor=tk.W)
        tree.column(col, width=w)


    def search_student():
            student_id = ID_text.get()
            if not student_id:
                messagebox.showerror("Input Error", "Please enter Student ID")
                return

            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Students WHERE ID=?", (student_id,))
            result = cursor.fetchone()

           
            for item in tree.get_children():
                tree.delete(item)

            if result:
                dob_value = result[3]
                if isinstance(dob_value, str):
                    dob = datetime.datetime.strptime(dob_value, "%Y-%m-%d").date()
                else:
                    dob = dob_value  

                first_name_text.delete(0, tk.END)
                last_name_text.delete(0, tk.END)
                email_text.delete(0, tk.END)

                first_name_text.insert(0, result[1])
                last_name_text.insert(0, result[2])
                cal.set_date(dob)
                cb.set(result[4])
                email_text.insert(0, result[5])
                cb_1.set(result[6])

                tree.insert("", "end", values=tuple(result))
            else:
                messagebox.showerror("Not Found", "Student not found")

            connection.close()

    findbutton = tk.Button(new_window, text="Find Student", command=search_student)
    findbutton.config(font=("Arial", 12, "bold"))
    findbutton.grid(row=8, column=0, columnspan=2, pady=15)


def update_student(root, tree, connection_string):  
    new_window = tk.Toplevel(root)
    new_window.title("Update Student")
    new_window.geometry("400x400")
    new_window.resizable(False, False)

    new_window.grid_rowconfigure(7, weight=1)
    new_window.grid_columnconfigure(0, weight=1)
    new_window.grid_columnconfigure(1, weight=1)

    labels = ["ID", "First Name", "Last Name", "DOB", "Gender", "Email", "Course"]
    entries = {}

    # StringVar for DOB to allow empty initial value
    date_var = tk.StringVar()
    date_var.set("")

    for i, label in enumerate(labels):
        tk.Label(new_window, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        if label == "DOB":
            entries[label] = DateEntry(
                new_window,
                width=17,
                background="darkblue",
                foreground="white",
                borderwidth=2,
                state="readonly",
                textvariable=date_var
            )
        elif label == "Gender":
            entries[label] = ttk.Combobox(new_window, width=17, values=["Male", "Female"], state="readonly")
            entries[label].set("Select Gender")
        elif label == "Course":
            entries[label] = ttk.Combobox(
                new_window,
                width=17,
                values=["Web Development 101", "Python 101", "Java 101", "C# 101", "DevOps 101"],
                state="readonly"
            )
            entries[label].set("Select Course")
        else:
            entries[label] = tk.Entry(new_window, width=20)

        entries[label].grid(row=i, column=1, padx=5, pady=5, sticky="w")

    def do_update():
        student_id = entries["ID"].get()
        if not student_id:
            messagebox.showerror("Error", "Please enter Student ID")
            return

        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students WHERE ID=?", (student_id,))
        result = cursor.fetchone()
        if not result:
            messagebox.showerror("Error", "Student not found")
            conn.close()
            return

    
        input_first = entries["First Name"].get()
        input_last = entries["Last Name"].get()
        input_dob = entries["DOB"].get()
        input_gender = entries["Gender"].get()
        input_email = entries["Email"].get()
        input_course = entries["Course"].get()

    
        if not (input_first or input_last or input_dob or 
                (input_gender and input_gender != "Select Gender") or 
                input_email or 
                (input_course and input_course != "Select Course")):
            messagebox.showerror("Input Error", "Please update at least one field besides ID")
            conn.close()
            return


        first_name = input_first or result[1]
        last_name = input_last or result[2]
        dob = result[3]
        if input_dob:
            dob = entries["DOB"].get_date().strftime("%Y-%m-%d")
        gender = input_gender if input_gender != "Select Gender" else result[4]
        email = input_email or result[5]
        course = input_course if input_course != "Select Course" else result[6]

  
        if input_email and not re.match(r"[^@]+@[^@]+\.[^@]+", input_email):
            messagebox.showerror("Input Error", "Please enter a valid email address")
            conn.close()
            return

      
        cursor.execute("SELECT * FROM Students WHERE EMAIL_ADDRESS=? AND ID<>?", (email, student_id))
        if cursor.fetchone():
            messagebox.showerror("Input Error", "Email address already exists")
            conn.close()
            return

        cursor.execute("""
            UPDATE Students
            SET First_Name=?, Last_Name=?, DOB=?, Gender=?, Email_address=?, Course=?
            WHERE ID=?
        """, (first_name, last_name, dob, gender, email, course, student_id))
        conn.commit()
        conn.close()


        tree.delete(*tree.get_children())
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students")
        for row in cursor.fetchall():
            tree.insert("", "end", values=[str(item) for item in row])
        conn.close()

        messagebox.showinfo("Success", "Student updated successfully")
        new_window.destroy()

    tk.Button(new_window, text="Update Student", padx=30, pady=15, font=("Arial", 12, "bold"), command=do_update).grid(row=len(labels), column=0, columnspan=2, pady=15)


def delete_student(root, tree, connection_string):
    new_window = tk.Toplevel(root)
    new_window.title("Delete Student")
    new_window.geometry("300x200")
    new_window.resizable(False, False)

    new_window.grid_rowconfigure(7, weight=1)
    new_window.grid_columnconfigure(0, weight=1)
    new_window.grid_columnconfigure(1, weight=1)

    tk.Label(new_window, text="ID").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    ID_text = tk.Entry(new_window, width=20)
    ID_text.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    def do_delete():
        student_id = ID_text.get()
        if not student_id:
            messagebox.showerror("Error", "Please enter Student ID")
            return

        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students WHERE ID=?", (student_id,))
        result = cursor.fetchone()
        if not result:
            messagebox.showerror("Error", "Student not found")
            conn.close()
            return

        cursor.execute("DELETE FROM Students WHERE ID=?", (student_id,))
        conn.commit()
        conn.close()

        tree.delete(*tree.get_children())
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students")
        for row in cursor.fetchall():
            tree.insert("", "end", values=[str(item) for item in row])
        conn.close()

        messagebox.showinfo("Success", "Student deleted successfully")
        new_window.destroy()

    deletebutton = tk.Button(new_window, text="Delete Student", padx=30, pady=15, font=("Arial", 12, "bold"), command=do_delete)
    deletebutton.grid(row=1, column=0, columnspan=2, pady=15)