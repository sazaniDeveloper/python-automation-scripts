import tkinter as tk

class Buttons:

    def __init__(self, root):
       self.button_frame = tk.Frame(root)
       self.button_frame.pack(expand=True)
    
    def button_student(self, text, cmd):
        addbutton = tk.Button(self.button_frame, text=text, padx=30, pady=15, relief=tk.RAISED, command=cmd)
        addbutton.config(font=("Arial", 12, "bold"))
        addbutton.pack(side=tk.LEFT, padx=15, pady=10)
    
