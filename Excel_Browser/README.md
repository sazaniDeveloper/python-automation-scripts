# Excel-to-Browser (Django) 
A Django-based application that takes an Excel file as input to render its values as a table in the browser.


## Install
1. git clone https://github.com/sazaniDeveloper/python-automation-scripts.git
2. cd python-automation-scripts
3. docker build -t excel_browser .
4. docker run -p 8080:8080 excel_browser
5. Run the API through localhost:8080

## Requirements
- Python 3.0 required
- Docker installed
- Git installed
- Microsoft Excel installed

Run Without Docker: 
pip install -r requirements.txt
python manage.py runserver 8080

## Instructions
1. Click on the Upload Button to select an Excel file. 
2. Click Submit to render the table of the Excel file in the browser.
