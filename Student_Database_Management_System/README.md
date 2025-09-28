# Student Database Management System 🗃️

A Tkinter GUI-based Python application that implements full CRUD operations. The application displays a Treeview that is connected to an SQL Server database to manage all the students. 

Libraries used:
- tkinter
- pyodbc
- tkcalendar
- python-dotenv
- os
- datetime
- random
- re


## Install
1. git clone https://github.com/sazaniDeveloper/python-automation-scripts.git
2. cd python-automation-scripts/Student_Database_Management_System
3. Go to the SQL query folder to initialize the database
4. Configure environment variables in .env in your own system such as the "ConnectionString" to connect the application to the SQL Server database. 
5. Go to main.py
6. Run the project by pressing F5 or by typing python main.py in the terminal

## Requirements
- Python 3.x
- Microsoft SQL SERVER installed and running.
- Git installed


## Instructions

### Add Student
Fill in all of the input fields in the add_student function, otherwise the record will not be added.

### Find Student
Enter the ID of the student and the student's record will appear in the Treeview, which is connected to the SQL Database. 

### Update Student
Enter the ID of the student and at least one input field to update the record.

### Delete Student
Enter the ID of the student to delete the record from the database. 



## Screenshots

<img width="755" height="465" alt="image" src="https://github.com/user-attachments/assets/d460aaab-67e2-4565-a1d4-0d6a391d8d1d" />
<img width="307" height="299" alt="image" src="https://github.com/user-attachments/assets/331912b6-8269-43b5-866d-ef3ae134bde3" />


