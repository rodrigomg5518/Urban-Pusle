import sqlite3
from bs4 import BeautifulSoup # type: ignore

# Define the paths to the HTML files
html_files = {
    'index': '/mnt/data/UrbanPulse_extracted/UrbanPulse/index.html',
    'reportesref': '/mnt/data/UrbanPulse_extracted/UrbanPulse/Erick/reportesref.html',
    'register': '/mnt/data/UrbanPulse_extracted/UrbanPulse/Samantha/Register.html',
    'denuncias': '/mnt/data/UrbanPulse_extracted/UrbanPulse/Eduardo/denuncias/denuncias.html'
}

# Function to extract data from HTML files
def extract_data_from_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            
            # Example extraction logic (modify according to your HTML structure)
            title = soup.title.string if soup.title else 'No Title'
            content = soup.body.get_text(separator='\n') if soup.body else 'No Content'
            
            return title, content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return "No Title", "No Content"

# Function to insert data into the database
def insert_data(db_name, table, data):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute(f'''
        INSERT INTO {table} (title, content)
        VALUES (?, ?)
    ''', data)
    
    conn.commit()
    conn.close()

# Main logic
db_name = 'urban_pulse.db'

for name, path in html_files.items():
    title, content = extract_data_from_html(path)
    insert_data(db_name, name.capitalize(), (title, content))

print("Data inserted successfully.")

