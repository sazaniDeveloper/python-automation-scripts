import pyodbc
from buttons import Buttons
from sql_server import connection_string  
from buttons import Buttons
from tk_root import create_root
from student_functions import add_student, find_student, update_student, delete_student

root, tree = create_root()

buttons = Buttons(root)


buttons.button_student("Add Student", lambda: add_student(root, tree, connection_string))
buttons.button_student("Find Student", lambda: find_student(root, tree, connection_string))
buttons.button_student("Update Student", lambda: update_student(root, tree, connection_string))
buttons.button_student("Delete Student", lambda: delete_student(root, tree, connection_string))

try:
   connection = pyodbc.connect(connection_string)
   cursor = connection.cursor()
   query = 'SELECT * FROM Students'
   cursor.execute(query)
   rows = cursor.fetchall()

   for row in rows:
      print(row)
      tree.insert("", "end", values=[str(item) for item in row])
except pyodbc.Error as ex:
      print("An error occurred in SQL Server:", ex)


root.mainloop()