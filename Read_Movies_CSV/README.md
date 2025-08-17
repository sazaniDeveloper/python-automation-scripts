# Read Movies CSV
An automation script that extracts the release year of all the movies that you have listed in the Excel file and writes them in the column "Year". 

Libraries used:
- IMDbPY
- pandas
- tqdm

## Instructions
1. git clone https://github.com/sazaniDeveloper/python-automation-scripts.git
2. cd python-automation-scripts/Read_Movies_CSV
3. pip install -r requirements.txt
4. Replace the Excel file in the read_csv_file program
5. Run the project by pressing F5 or run it in the terminal python read_csv_file.py

## Requirements
- Python 3.x
- Git installed
- Excel file must have a column named "Title"

## Example
Before the script:
###Title
Madagascar
The Avengers
Forrest Gump

After the script:
###Title       ###Year
Madagascar     2005
The Avengers   2012
Forrest Gump   1994

